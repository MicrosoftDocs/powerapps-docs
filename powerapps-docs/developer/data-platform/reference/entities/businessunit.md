---
title: "BusinessUnit table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the BusinessUnit table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# BusinessUnit table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Business, division, or department in the Microsoft Dynamics 365 database.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /businessunits<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /businessunits(*businessunitid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /businessunits(*businessunitid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveBusinessHierarchyBusinessUnit|<xref:Microsoft.Dynamics.CRM.RetrieveBusinessHierarchyBusinessUnit?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveBusinessHierarchyBusinessUnitRequest>|
|RetrieveMultiple|GET /businessunits<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetParentBusinessUnit|[Associate and disassociate entities](/powerapps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api)|<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|
|SetParentSystemUser|<xref:Microsoft.Dynamics.CRM.SetParentSystemUser?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|
|SetParentTeam|<xref:Microsoft.Dynamics.CRM.SetParentTeam?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|
|SetState|PATCH /businessunits(*businessunitid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /businessunits(*businessunitid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|BusinessUnits|
|DisplayCollectionName|Business Units|
|DisplayName|Business Unit|
|EntitySetName|businessunits|
|IsBPFEntity|False|
|LogicalCollectionName|businessunits|
|LogicalName|businessunit|
|OwnershipType|BusinessOwned|
|PrimaryIdAttribute|businessunitid|
|PrimaryNameAttribute|name|
|SchemaName|BusinessUnit|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Unique identifier for address 1.|
|DisplayName|Address 1: ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|address1_addressid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Address1_AddressTypeCode"></a> Address1_AddressTypeCode

|Property|Value|
|--------|-----|
|Description|Type of address for address 1, such as billing, shipping, or primary address.|
|DisplayName|Address 1: Address Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_addresstypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Address1_AddressTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Default Value||



### <a name="BKMK_Address1_City"></a> Address1_City

|Property|Value|
|--------|-----|
|Description|City name for address 1.|
|DisplayName|Bill To City|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_city|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Country"></a> Address1_Country

|Property|Value|
|--------|-----|
|Description|Country/region name for address 1.|
|DisplayName|Bill To Country/Region|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_country|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_County"></a> Address1_County

|Property|Value|
|--------|-----|
|Description|County name for address 1.|
|DisplayName|Address 1: County|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_county|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Fax"></a> Address1_Fax

|Property|Value|
|--------|-----|
|Description|Fax number for address 1.|
|DisplayName|Address 1: Fax|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_fax|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Latitude"></a> Address1_Latitude

|Property|Value|
|--------|-----|
|Description|Latitude for address 1.|
|DisplayName|Address 1: Latitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_latitude|
|MaxValue|90|
|MinValue|-90|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Address1_Line1"></a> Address1_Line1

|Property|Value|
|--------|-----|
|Description|First line for entering address 1 information.|
|DisplayName|Bill To Street 1|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_line1|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Line2"></a> Address1_Line2

|Property|Value|
|--------|-----|
|Description|Second line for entering address 1 information.|
|DisplayName|Bill To Street 2|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_line2|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Line3"></a> Address1_Line3

|Property|Value|
|--------|-----|
|Description|Third line for entering address 1 information.|
|DisplayName|Bill To Street 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_line3|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Longitude"></a> Address1_Longitude

|Property|Value|
|--------|-----|
|Description|Longitude for address 1.|
|DisplayName|Address 1: Longitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_longitude|
|MaxValue|180|
|MinValue|-180|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Address1_Name"></a> Address1_Name

|Property|Value|
|--------|-----|
|Description|Name to enter for address 1.|
|DisplayName|Address 1: Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_PostalCode"></a> Address1_PostalCode

|Property|Value|
|--------|-----|
|Description|ZIP Code or postal code for address 1.|
|DisplayName|Bill To ZIP/Postal Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_postalcode|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_PostOfficeBox"></a> Address1_PostOfficeBox

|Property|Value|
|--------|-----|
|Description|Post office box number for address 1.|
|DisplayName|Address 1: Post Office Box|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_postofficebox|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Method of shipment for address 1.|
|DisplayName|Address 1: Shipping Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_shippingmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### Address1_ShippingMethodCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Default Value||



### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

|Property|Value|
|--------|-----|
|Description|State or province for address 1.|
|DisplayName|Bill To State/Province|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_stateorprovince|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Telephone1"></a> Address1_Telephone1

|Property|Value|
|--------|-----|
|Description|First telephone number associated with address 1.|
|DisplayName|Main Phone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_telephone1|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Telephone2"></a> Address1_Telephone2

|Property|Value|
|--------|-----|
|Description|Second telephone number associated with address 1.|
|DisplayName|Other Phone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_telephone2|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Telephone3"></a> Address1_Telephone3

|Property|Value|
|--------|-----|
|Description|Third telephone number associated with address 1.|
|DisplayName|Address 1: Telephone 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_telephone3|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_UPSZone"></a> Address1_UPSZone

|Property|Value|
|--------|-----|
|Description|United Parcel Service (UPS) zone for address 1.|
|DisplayName|Address 1: UPS Zone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_upszone|
|MaxLength|4|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_UTCOffset"></a> Address1_UTCOffset

|Property|Value|
|--------|-----|
|Description|UTC offset for address 1. This is the difference between local time and standard Coordinated Universal Time.|
|DisplayName|Address 1: UTC Offset|
|Format|TimeZone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_utcoffset|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Address2_AddressId"></a> Address2_AddressId

|Property|Value|
|--------|-----|
|Description|Unique identifier for address 2.|
|DisplayName|Address 2: ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|address2_addressid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Address2_AddressTypeCode"></a> Address2_AddressTypeCode

|Property|Value|
|--------|-----|
|Description|Type of address for address 2, such as billing, shipping, or primary address.|
|DisplayName|Address 2: Address Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_addresstypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Address2_AddressTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Default Value||



### <a name="BKMK_Address2_City"></a> Address2_City

|Property|Value|
|--------|-----|
|Description|City name for address 2.|
|DisplayName|Ship To City|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_city|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Country"></a> Address2_Country

|Property|Value|
|--------|-----|
|Description|Country/region name for address 2.|
|DisplayName|Ship To Country/Region|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_country|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_County"></a> Address2_County

|Property|Value|
|--------|-----|
|Description|County name for address 2.|
|DisplayName|Address 2: County|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_county|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Fax"></a> Address2_Fax

|Property|Value|
|--------|-----|
|Description|Fax number for address 2.|
|DisplayName|Address 2: Fax|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_fax|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Latitude"></a> Address2_Latitude

|Property|Value|
|--------|-----|
|Description|Latitude for address 2.|
|DisplayName|Address 2: Latitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_latitude|
|MaxValue|90|
|MinValue|-90|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Address2_Line1"></a> Address2_Line1

|Property|Value|
|--------|-----|
|Description|First line for entering address 2 information.|
|DisplayName|Ship To Street 1|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_line1|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Line2"></a> Address2_Line2

|Property|Value|
|--------|-----|
|Description|Second line for entering address 2 information.|
|DisplayName|Ship To Street 2|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_line2|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Line3"></a> Address2_Line3

|Property|Value|
|--------|-----|
|Description|Third line for entering address 2 information.|
|DisplayName|Ship To Street 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_line3|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Longitude"></a> Address2_Longitude

|Property|Value|
|--------|-----|
|Description|Longitude for address 2.|
|DisplayName|Address 2: Longitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_longitude|
|MaxValue|180|
|MinValue|-180|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Address2_Name"></a> Address2_Name

|Property|Value|
|--------|-----|
|Description|Name to enter for address 2.|
|DisplayName|Address 2: Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_PostalCode"></a> Address2_PostalCode

|Property|Value|
|--------|-----|
|Description|ZIP Code or postal code for address 2.|
|DisplayName|Ship To ZIP/Postal Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_postalcode|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_PostOfficeBox"></a> Address2_PostOfficeBox

|Property|Value|
|--------|-----|
|Description|Post office box number for address 2.|
|DisplayName|Address 2: Post Office Box|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_postofficebox|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Method of shipment for address 2.|
|DisplayName|Address 2: Shipping Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_shippingmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### Address2_ShippingMethodCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Default Value||



### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

|Property|Value|
|--------|-----|
|Description|State or province for address 2.|
|DisplayName|Ship To State/Province|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_stateorprovince|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Telephone1"></a> Address2_Telephone1

|Property|Value|
|--------|-----|
|Description|First telephone number associated with address 2.|
|DisplayName|Address 2: Telephone 1|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_telephone1|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Telephone2"></a> Address2_Telephone2

|Property|Value|
|--------|-----|
|Description|Second telephone number associated with address 2.|
|DisplayName|Address 2: Telephone 2|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_telephone2|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Telephone3"></a> Address2_Telephone3

|Property|Value|
|--------|-----|
|Description|Third telephone number associated with address 2.|
|DisplayName|Address 2: Telephone 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_telephone3|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_UPSZone"></a> Address2_UPSZone

|Property|Value|
|--------|-----|
|Description|United Parcel Service (UPS) zone for address 2.|
|DisplayName|Address 2: UPS Zone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_upszone|
|MaxLength|4|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_UTCOffset"></a> Address2_UTCOffset

|Property|Value|
|--------|-----|
|Description|UTC offset for address 2. This is the difference between local time and standard Coordinated Universal Time.|
|DisplayName|Address 2: UTC Offset|
|Format|TimeZone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_utcoffset|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit.|
|DisplayName|Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|businessunitid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CalendarId"></a> CalendarId

|Property|Value|
|--------|-----|
|Description|Fiscal calendar associated with the business unit.|
|DisplayName|Calendar|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|calendarid|
|RequiredLevel|None|
|Targets|calendar|
|Type|Lookup|


### <a name="BKMK_CostCenter"></a> CostCenter

|Property|Value|
|--------|-----|
|Description|Name of the business unit cost center.|
|DisplayName|Cost Center|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|costcenter|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreditLimit"></a> CreditLimit

|Property|Value|
|--------|-----|
|Description|Credit limit for the business unit.|
|DisplayName|Credit Limit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|creditlimit|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the business unit.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DivisionName"></a> DivisionName

|Property|Value|
|--------|-----|
|Description|Name of the division to which the business unit belongs.|
|DisplayName|Division|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|divisionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|--------|-----|
|Description|Email address for the business unit.|
|DisplayName|Email|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileAsName"></a> FileAsName

|Property|Value|
|--------|-----|
|Description|Alternative name under which the business unit can be filed.|
|DisplayName|File as Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fileasname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FtpSiteUrl"></a> FtpSiteUrl

|Property|Value|
|--------|-----|
|Description|FTP site URL for the business unit.|
|DisplayName|FTP Site|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ftpsiteurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_InheritanceMask"></a> InheritanceMask

|Property|Value|
|--------|-----|
|Description|Inheritance mask for the business unit.|
|DisplayName|Inheritance Mask|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|inheritancemask|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsDisabled"></a> IsDisabled

|Property|Value|
|--------|-----|
|Description|Information about whether the business unit is enabled or disabled.|
|DisplayName|Is Disabled|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isdisabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDisabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the business unit.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ParentBusinessUnitId"></a> ParentBusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the parent business unit.|
|DisplayName|Parent Business|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentbusinessunitid|
|RequiredLevel|ApplicationRequired|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_Picture"></a> Picture

|Property|Value|
|--------|-----|
|Description|Picture or diagram of the business unit.|
|DisplayName|Picture|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|picture|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_StockExchange"></a> StockExchange

|Property|Value|
|--------|-----|
|Description|Stock exchange on which the business is listed.|
|DisplayName|Stock Exchange|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stockexchange|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TickerSymbol"></a> TickerSymbol

|Property|Value|
|--------|-----|
|Description|Stock exchange ticker symbol for the business unit.|
|DisplayName|Ticker Symbol|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tickersymbol|
|MaxLength|10|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the businessunit.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_UTCOffset"></a> UTCOffset

|Property|Value|
|--------|-----|
|Description|UTC offset for the business unit. This is the difference between local time and standard Coordinated Universal Time.|
|DisplayName|UTC Offset|
|Format|TimeZone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|utcoffset|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_WebSiteUrl"></a> WebSiteUrl

|Property|Value|
|--------|-----|
|Description|Website URL for the business unit.|
|DisplayName|Website|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|websiteurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WorkflowSuspended"></a> WorkflowSuspended

|Property|Value|
|--------|-----|
|Description|Information about whether workflow or sales process rules have been suspended.|
|DisplayName|Workflow Suspended|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workflowsuspended|
|RequiredLevel|None|
|Type|Boolean|

#### WorkflowSuspended Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the business unit.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the business unit was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the businessunit.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DisabledReason"></a> DisabledReason

|Property|Value|
|--------|-----|
|Description|Reason for disabling the business unit.|
|DisplayName|Disable Reason|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|disabledreason|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the businessunit with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the business unit.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the business unit was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the businessunit.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the business unit.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ParentBusinessUnitIdName"></a> ParentBusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentbusinessunitidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UserGroupId"></a> UserGroupId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|usergroupid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the business unit.|
|DisplayName|Version number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [business_unit_exchangesyncidmapping](#BKMK_business_unit_exchangesyncidmapping)
- [business_unit_interactionforemail](#BKMK_business_unit_interactionforemail)
- [business_unit_knowledgearticle](#BKMK_business_unit_knowledgearticle)
- [business_unit_sharepointdocumentlocation](#BKMK_business_unit_sharepointdocumentlocation)
- [business_unit_goal](#BKMK_business_unit_goal)
- [business_unit_mailbox](#BKMK_business_unit_mailbox)
- [business_unit_recurrencerule](#BKMK_business_unit_recurrencerule)
- [BusinessUnit_AsyncOperations](#BKMK_BusinessUnit_AsyncOperations)
- [BusinessUnit_ImportLogs](#BKMK_BusinessUnit_ImportLogs)
- [business_unit_user_settings](#BKMK_business_unit_user_settings)
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
- [BusinessUnit_DuplicateRules](#BKMK_BusinessUnit_DuplicateRules)
- [business_unit_email_activities](#BKMK_business_unit_email_activities)
- [business_unit_socialactivity](#BKMK_business_unit_socialactivity)
- [business_unit_reports](#BKMK_business_unit_reports)
- [business_unit_calendars](#BKMK_business_unit_calendars)
- [BusinessUnit_ImportMaps](#BKMK_BusinessUnit_ImportMaps)
- [business_unit_slakpiinstance](#BKMK_business_unit_slakpiinstance)
- [business_unit_recurringappointmentmaster_activities](#BKMK_business_unit_recurringappointmentmaster_activities)
- [business_unit_slabase](#BKMK_business_unit_slabase)
- [business_unit_userqueryvisualizations](#BKMK_business_unit_userqueryvisualizations)
- [business_unit_system_users](#BKMK_business_unit_system_users)
- [business_unit_socialprofiles](#BKMK_business_unit_socialprofiles)
- [BusinessUnit_BulkDeleteFailures](#BKMK_BusinessUnit_BulkDeleteFailures)
- [BusinessUnit_ProcessSessions](#BKMK_BusinessUnit_ProcessSessions)
- [business_unit_accounts](#BKMK_business_unit_accounts)
- [business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit)
- [Owning_businessunit_processsessions](#BKMK_Owning_businessunit_processsessions)
- [business_unit_activitypointer](#BKMK_business_unit_activitypointer)
- [businessunit_callbackregistration](#BKMK_businessunit_callbackregistration)
- [businessunit_canvasapp](#BKMK_businessunit_canvasapp)
- [business_unit_solutioncomponentbatchconfiguration](#BKMK_business_unit_solutioncomponentbatchconfiguration)
- [business_unit_stagesolutionupload](#BKMK_business_unit_stagesolutionupload)
- [business_unit_exportsolutionupload](#BKMK_business_unit_exportsolutionupload)
- [business_unit_featurecontrolsetting](#BKMK_business_unit_featurecontrolsetting)
- [business_unit_customapi](#BKMK_business_unit_customapi)
- [business_unit_customapirequestparameter](#BKMK_business_unit_customapirequestparameter)
- [business_unit_customapiresponseproperty](#BKMK_business_unit_customapiresponseproperty)
- [business_unit_datalakefolder](#BKMK_business_unit_datalakefolder)
- [business_unit_exportedexcel](#BKMK_business_unit_exportedexcel)
- [business_unit_retaineddataexcel](#BKMK_business_unit_retaineddataexcel)
- [business_unit_synapsedatabase](#BKMK_business_unit_synapsedatabase)
- [business_unit_msdyn_dataflow](#BKMK_business_unit_msdyn_dataflow)
- [business_unit_msdyn_dataflowrefreshhistory](#BKMK_business_unit_msdyn_dataflowrefreshhistory)
- [business_unit_msdyn_entityrefreshhistory](#BKMK_business_unit_msdyn_entityrefreshhistory)
- [business_unit_applicationuser](#BKMK_business_unit_applicationuser)
- [business_unit_connector](#BKMK_business_unit_connector)
- [business_unit_environmentvariabledefinition](#BKMK_business_unit_environmentvariabledefinition)
- [business_unit_environmentvariablevalue](#BKMK_business_unit_environmentvariablevalue)
- [business_unit_workflowbinary](#BKMK_business_unit_workflowbinary)
- [business_unit_desktopflowmodule](#BKMK_business_unit_desktopflowmodule)
- [business_unit_flowmachine](#BKMK_business_unit_flowmachine)
- [business_unit_flowmachinegroup](#BKMK_business_unit_flowmachinegroup)
- [business_unit_flowmachineimage](#BKMK_business_unit_flowmachineimage)
- [business_unit_flowmachineimageversion](#BKMK_business_unit_flowmachineimageversion)
- [business_unit_flowmachinenetwork](#BKMK_business_unit_flowmachinenetwork)
- [business_unit_processstageparameter](#BKMK_business_unit_processstageparameter)
- [business_unit_workqueue](#BKMK_business_unit_workqueue)
- [business_unit_workqueueitem](#BKMK_business_unit_workqueueitem)
- [business_unit_desktopflowbinary](#BKMK_business_unit_desktopflowbinary)
- [business_unit_flowsession](#BKMK_business_unit_flowsession)
- [business_unit_connectionreference](#BKMK_business_unit_connectionreference)
- [business_unit_connectioninstance](#BKMK_business_unit_connectioninstance)
- [business_unit_msdynce_botcontent](#BKMK_business_unit_msdynce_botcontent)
- [business_unit_conversationtranscript](#BKMK_business_unit_conversationtranscript)
- [business_unit_bot](#BKMK_business_unit_bot)
- [business_unit_botcomponent](#BKMK_business_unit_botcomponent)
- [business_unit_activityfileattachment](#BKMK_business_unit_activityfileattachment)
- [chat_businessunit_owningbusinessunit](#BKMK_chat_businessunit_owningbusinessunit)
- [business_unit_msdyn_serviceconfiguration](#BKMK_business_unit_msdyn_serviceconfiguration)
- [business_unit_msdyn_slakpi](#BKMK_business_unit_msdyn_slakpi)
- [business_unit_msdyn_knowledgemanagementsetting](#BKMK_business_unit_msdyn_knowledgemanagementsetting)
- [business_unit_msdyn_federatedarticle](#BKMK_business_unit_msdyn_federatedarticle)
- [business_unit_msdyn_integratedsearchprovider](#BKMK_business_unit_msdyn_integratedsearchprovider)
- [business_unit_msdyn_kmfederatedsearchconfig](#BKMK_business_unit_msdyn_kmfederatedsearchconfig)
- [business_unit_msdyn_knowledgearticleimage](#BKMK_business_unit_msdyn_knowledgearticleimage)
- [business_unit_msdyn_knowledgeinteractioninsight](#BKMK_business_unit_msdyn_knowledgeinteractioninsight)
- [business_unit_msdyn_knowledgesearchinsight](#BKMK_business_unit_msdyn_knowledgesearchinsight)
- [business_unit_msdyn_favoriteknowledgearticle](#BKMK_business_unit_msdyn_favoriteknowledgearticle)
- [business_unit_msdyn_kalanguagesetting](#BKMK_business_unit_msdyn_kalanguagesetting)
- [business_unit_msdyn_kbattachment](#BKMK_business_unit_msdyn_kbattachment)
- [business_unit_msdyn_knowledgearticletemplate](#BKMK_business_unit_msdyn_knowledgearticletemplate)
- [business_unit_msdyn_knowledgepersonalfilter](#BKMK_business_unit_msdyn_knowledgepersonalfilter)
- [business_unit_msdyn_knowledgesearchfilter](#BKMK_business_unit_msdyn_knowledgesearchfilter)
- [business_unit_fxexpression](#BKMK_business_unit_fxexpression)
- [business_unit_powerfxrule](#BKMK_business_unit_powerfxrule)
- [business_unit_keyvaultreference](#BKMK_business_unit_keyvaultreference)
- [business_unit_managedidentity](#BKMK_business_unit_managedidentity)
- [business_unit_retentionconfig](#BKMK_business_unit_retentionconfig)
- [business_unit_retentionfailuredetail](#BKMK_business_unit_retentionfailuredetail)
- [business_unit_retentionoperation](#BKMK_business_unit_retentionoperation)
- [business_unit_msdyn_dataflowtemplate](#BKMK_business_unit_msdyn_dataflowtemplate)
- [business_unit_appnotification](#BKMK_business_unit_appnotification)
- [business_unit_msdyn_mobileapp](#BKMK_business_unit_msdyn_mobileapp)
- [business_unit_card](#BKMK_business_unit_card)
- [business_unit_msdyn_entitylinkchatconfiguration](#BKMK_business_unit_msdyn_entitylinkchatconfiguration)
- [business_unit_msdyn_richtextfile](#BKMK_business_unit_msdyn_richtextfile)
- [business_unit_msdyn_customcontrolextendedsettings](#BKMK_business_unit_msdyn_customcontrolextendedsettings)
- [business_unit_recentlyused](#BKMK_business_unit_recentlyused)
- [business_unit_msdyn_virtualtablecolumncandidate](#BKMK_business_unit_msdyn_virtualtablecolumncandidate)
- [business_unit_msdyn_aievent](#BKMK_business_unit_msdyn_aievent)
- [business_unit_msdyn_aimodel](#BKMK_business_unit_msdyn_aimodel)
- [business_unit_msdyn_aitemplate](#BKMK_business_unit_msdyn_aitemplate)
- [business_unit_msdyn_aibfeedbackloop](#BKMK_business_unit_msdyn_aibfeedbackloop)
- [business_unit_msdyn_aifptrainingdocument](#BKMK_business_unit_msdyn_aifptrainingdocument)
- [business_unit_msdyn_aiodimage](#BKMK_business_unit_msdyn_aiodimage)
- [business_unit_msdyn_aiodlabel](#BKMK_business_unit_msdyn_aiodlabel)
- [business_unit_msdyn_aiodtrainingboundingbox](#BKMK_business_unit_msdyn_aiodtrainingboundingbox)
- [business_unit_msdyn_aiodtrainingimage](#BKMK_business_unit_msdyn_aiodtrainingimage)
- [business_unit_msdyn_aibdataset](#BKMK_business_unit_msdyn_aibdataset)
- [business_unit_msdyn_aibdatasetfile](#BKMK_business_unit_msdyn_aibdatasetfile)
- [business_unit_msdyn_aibdatasetrecord](#BKMK_business_unit_msdyn_aibdatasetrecord)
- [business_unit_msdyn_aibdatasetscontainer](#BKMK_business_unit_msdyn_aibdatasetscontainer)
- [business_unit_msdyn_aibfile](#BKMK_business_unit_msdyn_aibfile)
- [business_unit_msdyn_aibfileattacheddata](#BKMK_business_unit_msdyn_aibfileattacheddata)
- [business_unit_msdyn_pmanalysishistory](#BKMK_business_unit_msdyn_pmanalysishistory)
- [business_unit_msdyn_pmcalendar](#BKMK_business_unit_msdyn_pmcalendar)
- [business_unit_msdyn_pmcalendarversion](#BKMK_business_unit_msdyn_pmcalendarversion)
- [business_unit_msdyn_pminferredtask](#BKMK_business_unit_msdyn_pminferredtask)
- [business_unit_msdyn_pmprocessextendedmetadataversion](#BKMK_business_unit_msdyn_pmprocessextendedmetadataversion)
- [business_unit_msdyn_pmprocesstemplate](#BKMK_business_unit_msdyn_pmprocesstemplate)
- [business_unit_msdyn_pmprocessusersettings](#BKMK_business_unit_msdyn_pmprocessusersettings)
- [business_unit_msdyn_pmprocessversion](#BKMK_business_unit_msdyn_pmprocessversion)
- [business_unit_msdyn_pmrecording](#BKMK_business_unit_msdyn_pmrecording)
- [business_unit_msdyn_pmtemplate](#BKMK_business_unit_msdyn_pmtemplate)
- [business_unit_msdyn_pmview](#BKMK_business_unit_msdyn_pmview)
- [business_unit_msdyn_analysiscomponent](#BKMK_business_unit_msdyn_analysiscomponent)
- [business_unit_msdyn_analysisjob](#BKMK_business_unit_msdyn_analysisjob)
- [business_unit_msdyn_analysisoverride](#BKMK_business_unit_msdyn_analysisoverride)
- [business_unit_msdyn_analysisresult](#BKMK_business_unit_msdyn_analysisresult)
- [business_unit_msdyn_analysisresultdetail](#BKMK_business_unit_msdyn_analysisresultdetail)
- [business_unit_msdyn_solutionhealthrule](#BKMK_business_unit_msdyn_solutionhealthrule)
- [business_unit_msdyn_solutionhealthruleargument](#BKMK_business_unit_msdyn_solutionhealthruleargument)
- [business_unit_powerbidataset](#BKMK_business_unit_powerbidataset)
- [business_unit_powerbimashupparameter](#BKMK_business_unit_powerbimashupparameter)
- [business_unit_powerbireport](#BKMK_business_unit_powerbireport)
- [business_unit_msdyn_fileupload](#BKMK_business_unit_msdyn_fileupload)
- [business_unit_mspcat_catalogsubmissionfiles](#BKMK_business_unit_mspcat_catalogsubmissionfiles)
- [business_unit_mspcat_packagestore](#BKMK_business_unit_mspcat_packagestore)
- [business_unit_msdyn_schedule](#BKMK_business_unit_msdyn_schedule)
- [business_unit_msdyn_dataflow_datalakefolder](#BKMK_business_unit_msdyn_dataflow_datalakefolder)
- [business_unit_msdyn_dmsrequest](#BKMK_business_unit_msdyn_dmsrequest)
- [business_unit_msdyn_dmsrequeststatus](#BKMK_business_unit_msdyn_dmsrequeststatus)


### <a name="BKMK_business_unit_exchangesyncidmapping"></a> business_unit_exchangesyncidmapping

Same as the [business_unit_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_business_unit_exchangesyncidmapping) many-to-one relationship for the [exchangesyncidmapping](exchangesyncidmapping.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|exchangesyncidmapping|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_exchangesyncidmapping|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_interactionforemail"></a> business_unit_interactionforemail

Same as the [business_unit_interactionforemail](interactionforemail.md#BKMK_business_unit_interactionforemail) many-to-one relationship for the [interactionforemail](interactionforemail.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_new_interactionforemail|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_knowledgearticle"></a> business_unit_knowledgearticle

Same as the [business_unit_knowledgearticle](knowledgearticle.md#BKMK_business_unit_knowledgearticle) many-to-one relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_knowledgearticle|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_sharepointdocumentlocation"></a> business_unit_sharepointdocumentlocation

Same as the [business_unit_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_business_unit_sharepointdocumentlocation) many-to-one relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_sharepointdocumentlocation|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_goal"></a> business_unit_goal

Same as the [business_unit_goal](goal.md#BKMK_business_unit_goal) many-to-one relationship for the [goal](goal.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_goal|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_mailbox"></a> business_unit_mailbox

Same as the [business_unit_mailbox](mailbox.md#BKMK_business_unit_mailbox) many-to-one relationship for the [mailbox](mailbox.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_recurrencerule"></a> business_unit_recurrencerule

Same as the [business_unit_recurrencerule](recurrencerule.md#BKMK_business_unit_recurrencerule) many-to-one relationship for the [recurrencerule](recurrencerule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurrencerule|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_recurrencerule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_AsyncOperations"></a> BusinessUnit_AsyncOperations

Same as the [BusinessUnit_AsyncOperations](asyncoperation.md#BKMK_BusinessUnit_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_ImportLogs"></a> BusinessUnit_ImportLogs

Same as the [BusinessUnit_ImportLogs](importlog.md#BKMK_BusinessUnit_ImportLogs) many-to-one relationship for the [importlog](importlog.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_ImportLogs|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_user_settings"></a> business_unit_user_settings

Same as the [business_unit_user_settings](usersettings.md#BKMK_business_unit_user_settings) many-to-one relationship for the [usersettings](usersettings.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_user_settings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

Same as the [BusinessUnit_SyncError](syncerror.md#BKMK_BusinessUnit_SyncError) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_SyncError|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_sharepointsites"></a> business_unit_sharepointsites

Same as the [business_unit_sharepointsites](sharepointsite.md#BKMK_business_unit_sharepointsites) many-to-one relationship for the [sharepointsite](sharepointsite.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_sharepointsites|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_feedback"></a> business_unit_feedback

Same as the [business_unit_feedback](feedback.md#BKMK_business_unit_feedback) many-to-one relationship for the [feedback](feedback.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_feedback|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_roles"></a> business_unit_roles

Same as the [business_unit_roles](role.md#BKMK_business_unit_roles) many-to-one relationship for the [role](role.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_roles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_postfollows"></a> business_unit_postfollows

Same as the [business_unit_postfollows](postfollow.md#BKMK_business_unit_postfollows) many-to-one relationship for the [postfollow](postfollow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_postfollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_teams"></a> business_unit_teams

Same as the [business_unit_teams](team.md#BKMK_business_unit_teams) many-to-one relationship for the [team](team.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_teams|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_queues2"></a> business_unit_queues2

Same as the [business_unit_queues2](queue.md#BKMK_business_unit_queues2) many-to-one relationship for the [queue](queue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_queues2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_goalrollupquery"></a> business_unit_goalrollupquery

Same as the [business_unit_goalrollupquery](goalrollupquery.md#BKMK_business_unit_goalrollupquery) many-to-one relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_goalrollupquery|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_userquery"></a> business_unit_userquery

Same as the [business_unit_userquery](userquery.md#BKMK_business_unit_userquery) many-to-one relationship for the [userquery](userquery.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_userquery|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_Imports"></a> BusinessUnit_Imports

Same as the [BusinessUnit_Imports](import.md#BKMK_BusinessUnit_Imports) many-to-one relationship for the [import](import.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_Imports|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_ImportFiles"></a> BusinessUnit_ImportFiles

Same as the [BusinessUnit_ImportFiles](importfile.md#BKMK_BusinessUnit_ImportFiles) many-to-one relationship for the [importfile](importfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_ImportFiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_letter_activities"></a> business_unit_letter_activities

Same as the [business_unit_letter_activities](letter.md#BKMK_business_unit_letter_activities) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_letter_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_businessunit_mailboxtrackingfolder"></a> businessunit_mailboxtrackingfolder

Same as the [businessunit_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_businessunit_mailboxtrackingfolder) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|businessunit_mailboxtrackingfolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_queues"></a> business_unit_queues

Same as the [business_unit_queues](queue.md#BKMK_business_unit_queues) many-to-one relationship for the [queue](queue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_queues|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_annotations"></a> business_unit_annotations

Same as the [business_unit_annotations](annotation.md#BKMK_business_unit_annotations) many-to-one relationship for the [annotation](annotation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_workflow"></a> business_unit_workflow

Same as the [business_unit_workflow](workflow.md#BKMK_business_unit_workflow) many-to-one relationship for the [workflow](workflow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_workflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_personaldocumenttemplates"></a> business_unit_personaldocumenttemplates

Same as the [business_unit_personaldocumenttemplates](personaldocumenttemplate.md#BKMK_business_unit_personaldocumenttemplates) many-to-one relationship for the [personaldocumenttemplate](personaldocumenttemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|personaldocumenttemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_personaldocumenttemplates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_businessunit_principalobjectattributeaccess"></a> businessunit_principalobjectattributeaccess

Same as the [businessunit_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_businessunit_principalobjectattributeaccess) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|businessunit_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_emailserverprofile"></a> business_unit_emailserverprofile

Same as the [business_unit_emailserverprofile](emailserverprofile.md#BKMK_business_unit_emailserverprofile) many-to-one relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_emailserverprofile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_templates"></a> business_unit_templates

Same as the [business_unit_templates](template.md#BKMK_business_unit_templates) many-to-one relationship for the [template](template.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_templates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_contacts"></a> business_unit_contacts

Same as the [business_unit_contacts](contact.md#BKMK_business_unit_contacts) many-to-one relationship for the [contact](contact.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_contacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BulkDeleteOperation_BusinessUnit"></a> BulkDeleteOperation_BusinessUnit

Same as the [BulkDeleteOperation_BusinessUnit](bulkdeleteoperation.md#BKMK_BulkDeleteOperation_BusinessUnit) many-to-one relationship for the [bulkdeleteoperation](bulkdeleteoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeleteoperation|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BulkDeleteOperation_BusinessUnit|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_task_activities"></a> business_unit_task_activities

Same as the [business_unit_task_activities](task.md#BKMK_business_unit_task_activities) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_task_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_actioncards"></a> business_unit_actioncards

Same as the [business_unit_actioncards](actioncard.md#BKMK_business_unit_actioncards) many-to-one relationship for the [actioncard](actioncard.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_actioncards|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_asyncoperation"></a> business_unit_asyncoperation

Same as the [business_unit_asyncoperation](asyncoperation.md#BKMK_business_unit_asyncoperation) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_asyncoperation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_mailmergetemplates"></a> business_unit_mailmergetemplates

Same as the [business_unit_mailmergetemplates](mailmergetemplate.md#BKMK_business_unit_mailmergetemplates) many-to-one relationship for the [mailmergetemplate](mailmergetemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_mailmergetemplates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_userform"></a> business_unit_userform

Same as the [business_unit_userform](userform.md#BKMK_business_unit_userform) many-to-one relationship for the [userform](userform.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_userform|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_category"></a> business_unit_category

Same as the [business_unit_category](category.md#BKMK_business_unit_category) many-to-one relationship for the [category](category.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_category|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_connections"></a> business_unit_connections

Same as the [business_unit_connections](connection.md#BKMK_business_unit_connections) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_connections|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

Same as the [BusinessUnit_SyncErrors](syncerror.md#BKMK_BusinessUnit_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|BusinessUnit_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: NoCascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_business_unit_workflowlogs"></a> business_unit_workflowlogs

Same as the [business_unit_workflowlogs](workflowlog.md#BKMK_business_unit_workflowlogs) many-to-one relationship for the [workflowlog](workflowlog.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_workflowlogs|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_phone_call_activities"></a> business_unit_phone_call_activities

Same as the [business_unit_phone_call_activities](phonecall.md#BKMK_business_unit_phone_call_activities) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_phone_call_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_fax_activities"></a> business_unit_fax_activities

Same as the [business_unit_fax_activities](fax.md#BKMK_business_unit_fax_activities) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_fax_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_appointment_activities"></a> business_unit_appointment_activities

Same as the [business_unit_appointment_activities](appointment.md#BKMK_business_unit_appointment_activities) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_appointment_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_DuplicateRules"></a> BusinessUnit_DuplicateRules

Same as the [BusinessUnit_DuplicateRules](duplicaterule.md#BKMK_BusinessUnit_DuplicateRules) many-to-one relationship for the [duplicaterule](duplicaterule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_DuplicateRules|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_email_activities"></a> business_unit_email_activities

Same as the [business_unit_email_activities](email.md#BKMK_business_unit_email_activities) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_email_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_socialactivity"></a> business_unit_socialactivity

Same as the [business_unit_socialactivity](socialactivity.md#BKMK_business_unit_socialactivity) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_socialactivity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_reports"></a> business_unit_reports

Same as the [business_unit_reports](report.md#BKMK_business_unit_reports) many-to-one relationship for the [report](report.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_reports|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_calendars"></a> business_unit_calendars

Same as the [business_unit_calendars](calendar.md#BKMK_business_unit_calendars) many-to-one relationship for the [calendar](calendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|calendar|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_calendars|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_ImportMaps"></a> BusinessUnit_ImportMaps

Same as the [BusinessUnit_ImportMaps](importmap.md#BKMK_BusinessUnit_ImportMaps) many-to-one relationship for the [importmap](importmap.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_ImportMaps|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_slakpiinstance"></a> business_unit_slakpiinstance

Same as the [business_unit_slakpiinstance](slakpiinstance.md#BKMK_business_unit_slakpiinstance) many-to-one relationship for the [slakpiinstance](slakpiinstance.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_slakpiinstance|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_recurringappointmentmaster_activities"></a> business_unit_recurringappointmentmaster_activities

Same as the [business_unit_recurringappointmentmaster_activities](recurringappointmentmaster.md#BKMK_business_unit_recurringappointmentmaster_activities) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_recurringappointmentmaster_activities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_slabase"></a> business_unit_slabase

Same as the [business_unit_slabase](sla.md#BKMK_business_unit_slabase) many-to-one relationship for the [sla](sla.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_slabase|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_userqueryvisualizations"></a> business_unit_userqueryvisualizations

Same as the [business_unit_userqueryvisualizations](userqueryvisualization.md#BKMK_business_unit_userqueryvisualizations) many-to-one relationship for the [userqueryvisualization](userqueryvisualization.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_userqueryvisualizations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_system_users"></a> business_unit_system_users

Same as the [business_unit_system_users](systemuser.md#BKMK_business_unit_system_users) many-to-one relationship for the [systemuser](systemuser.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_system_users|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_socialprofiles"></a> business_unit_socialprofiles

Same as the [business_unit_socialprofiles](socialprofile.md#BKMK_business_unit_socialprofiles) many-to-one relationship for the [socialprofile](socialprofile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_socialprofiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_BulkDeleteFailures"></a> BusinessUnit_BulkDeleteFailures

Same as the [BusinessUnit_BulkDeleteFailures](bulkdeletefailure.md#BKMK_BusinessUnit_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

Same as the [BusinessUnit_ProcessSessions](processsession.md#BKMK_BusinessUnit_ProcessSessions) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_accounts"></a> business_unit_accounts

Same as the [business_unit_accounts](account.md#BKMK_business_unit_accounts) many-to-one relationship for the [account](account.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_accounts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_parent_business_unit"></a> business_unit_parent_business_unit

Same as the [business_unit_parent_business_unit](businessunit.md#BKMK_business_unit_parent_business_unit) many-to-one relationship for the [businessunit](businessunit.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|parentbusinessunitid|
|IsHierarchical|True|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_parent_business_unit|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

Same as the [Owning_businessunit_processsessions](processsession.md#BKMK_Owning_businessunit_processsessions) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Owning_businessunit_processsessions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_activitypointer"></a> business_unit_activitypointer

Same as the [business_unit_activitypointer](activitypointer.md#BKMK_business_unit_activitypointer) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|business_unit_activitypointer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_businessunit_callbackregistration"></a> businessunit_callbackregistration

Same as the [businessunit_callbackregistration](callbackregistration.md#BKMK_businessunit_callbackregistration) many-to-one relationship for the [callbackregistration](callbackregistration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|callbackregistration|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|businessunit_callbackregistration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_businessunit_canvasapp"></a> businessunit_canvasapp

Same as the [businessunit_canvasapp](canvasapp.md#BKMK_businessunit_canvasapp) many-to-one relationship for the [canvasapp](canvasapp.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|canvasapp|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|businessunit_canvasapp|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_solutioncomponentbatchconfiguration"></a> business_unit_solutioncomponentbatchconfiguration

**Added by**: Active Solution Solution

Same as the [business_unit_solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md#BKMK_business_unit_solutioncomponentbatchconfiguration) many-to-one relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_solutioncomponentbatchconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_stagesolutionupload"></a> business_unit_stagesolutionupload

**Added by**: Active Solution Solution

Same as the [business_unit_stagesolutionupload](stagesolutionupload.md#BKMK_business_unit_stagesolutionupload) many-to-one relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_stagesolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_exportsolutionupload"></a> business_unit_exportsolutionupload

**Added by**: Active Solution Solution

Same as the [business_unit_exportsolutionupload](exportsolutionupload.md#BKMK_business_unit_exportsolutionupload) many-to-one relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_exportsolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_featurecontrolsetting"></a> business_unit_featurecontrolsetting

**Added by**: Active Solution Solution

Same as the [business_unit_featurecontrolsetting](featurecontrolsetting.md#BKMK_business_unit_featurecontrolsetting) many-to-one relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_featurecontrolsetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_customapi"></a> business_unit_customapi

**Added by**: Active Solution Solution

Same as the [business_unit_customapi](customapi.md#BKMK_business_unit_customapi) many-to-one relationship for the [customapi](customapi.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_customapi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_customapirequestparameter"></a> business_unit_customapirequestparameter

**Added by**: Active Solution Solution

Same as the [business_unit_customapirequestparameter](customapirequestparameter.md#BKMK_business_unit_customapirequestparameter) many-to-one relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_customapirequestparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_customapiresponseproperty"></a> business_unit_customapiresponseproperty

**Added by**: Active Solution Solution

Same as the [business_unit_customapiresponseproperty](customapiresponseproperty.md#BKMK_business_unit_customapiresponseproperty) many-to-one relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_customapiresponseproperty|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_datalakefolder"></a> business_unit_datalakefolder

**Added by**: Active Solution Solution

Same as the [business_unit_datalakefolder](datalakefolder.md#BKMK_business_unit_datalakefolder) many-to-one relationship for the [datalakefolder](datalakefolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_datalakefolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_exportedexcel"></a> business_unit_exportedexcel

**Added by**: Active Solution Solution

Same as the [business_unit_exportedexcel](exportedexcel.md#BKMK_business_unit_exportedexcel) many-to-one relationship for the [exportedexcel](exportedexcel.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportedexcel|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_exportedexcel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_retaineddataexcel"></a> business_unit_retaineddataexcel

**Added by**: Active Solution Solution

Same as the [business_unit_retaineddataexcel](retaineddataexcel.md#BKMK_business_unit_retaineddataexcel) many-to-one relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retaineddataexcel|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_retaineddataexcel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_synapsedatabase"></a> business_unit_synapsedatabase

**Added by**: Active Solution Solution

Same as the [business_unit_synapsedatabase](synapsedatabase.md#BKMK_business_unit_synapsedatabase) many-to-one relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapsedatabase|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_synapsedatabase|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_dataflow"></a> business_unit_msdyn_dataflow

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_dataflow](msdyn_dataflow.md#BKMK_business_unit_msdyn_dataflow) many-to-one relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_dataflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_dataflowrefreshhistory"></a> business_unit_msdyn_dataflowrefreshhistory

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md#BKMK_business_unit_msdyn_dataflowrefreshhistory) many-to-one relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflowrefreshhistory|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_dataflowrefreshhistory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_entityrefreshhistory"></a> business_unit_msdyn_entityrefreshhistory

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md#BKMK_business_unit_msdyn_entityrefreshhistory) many-to-one relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_entityrefreshhistory|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_entityrefreshhistory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_applicationuser"></a> business_unit_applicationuser

**Added by**: ApplicationUserSolution Solution

Same as the [business_unit_applicationuser](applicationuser.md#BKMK_business_unit_applicationuser) many-to-one relationship for the [applicationuser](applicationuser.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|applicationuser|
|ReferencingAttribute|businessunitid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_applicationuser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_connector"></a> business_unit_connector

**Added by**: Active Solution Solution

Same as the [business_unit_connector](connector.md#BKMK_business_unit_connector) many-to-one relationship for the [connector](connector.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_connector|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_environmentvariabledefinition"></a> business_unit_environmentvariabledefinition

**Added by**: Active Solution Solution

Same as the [business_unit_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_business_unit_environmentvariabledefinition) many-to-one relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_environmentvariabledefinition|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_environmentvariablevalue"></a> business_unit_environmentvariablevalue

**Added by**: Active Solution Solution

Same as the [business_unit_environmentvariablevalue](environmentvariablevalue.md#BKMK_business_unit_environmentvariablevalue) many-to-one relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_environmentvariablevalue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_workflowbinary"></a> business_unit_workflowbinary

**Added by**: Active Solution Solution

Same as the [business_unit_workflowbinary](workflowbinary.md#BKMK_business_unit_workflowbinary) many-to-one relationship for the [workflowbinary](workflowbinary.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_workflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_desktopflowmodule"></a> business_unit_desktopflowmodule

**Added by**: Active Solution Solution

Same as the [business_unit_desktopflowmodule](desktopflowmodule.md#BKMK_business_unit_desktopflowmodule) many-to-one relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|desktopflowmodule|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_desktopflowmodule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_flowmachine"></a> business_unit_flowmachine

**Added by**: Active Solution Solution

Same as the [business_unit_flowmachine](flowmachine.md#BKMK_business_unit_flowmachine) many-to-one relationship for the [flowmachine](flowmachine.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_flowmachine|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_flowmachinegroup"></a> business_unit_flowmachinegroup

**Added by**: Active Solution Solution

Same as the [business_unit_flowmachinegroup](flowmachinegroup.md#BKMK_business_unit_flowmachinegroup) many-to-one relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_flowmachinegroup|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_flowmachineimage"></a> business_unit_flowmachineimage

**Added by**: Active Solution Solution

Same as the [business_unit_flowmachineimage](flowmachineimage.md#BKMK_business_unit_flowmachineimage) many-to-one relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachineimage|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_flowmachineimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_flowmachineimageversion"></a> business_unit_flowmachineimageversion

**Added by**: Active Solution Solution

Same as the [business_unit_flowmachineimageversion](flowmachineimageversion.md#BKMK_business_unit_flowmachineimageversion) many-to-one relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachineimageversion|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_flowmachineimageversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_flowmachinenetwork"></a> business_unit_flowmachinenetwork

**Added by**: Active Solution Solution

Same as the [business_unit_flowmachinenetwork](flowmachinenetwork.md#BKMK_business_unit_flowmachinenetwork) many-to-one relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinenetwork|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_flowmachinenetwork|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_processstageparameter"></a> business_unit_processstageparameter

**Added by**: Active Solution Solution

Same as the [business_unit_processstageparameter](processstageparameter.md#BKMK_business_unit_processstageparameter) many-to-one relationship for the [processstageparameter](processstageparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_processstageparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_workqueue"></a> business_unit_workqueue

**Added by**: Active Solution Solution

Same as the [business_unit_workqueue](workqueue.md#BKMK_business_unit_workqueue) many-to-one relationship for the [workqueue](workqueue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workqueue|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_workqueue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_workqueueitem"></a> business_unit_workqueueitem

**Added by**: Active Solution Solution

Same as the [business_unit_workqueueitem](workqueueitem.md#BKMK_business_unit_workqueueitem) many-to-one relationship for the [workqueueitem](workqueueitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workqueueitem|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_workqueueitem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_desktopflowbinary"></a> business_unit_desktopflowbinary

**Added by**: Active Solution Solution

Same as the [business_unit_desktopflowbinary](desktopflowbinary.md#BKMK_business_unit_desktopflowbinary) many-to-one relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|desktopflowbinary|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_desktopflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_flowsession"></a> business_unit_flowsession

**Added by**: Active Solution Solution

Same as the [business_unit_flowsession](flowsession.md#BKMK_business_unit_flowsession) many-to-one relationship for the [flowsession](flowsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_flowsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_connectionreference"></a> business_unit_connectionreference

**Added by**: Active Solution Solution

Same as the [business_unit_connectionreference](connectionreference.md#BKMK_business_unit_connectionreference) many-to-one relationship for the [connectionreference](connectionreference.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_connectionreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_connectioninstance"></a> business_unit_connectioninstance

**Added by**: Active Solution Solution

Same as the [business_unit_connectioninstance](connectioninstance.md#BKMK_business_unit_connectioninstance) many-to-one relationship for the [connectioninstance](connectioninstance.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectioninstance|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_connectioninstance|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdynce_botcontent"></a> business_unit_msdynce_botcontent

**Added by**: Active Solution Solution

Same as the [business_unit_msdynce_botcontent](msdynce_botcontent.md#BKMK_business_unit_msdynce_botcontent) many-to-one relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdynce_botcontent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_conversationtranscript"></a> business_unit_conversationtranscript

**Added by**: Active Solution Solution

Same as the [business_unit_conversationtranscript](conversationtranscript.md#BKMK_business_unit_conversationtranscript) many-to-one relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_conversationtranscript|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_bot"></a> business_unit_bot

**Added by**: Active Solution Solution

Same as the [business_unit_bot](bot.md#BKMK_business_unit_bot) many-to-one relationship for the [bot](bot.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_bot|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_botcomponent"></a> business_unit_botcomponent

**Added by**: Active Solution Solution

Same as the [business_unit_botcomponent](botcomponent.md#BKMK_business_unit_botcomponent) many-to-one relationship for the [botcomponent](botcomponent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_botcomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_activityfileattachment"></a> business_unit_activityfileattachment

**Added by**: Activities Patch Solution

Same as the [business_unit_activityfileattachment](activityfileattachment.md#BKMK_business_unit_activityfileattachment) many-to-one relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_activityfileattachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_chat_businessunit_owningbusinessunit"></a> chat_businessunit_owningbusinessunit

**Added by**: Activities Patch Solution

Same as the [chat_businessunit_owningbusinessunit](chat.md#BKMK_chat_businessunit_owningbusinessunit) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|chat_businessunit_owningbusinessunit|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_serviceconfiguration"></a> business_unit_msdyn_serviceconfiguration

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md#BKMK_business_unit_msdyn_serviceconfiguration) many-to-one relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_serviceconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_slakpi"></a> business_unit_msdyn_slakpi

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_slakpi](msdyn_slakpi.md#BKMK_business_unit_msdyn_slakpi) many-to-one relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_slakpi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgemanagementsetting"></a> business_unit_msdyn_knowledgemanagementsetting

**Added by**: Knowledge Management Patch Solution

Same as the [business_unit_msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md#BKMK_business_unit_msdyn_knowledgemanagementsetting) many-to-one relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgemanagementsetting|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgemanagementsetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_federatedarticle"></a> business_unit_msdyn_federatedarticle

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_federatedarticle](msdyn_federatedarticle.md#BKMK_business_unit_msdyn_federatedarticle) many-to-one relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_federatedarticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_integratedsearchprovider"></a> business_unit_msdyn_integratedsearchprovider

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md#BKMK_business_unit_msdyn_integratedsearchprovider) many-to-one relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_integratedsearchprovider|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_integratedsearchprovider|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_kmfederatedsearchconfig"></a> business_unit_msdyn_kmfederatedsearchconfig

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md#BKMK_business_unit_msdyn_kmfederatedsearchconfig) many-to-one relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_kmfederatedsearchconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgearticleimage"></a> business_unit_msdyn_knowledgearticleimage

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_business_unit_msdyn_knowledgearticleimage) many-to-one relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgearticleimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgeinteractioninsight"></a> business_unit_msdyn_knowledgeinteractioninsight

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md#BKMK_business_unit_msdyn_knowledgeinteractioninsight) many-to-one relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgeinteractioninsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgesearchinsight"></a> business_unit_msdyn_knowledgesearchinsight

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md#BKMK_business_unit_msdyn_knowledgesearchinsight) many-to-one relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgesearchinsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_favoriteknowledgearticle"></a> business_unit_msdyn_favoriteknowledgearticle

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md#BKMK_business_unit_msdyn_favoriteknowledgearticle) many-to-one relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_favoriteknowledgearticle|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_favoriteknowledgearticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_kalanguagesetting"></a> business_unit_msdyn_kalanguagesetting

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_kalanguagesetting](msdyn_kalanguagesetting.md#BKMK_business_unit_msdyn_kalanguagesetting) many-to-one relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_kalanguagesetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_kbattachment"></a> business_unit_msdyn_kbattachment

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_kbattachment](msdyn_kbattachment.md#BKMK_business_unit_msdyn_kbattachment) many-to-one relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_kbattachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgearticletemplate"></a> business_unit_msdyn_knowledgearticletemplate

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_business_unit_msdyn_knowledgearticletemplate) many-to-one relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgearticletemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgepersonalfilter"></a> business_unit_msdyn_knowledgepersonalfilter

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md#BKMK_business_unit_msdyn_knowledgepersonalfilter) many-to-one relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgepersonalfilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_knowledgesearchfilter"></a> business_unit_msdyn_knowledgesearchfilter

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md#BKMK_business_unit_msdyn_knowledgesearchfilter) many-to-one relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_knowledgesearchfilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_fxexpression"></a> business_unit_fxexpression

**Added by**: Active Solution Solution

Same as the [business_unit_fxexpression](fxexpression.md#BKMK_business_unit_fxexpression) many-to-one relationship for the [fxexpression](fxexpression.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fxexpression|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_fxexpression|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_powerfxrule"></a> business_unit_powerfxrule

**Added by**: Active Solution Solution

Same as the [business_unit_powerfxrule](powerfxrule.md#BKMK_business_unit_powerfxrule) many-to-one relationship for the [powerfxrule](powerfxrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerfxrule|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_powerfxrule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_keyvaultreference"></a> business_unit_keyvaultreference

**Added by**: Active Solution Solution

Same as the [business_unit_keyvaultreference](keyvaultreference.md#BKMK_business_unit_keyvaultreference) many-to-one relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_keyvaultreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_managedidentity"></a> business_unit_managedidentity

**Added by**: Active Solution Solution

Same as the [business_unit_managedidentity](managedidentity.md#BKMK_business_unit_managedidentity) many-to-one relationship for the [managedidentity](managedidentity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_managedidentity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_retentionconfig"></a> business_unit_retentionconfig

**Added by**: Active Solution Solution

Same as the [business_unit_retentionconfig](retentionconfig.md#BKMK_business_unit_retentionconfig) many-to-one relationship for the [retentionconfig](retentionconfig.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retentionconfig|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_retentionconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_retentionfailuredetail"></a> business_unit_retentionfailuredetail

**Added by**: Active Solution Solution

Same as the [business_unit_retentionfailuredetail](retentionfailuredetail.md#BKMK_business_unit_retentionfailuredetail) many-to-one relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retentionfailuredetail|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_retentionfailuredetail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_retentionoperation"></a> business_unit_retentionoperation

**Added by**: Active Solution Solution

Same as the [business_unit_retentionoperation](retentionoperation.md#BKMK_business_unit_retentionoperation) many-to-one relationship for the [retentionoperation](retentionoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retentionoperation|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_retentionoperation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_dataflowtemplate"></a> business_unit_msdyn_dataflowtemplate

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_dataflowtemplate](msdyn_dataflowtemplate.md#BKMK_business_unit_msdyn_dataflowtemplate) many-to-one relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflowtemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_dataflowtemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_appnotification"></a> business_unit_appnotification

**Added by**: Active Solution Solution

Same as the [business_unit_appnotification](appnotification.md#BKMK_business_unit_appnotification) many-to-one relationship for the [appnotification](appnotification.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_appnotification|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_mobileapp"></a> business_unit_msdyn_mobileapp

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_mobileapp](msdyn_mobileapp.md#BKMK_business_unit_msdyn_mobileapp) many-to-one relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_mobileapp|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_mobileapp|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_card"></a> business_unit_card

**Added by**: Active Solution Solution

Same as the [business_unit_card](card.md#BKMK_business_unit_card) many-to-one relationship for the [card](card.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|card|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_card|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_entitylinkchatconfiguration"></a> business_unit_msdyn_entitylinkchatconfiguration

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md#BKMK_business_unit_msdyn_entitylinkchatconfiguration) many-to-one relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_entitylinkchatconfiguration|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_entitylinkchatconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_richtextfile"></a> business_unit_msdyn_richtextfile

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_richtextfile](msdyn_richtextfile.md#BKMK_business_unit_msdyn_richtextfile) many-to-one relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_richtextfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_customcontrolextendedsettings"></a> business_unit_msdyn_customcontrolextendedsettings

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md#BKMK_business_unit_msdyn_customcontrolextendedsettings) many-to-one relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_customcontrolextendedsettings|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_customcontrolextendedsettings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_recentlyused"></a> business_unit_recentlyused

**Added by**: Active Solution Solution

Same as the [business_unit_recentlyused](recentlyused.md#BKMK_business_unit_recentlyused) many-to-one relationship for the [recentlyused](recentlyused.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recentlyused|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_recentlyused|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_virtualtablecolumncandidate"></a> business_unit_msdyn_virtualtablecolumncandidate

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md#BKMK_business_unit_msdyn_virtualtablecolumncandidate) many-to-one relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_virtualtablecolumncandidate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_virtualtablecolumncandidate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aievent"></a> business_unit_msdyn_aievent

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aievent](msdyn_aievent.md#BKMK_business_unit_msdyn_aievent) many-to-one relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aievent|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aievent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aimodel"></a> business_unit_msdyn_aimodel

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aimodel](msdyn_aimodel.md#BKMK_business_unit_msdyn_aimodel) many-to-one relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aimodel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aitemplate"></a> business_unit_msdyn_aitemplate

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_business_unit_msdyn_aitemplate) many-to-one relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aitemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibfeedbackloop"></a> business_unit_msdyn_aibfeedbackloop

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md#BKMK_business_unit_msdyn_aibfeedbackloop) many-to-one relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfeedbackloop|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibfeedbackloop|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aifptrainingdocument"></a> business_unit_msdyn_aifptrainingdocument

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_business_unit_msdyn_aifptrainingdocument) many-to-one relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aifptrainingdocument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aiodimage"></a> business_unit_msdyn_aiodimage

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_business_unit_msdyn_aiodimage) many-to-one relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aiodimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aiodlabel"></a> business_unit_msdyn_aiodlabel

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_business_unit_msdyn_aiodlabel) many-to-one relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aiodlabel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aiodtrainingboundingbox"></a> business_unit_msdyn_aiodtrainingboundingbox

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_business_unit_msdyn_aiodtrainingboundingbox) many-to-one relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aiodtrainingboundingbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aiodtrainingimage"></a> business_unit_msdyn_aiodtrainingimage

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_business_unit_msdyn_aiodtrainingimage) many-to-one relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aiodtrainingimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibdataset"></a> business_unit_msdyn_aibdataset

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_business_unit_msdyn_aibdataset) many-to-one relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibdataset|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibdatasetfile"></a> business_unit_msdyn_aibdatasetfile

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_business_unit_msdyn_aibdatasetfile) many-to-one relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibdatasetfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibdatasetrecord"></a> business_unit_msdyn_aibdatasetrecord

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_business_unit_msdyn_aibdatasetrecord) many-to-one relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibdatasetrecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibdatasetscontainer"></a> business_unit_msdyn_aibdatasetscontainer

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_business_unit_msdyn_aibdatasetscontainer) many-to-one relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibdatasetscontainer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibfile"></a> business_unit_msdyn_aibfile

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibfile](msdyn_aibfile.md#BKMK_business_unit_msdyn_aibfile) many-to-one relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_aibfileattacheddata"></a> business_unit_msdyn_aibfileattacheddata

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_business_unit_msdyn_aibfileattacheddata) many-to-one relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_aibfileattacheddata|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmanalysishistory"></a> business_unit_msdyn_pmanalysishistory

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmanalysishistory](msdyn_pmanalysishistory.md#BKMK_business_unit_msdyn_pmanalysishistory) many-to-one relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmanalysishistory|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmanalysishistory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmcalendar"></a> business_unit_msdyn_pmcalendar

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmcalendar](msdyn_pmcalendar.md#BKMK_business_unit_msdyn_pmcalendar) many-to-one relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmcalendar|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmcalendarversion"></a> business_unit_msdyn_pmcalendarversion

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmcalendarversion](msdyn_pmcalendarversion.md#BKMK_business_unit_msdyn_pmcalendarversion) many-to-one relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmcalendarversion|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmcalendarversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pminferredtask"></a> business_unit_msdyn_pminferredtask

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_business_unit_msdyn_pminferredtask) many-to-one relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pminferredtask|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmprocessextendedmetadataversion"></a> business_unit_msdyn_pmprocessextendedmetadataversion

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md#BKMK_business_unit_msdyn_pmprocessextendedmetadataversion) many-to-one relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocessextendedmetadataversion|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmprocessextendedmetadataversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmprocesstemplate"></a> business_unit_msdyn_pmprocesstemplate

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md#BKMK_business_unit_msdyn_pmprocesstemplate) many-to-one relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocesstemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmprocesstemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmprocessusersettings"></a> business_unit_msdyn_pmprocessusersettings

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md#BKMK_business_unit_msdyn_pmprocessusersettings) many-to-one relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocessusersettings|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmprocessusersettings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmprocessversion"></a> business_unit_msdyn_pmprocessversion

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmprocessversion](msdyn_pmprocessversion.md#BKMK_business_unit_msdyn_pmprocessversion) many-to-one relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocessversion|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmprocessversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmrecording"></a> business_unit_msdyn_pmrecording

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_business_unit_msdyn_pmrecording) many-to-one relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmrecording|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmtemplate"></a> business_unit_msdyn_pmtemplate

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmtemplate](msdyn_pmtemplate.md#BKMK_business_unit_msdyn_pmtemplate) many-to-one relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmtemplate|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmtemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_pmview"></a> business_unit_msdyn_pmview

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_pmview](msdyn_pmview.md#BKMK_business_unit_msdyn_pmview) many-to-one relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmview|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_pmview|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_analysiscomponent"></a> business_unit_msdyn_analysiscomponent

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_business_unit_msdyn_analysiscomponent) many-to-one relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_analysiscomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_analysisjob"></a> business_unit_msdyn_analysisjob

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_business_unit_msdyn_analysisjob) many-to-one relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_analysisjob|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_analysisoverride"></a> business_unit_msdyn_analysisoverride

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_analysisoverride](msdyn_analysisoverride.md#BKMK_business_unit_msdyn_analysisoverride) many-to-one relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisoverride|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_analysisoverride|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_analysisresult"></a> business_unit_msdyn_analysisresult

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_business_unit_msdyn_analysisresult) many-to-one relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_analysisresult|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_analysisresultdetail"></a> business_unit_msdyn_analysisresultdetail

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_business_unit_msdyn_analysisresultdetail) many-to-one relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_analysisresultdetail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_solutionhealthrule"></a> business_unit_msdyn_solutionhealthrule

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_business_unit_msdyn_solutionhealthrule) many-to-one relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_solutionhealthrule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_solutionhealthruleargument"></a> business_unit_msdyn_solutionhealthruleargument

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_business_unit_msdyn_solutionhealthruleargument) many-to-one relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_solutionhealthruleargument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_powerbidataset"></a> business_unit_powerbidataset

**Added by**: Active Solution Solution

Same as the [business_unit_powerbidataset](powerbidataset.md#BKMK_business_unit_powerbidataset) many-to-one relationship for the [powerbidataset](powerbidataset.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbidataset|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_powerbidataset|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_powerbimashupparameter"></a> business_unit_powerbimashupparameter

**Added by**: Active Solution Solution

Same as the [business_unit_powerbimashupparameter](powerbimashupparameter.md#BKMK_business_unit_powerbimashupparameter) many-to-one relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbimashupparameter|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_powerbimashupparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_powerbireport"></a> business_unit_powerbireport

**Added by**: Active Solution Solution

Same as the [business_unit_powerbireport](powerbireport.md#BKMK_business_unit_powerbireport) many-to-one relationship for the [powerbireport](powerbireport.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbireport|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_powerbireport|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_fileupload"></a> business_unit_msdyn_fileupload

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_fileupload](msdyn_fileupload.md#BKMK_business_unit_msdyn_fileupload) many-to-one relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_fileupload|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_fileupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_mspcat_catalogsubmissionfiles"></a> business_unit_mspcat_catalogsubmissionfiles

**Added by**: Active Solution Solution

Same as the [business_unit_mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md#BKMK_business_unit_mspcat_catalogsubmissionfiles) many-to-one relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspcat_catalogsubmissionfiles|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_mspcat_catalogsubmissionfiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_mspcat_packagestore"></a> business_unit_mspcat_packagestore

**Added by**: Active Solution Solution

Same as the [business_unit_mspcat_packagestore](mspcat_packagestore.md#BKMK_business_unit_mspcat_packagestore) many-to-one relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspcat_packagestore|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_mspcat_packagestore|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_schedule"></a> business_unit_msdyn_schedule

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_schedule](msdyn_schedule.md#BKMK_business_unit_msdyn_schedule) many-to-one relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_schedule|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_schedule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_dataflow_datalakefolder"></a> business_unit_msdyn_dataflow_datalakefolder

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md#BKMK_business_unit_msdyn_dataflow_datalakefolder) many-to-one relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow_datalakefolder|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_dataflow_datalakefolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_dmsrequest"></a> business_unit_msdyn_dmsrequest

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_dmsrequest](msdyn_dmsrequest.md#BKMK_business_unit_msdyn_dmsrequest) many-to-one relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dmsrequest|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_dmsrequest|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_business_unit_msdyn_dmsrequeststatus"></a> business_unit_msdyn_dmsrequeststatus

**Added by**: Active Solution Solution

Same as the [business_unit_msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md#BKMK_business_unit_msdyn_dmsrequeststatus) many-to-one relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dmsrequeststatus|
|ReferencingAttribute|owningbusinessunit|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|business_unit_msdyn_dmsrequeststatus|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [TransactionCurrency_BusinessUnit](#BKMK_TransactionCurrency_BusinessUnit)
- [lk_businessunitbase_createdby](#BKMK_lk_businessunitbase_createdby)
- [lk_businessunit_modifiedonbehalfby](#BKMK_lk_businessunit_modifiedonbehalfby)
- [business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit)
- [organization_business_units](#BKMK_organization_business_units)
- [lk_businessunit_createdonbehalfby](#BKMK_lk_businessunit_createdonbehalfby)
- [lk_businessunitbase_modifiedby](#BKMK_lk_businessunitbase_modifiedby)
- [BusinessUnit_Calendar](#BKMK_BusinessUnit_Calendar)


### <a name="BKMK_TransactionCurrency_BusinessUnit"></a> TransactionCurrency_BusinessUnit

See the [TransactionCurrency_BusinessUnit](transactioncurrency.md#BKMK_TransactionCurrency_BusinessUnit) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_lk_businessunitbase_createdby"></a> lk_businessunitbase_createdby

See the [lk_businessunitbase_createdby](systemuser.md#BKMK_lk_businessunitbase_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_businessunit_modifiedonbehalfby"></a> lk_businessunit_modifiedonbehalfby

See the [lk_businessunit_modifiedonbehalfby](systemuser.md#BKMK_lk_businessunit_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_business_unit_parent_business_unit"></a> business_unit_parent_business_unit

See the [business_unit_parent_business_unit](businessunit.md#BKMK_business_unit_parent_business_unit) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_organization_business_units"></a> organization_business_units

See the [organization_business_units](organization.md#BKMK_organization_business_units) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_lk_businessunit_createdonbehalfby"></a> lk_businessunit_createdonbehalfby

See the [lk_businessunit_createdonbehalfby](systemuser.md#BKMK_lk_businessunit_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_businessunitbase_modifiedby"></a> lk_businessunitbase_modifiedby

See the [lk_businessunitbase_modifiedby](systemuser.md#BKMK_lk_businessunitbase_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_BusinessUnit_Calendar"></a> BusinessUnit_Calendar

See the [BusinessUnit_Calendar](calendar.md#BKMK_BusinessUnit_Calendar) one-to-many relationship for the [calendar](calendar.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.businessunit?text=businessunit EntityType" />