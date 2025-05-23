---
title: "Account table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Account table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Account table/entity reference (Microsoft Dataverse)

Business that represents a customer or potential customer. The company that is billed in business transactions.

## Messages

The following table lists the messages for the Account table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /accounts(*accountid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /accounts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /accounts(*accountid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: True |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Merge`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Merge?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.MergeRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /accounts(*accountid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /accounts<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /accounts(*accountid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /accounts(*accountid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /accounts(*accountid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Account table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Account table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Account** |
| **DisplayCollectionName** | **Accounts** |
| **SchemaName** | `Account` |
| **CollectionSchemaName** | `Accounts` |
| **EntitySetName** | `accounts`|
| **LogicalName** | `account` |
| **LogicalCollectionName** | `accounts` |
| **PrimaryIdAttribute** | `accountid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccountCategoryCode](#BKMK_AccountCategoryCode)
- [AccountClassificationCode](#BKMK_AccountClassificationCode)
- [AccountId](#BKMK_AccountId)
- [AccountNumber](#BKMK_AccountNumber)
- [AccountRatingCode](#BKMK_AccountRatingCode)
- [Address1_AddressId](#BKMK_Address1_AddressId)
- [Address1_AddressTypeCode](#BKMK_Address1_AddressTypeCode)
- [Address1_City](#BKMK_Address1_City)
- [Address1_Country](#BKMK_Address1_Country)
- [Address1_County](#BKMK_Address1_County)
- [Address1_Fax](#BKMK_Address1_Fax)
- [Address1_FreightTermsCode](#BKMK_Address1_FreightTermsCode)
- [Address1_Latitude](#BKMK_Address1_Latitude)
- [Address1_Line1](#BKMK_Address1_Line1)
- [Address1_Line2](#BKMK_Address1_Line2)
- [Address1_Line3](#BKMK_Address1_Line3)
- [Address1_Longitude](#BKMK_Address1_Longitude)
- [Address1_Name](#BKMK_Address1_Name)
- [Address1_PostalCode](#BKMK_Address1_PostalCode)
- [Address1_PostOfficeBox](#BKMK_Address1_PostOfficeBox)
- [Address1_PrimaryContactName](#BKMK_Address1_PrimaryContactName)
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
- [Address2_FreightTermsCode](#BKMK_Address2_FreightTermsCode)
- [Address2_Latitude](#BKMK_Address2_Latitude)
- [Address2_Line1](#BKMK_Address2_Line1)
- [Address2_Line2](#BKMK_Address2_Line2)
- [Address2_Line3](#BKMK_Address2_Line3)
- [Address2_Longitude](#BKMK_Address2_Longitude)
- [Address2_Name](#BKMK_Address2_Name)
- [Address2_PostalCode](#BKMK_Address2_PostalCode)
- [Address2_PostOfficeBox](#BKMK_Address2_PostOfficeBox)
- [Address2_PrimaryContactName](#BKMK_Address2_PrimaryContactName)
- [Address2_ShippingMethodCode](#BKMK_Address2_ShippingMethodCode)
- [Address2_StateOrProvince](#BKMK_Address2_StateOrProvince)
- [Address2_Telephone1](#BKMK_Address2_Telephone1)
- [Address2_Telephone2](#BKMK_Address2_Telephone2)
- [Address2_Telephone3](#BKMK_Address2_Telephone3)
- [Address2_UPSZone](#BKMK_Address2_UPSZone)
- [Address2_UTCOffset](#BKMK_Address2_UTCOffset)
- [Adx_CreatedByIPAddress](#BKMK_Adx_CreatedByIPAddress)
- [Adx_CreatedByUsername](#BKMK_Adx_CreatedByUsername)
- [Adx_ModifiedByIPAddress](#BKMK_Adx_ModifiedByIPAddress)
- [Adx_ModifiedByUsername](#BKMK_Adx_ModifiedByUsername)
- [BusinessTypeCode](#BKMK_BusinessTypeCode)
- [CreditLimit](#BKMK_CreditLimit)
- [CreditOnHold](#BKMK_CreditOnHold)
- [CustomerSizeCode](#BKMK_CustomerSizeCode)
- [CustomerTypeCode](#BKMK_CustomerTypeCode)
- [Description](#BKMK_Description)
- [DoNotBulkEMail](#BKMK_DoNotBulkEMail)
- [DoNotBulkPostalMail](#BKMK_DoNotBulkPostalMail)
- [DoNotEMail](#BKMK_DoNotEMail)
- [DoNotFax](#BKMK_DoNotFax)
- [DoNotPhone](#BKMK_DoNotPhone)
- [DoNotPostalMail](#BKMK_DoNotPostalMail)
- [DoNotSendMM](#BKMK_DoNotSendMM)
- [EMailAddress1](#BKMK_EMailAddress1)
- [EMailAddress2](#BKMK_EMailAddress2)
- [EMailAddress3](#BKMK_EMailAddress3)
- [EntityImage](#BKMK_EntityImage)
- [Fax](#BKMK_Fax)
- [FollowEmail](#BKMK_FollowEmail)
- [FtpSiteURL](#BKMK_FtpSiteURL)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IndustryCode](#BKMK_IndustryCode)
- [LastOnHoldTime](#BKMK_LastOnHoldTime)
- [LastUsedInCampaign](#BKMK_LastUsedInCampaign)
- [MarketCap](#BKMK_MarketCap)
- [MarketingOnly](#BKMK_MarketingOnly)
- [msa_managingpartnerid](#BKMK_msa_managingpartnerid)
- [Name](#BKMK_Name)
- [NumberOfEmployees](#BKMK_NumberOfEmployees)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwnershipCode](#BKMK_OwnershipCode)
- [ParentAccountId](#BKMK_ParentAccountId)
- [ParticipatesInWorkflow](#BKMK_ParticipatesInWorkflow)
- [PaymentTermsCode](#BKMK_PaymentTermsCode)
- [PreferredAppointmentDayCode](#BKMK_PreferredAppointmentDayCode)
- [PreferredAppointmentTimeCode](#BKMK_PreferredAppointmentTimeCode)
- [PreferredContactMethodCode](#BKMK_PreferredContactMethodCode)
- [PreferredSystemUserId](#BKMK_PreferredSystemUserId)
- [PrimaryContactId](#BKMK_PrimaryContactId)
- [PrimarySatoriId](#BKMK_PrimarySatoriId)
- [PrimaryTwitterId](#BKMK_PrimaryTwitterId)
- [ProcessId](#BKMK_ProcessId)
- [Revenue](#BKMK_Revenue)
- [SharesOutstanding](#BKMK_SharesOutstanding)
- [ShippingMethodCode](#BKMK_ShippingMethodCode)
- [SIC](#BKMK_SIC)
- [SLAId](#BKMK_SLAId)
- [StageId](#BKMK_StageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [StockExchange](#BKMK_StockExchange)
- [Telephone1](#BKMK_Telephone1)
- [Telephone2](#BKMK_Telephone2)
- [Telephone3](#BKMK_Telephone3)
- [TerritoryCode](#BKMK_TerritoryCode)
- [TickerSymbol](#BKMK_TickerSymbol)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WebSiteURL](#BKMK_WebSiteURL)
- [YomiName](#BKMK_YomiName)

### <a name="BKMK_AccountCategoryCode"></a> AccountCategoryCode

|Property|Value|
|---|---|
|Description|**Select a category to indicate whether the customer account is standard or preferred.**|
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accountcategorycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_accountcategorycode`|

#### AccountCategoryCode Choices/Options

|Value|Label|
|---|---|
|1|**Preferred Customer**|
|2|**Standard**|

### <a name="BKMK_AccountClassificationCode"></a> AccountClassificationCode

|Property|Value|
|---|---|
|Description|**Select a classification code to indicate the potential value of the customer account based on the projected return on investment, cooperation level, sales cycle length or other criteria.**|
|DisplayName|**Classification**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accountclassificationcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_accountclassificationcode`|

#### AccountClassificationCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_AccountId"></a> AccountId

|Property|Value|
|---|---|
|Description|**Unique identifier of the account.**|
|DisplayName|**Account**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`accountid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AccountNumber"></a> AccountNumber

|Property|Value|
|---|---|
|Description|**Type an ID number or code for the account to quickly search and identify the account in system views.**|
|DisplayName|**Account Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accountnumber`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_AccountRatingCode"></a> AccountRatingCode

|Property|Value|
|---|---|
|Description|**Select a rating to indicate the value of the customer account.**|
|DisplayName|**Account Rating**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accountratingcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_accountratingcode`|

#### AccountRatingCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

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
|Description|**Select the primary address type.**|
|DisplayName|**Address 1: Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_address1_addresstypecode`|

#### Address1_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Bill To**|
|2|**Ship To**|
|3|**Primary**|
|4|**Other**|

### <a name="BKMK_Address1_City"></a> Address1_City

|Property|Value|
|---|---|
|Description|**Type the city for the primary address.**|
|DisplayName|**Address 1: City**|
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
|Description|**Type the country or region for the primary address.**|
|DisplayName|**Address 1: Country/Region**|
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
|Description|**Type the county for the primary address.**|
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
|Description|**Type the fax number associated with the primary address.**|
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

### <a name="BKMK_Address1_FreightTermsCode"></a> Address1_FreightTermsCode

|Property|Value|
|---|---|
|Description|**Select the freight terms for the primary address to make sure shipping orders are processed correctly.**|
|DisplayName|**Address 1: Freight Terms**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_freighttermscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_address1_freighttermscode`|

#### Address1_FreightTermsCode Choices/Options

|Value|Label|
|---|---|
|1|**FOB**|
|2|**No Charge**|

### <a name="BKMK_Address1_Latitude"></a> Address1_Latitude

|Property|Value|
|---|---|
|Description|**Type the latitude value for the primary address for use in mapping and other applications.**|
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
|Description|**Type the first line of the primary address.**|
|DisplayName|**Address 1: Street 1**|
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
|Description|**Type the second line of the primary address.**|
|DisplayName|**Address 1: Street 2**|
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
|Description|**Type the third line of the primary address.**|
|DisplayName|**Address 1: Street 3**|
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
|Description|**Type the longitude value for the primary address for use in mapping and other applications.**|
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
|Description|**Type a descriptive name for the primary address, such as Corporate Headquarters.**|
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
|MaxLength|200|

### <a name="BKMK_Address1_PostalCode"></a> Address1_PostalCode

|Property|Value|
|---|---|
|Description|**Type the ZIP Code or postal code for the primary address.**|
|DisplayName|**Address 1: ZIP/Postal Code**|
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
|Description|**Type the post office box number of the primary address.**|
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

### <a name="BKMK_Address1_PrimaryContactName"></a> Address1_PrimaryContactName

|Property|Value|
|---|---|
|Description|**Type the name of the main contact at the account's primary address.**|
|DisplayName|**Address 1: Primary Contact Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_primarycontactname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Select a shipping method for deliveries sent to this address.**|
|DisplayName|**Address 1: Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_address1_shippingmethodcode`|

#### Address1_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Airborne**|
|2|**DHL**|
|3|**FedEx**|
|4|**UPS**|
|5|**Postal Mail**|
|6|**Full Load**|
|7|**Will Call**|

### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

|Property|Value|
|---|---|
|Description|**Type the state or province of the primary address.**|
|DisplayName|**Address 1: State/Province**|
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
|Description|**Type the main phone number associated with the primary address.**|
|DisplayName|**Address Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Telephone2"></a> Address1_Telephone2

|Property|Value|
|---|---|
|Description|**Type a second phone number associated with the primary address.**|
|DisplayName|**Address 1: Telephone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Telephone3"></a> Address1_Telephone3

|Property|Value|
|---|---|
|Description|**Type a third phone number associated with the primary address.**|
|DisplayName|**Address 1: Telephone 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_UPSZone"></a> Address1_UPSZone

|Property|Value|
|---|---|
|Description|**Type the UPS zone of the primary address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.**|
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
|Description|**Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.**|
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
|Description|**Select the secondary address type.**|
|DisplayName|**Address 2: Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_address2_addresstypecode`|

#### Address2_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_City"></a> Address2_City

|Property|Value|
|---|---|
|Description|**Type the city for the secondary address.**|
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
|Description|**Type the country or region for the secondary address.**|
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
|Description|**Type the county for the secondary address.**|
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
|Description|**Type the fax number associated with the secondary address.**|
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

### <a name="BKMK_Address2_FreightTermsCode"></a> Address2_FreightTermsCode

|Property|Value|
|---|---|
|Description|**Select the freight terms for the secondary address to make sure shipping orders are processed correctly.**|
|DisplayName|**Address 2: Freight Terms**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_freighttermscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_address2_freighttermscode`|

#### Address2_FreightTermsCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_Latitude"></a> Address2_Latitude

|Property|Value|
|---|---|
|Description|**Type the latitude value for the secondary address for use in mapping and other applications.**|
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
|Description|**Type the first line of the secondary address.**|
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
|MaxLength|250|

### <a name="BKMK_Address2_Line2"></a> Address2_Line2

|Property|Value|
|---|---|
|Description|**Type the second line of the secondary address.**|
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
|MaxLength|250|

### <a name="BKMK_Address2_Line3"></a> Address2_Line3

|Property|Value|
|---|---|
|Description|**Type the third line of the secondary address.**|
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
|MaxLength|250|

### <a name="BKMK_Address2_Longitude"></a> Address2_Longitude

|Property|Value|
|---|---|
|Description|**Type the longitude value for the secondary address for use in mapping and other applications.**|
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
|Description|**Type a descriptive name for the secondary address, such as Corporate Headquarters.**|
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
|MaxLength|200|

### <a name="BKMK_Address2_PostalCode"></a> Address2_PostalCode

|Property|Value|
|---|---|
|Description|**Type the ZIP Code or postal code for the secondary address.**|
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
|Description|**Type the post office box number of the secondary address.**|
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

### <a name="BKMK_Address2_PrimaryContactName"></a> Address2_PrimaryContactName

|Property|Value|
|---|---|
|Description|**Type the name of the main contact at the account's secondary address.**|
|DisplayName|**Address 2: Primary Contact Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_primarycontactname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Select a shipping method for deliveries sent to this address.**|
|DisplayName|**Address 2: Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_address2_shippingmethodcode`|

#### Address2_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

|Property|Value|
|---|---|
|Description|**Type the state or province of the secondary address.**|
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
|Description|**Type the main phone number associated with the secondary address.**|
|DisplayName|**Address 2: Telephone 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Telephone2"></a> Address2_Telephone2

|Property|Value|
|---|---|
|Description|**Type a second phone number associated with the secondary address.**|
|DisplayName|**Address 2: Telephone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Telephone3"></a> Address2_Telephone3

|Property|Value|
|---|---|
|Description|**Type a third phone number associated with the secondary address.**|
|DisplayName|**Address 2: Telephone 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_UPSZone"></a> Address2_UPSZone

|Property|Value|
|---|---|
|Description|**Type the UPS zone of the secondary address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.**|
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
|Description|**Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.**|
|DisplayName|**Address 2: UTC Offset**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_utcoffset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_Adx_CreatedByIPAddress"></a> Adx_CreatedByIPAddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**Created By (IP Address)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_createdbyipaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Adx_CreatedByUsername"></a> Adx_CreatedByUsername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Created By (User Name)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_createdbyusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Adx_ModifiedByIPAddress"></a> Adx_ModifiedByIPAddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**Modified By (IP Address)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_modifiedbyipaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Adx_ModifiedByUsername"></a> Adx_ModifiedByUsername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Modified By (User Name)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_modifiedbyusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_BusinessTypeCode"></a> BusinessTypeCode

|Property|Value|
|---|---|
|Description|**Select the legal designation or other business type of the account for contracts or reporting purposes.**|
|DisplayName|**Business Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`businesstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_businesstypecode`|

#### BusinessTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_CreditLimit"></a> CreditLimit

|Property|Value|
|---|---|
|Description|**Type the credit limit of the account. This is a useful reference when you address invoice and accounting issues with the customer.**|
|DisplayName|**Credit Limit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`creditlimit`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_CreditOnHold"></a> CreditOnHold

|Property|Value|
|---|---|
|Description|**Select whether the credit for the account is on hold. This is a useful reference while addressing the invoice and accounting issues with the customer.**|
|DisplayName|**Credit Hold**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`creditonhold`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_creditonhold`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CustomerSizeCode"></a> CustomerSizeCode

|Property|Value|
|---|---|
|Description|**Select the size category or range of the account for segmentation and reporting purposes.**|
|DisplayName|**Customer Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customersizecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_customersizecode`|

#### CustomerSizeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_CustomerTypeCode"></a> CustomerTypeCode

|Property|Value|
|---|---|
|Description|**Select the category that best describes the relationship between the account and your organization.**|
|DisplayName|**Relationship Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customertypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_customertypecode`|

#### CustomerTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Competitor**|
|2|**Consultant**|
|3|**Customer**|
|4|**Investor**|
|5|**Partner**|
|6|**Influencer**|
|7|**Press**|
|8|**Prospect**|
|9|**Reseller**|
|10|**Supplier**|
|11|**Vendor**|
|12|**Other**|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the account, such as an excerpt from the company's website.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_DoNotBulkEMail"></a> DoNotBulkEMail

|Property|Value|
|---|---|
|Description|**Select whether the account allows bulk email sent through campaigns. If Do Not Allow is selected, the account can be added to marketing lists, but is excluded from email.**|
|DisplayName|**Do not allow Bulk Emails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotbulkemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotbulkemail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotBulkPostalMail"></a> DoNotBulkPostalMail

|Property|Value|
|---|---|
|Description|**Select whether the account allows bulk postal mail sent through marketing campaigns or quick campaigns. If Do Not Allow is selected, the account can be added to marketing lists, but will be excluded from the postal mail.**|
|DisplayName|**Do not allow Bulk Mails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotbulkpostalmail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotbulkpostalmail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_DoNotEMail"></a> DoNotEMail

|Property|Value|
|---|---|
|Description|**Select whether the account allows direct email sent from Microsoft Dynamics 365.**|
|DisplayName|**Do not allow Emails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotemail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotFax"></a> DoNotFax

|Property|Value|
|---|---|
|Description|**Select whether the account allows faxes. If Do Not Allow is selected, the account will be excluded from fax activities distributed in marketing campaigns.**|
|DisplayName|**Do not allow Faxes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotfax`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotfax`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotPhone"></a> DoNotPhone

|Property|Value|
|---|---|
|Description|**Select whether the account allows phone calls. If Do Not Allow is selected, the account will be excluded from phone call activities distributed in marketing campaigns.**|
|DisplayName|**Do not allow Phone Calls**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotphone`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotphone`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotPostalMail"></a> DoNotPostalMail

|Property|Value|
|---|---|
|Description|**Select whether the account allows direct mail. If Do Not Allow is selected, the account will be excluded from letter activities distributed in marketing campaigns.**|
|DisplayName|**Do not allow Mails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotpostalmail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotpostalmail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotSendMM"></a> DoNotSendMM

|Property|Value|
|---|---|
|Description|**Select whether the account accepts marketing materials, such as brochures or catalogs.**|
|DisplayName|**Send Marketing Materials**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotsendmm`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_donotsendmm`|
|DefaultValue|False|
|True Label|Do Not Send|
|False Label|Send|

### <a name="BKMK_EMailAddress1"></a> EMailAddress1

|Property|Value|
|---|---|
|Description|**Type the primary email address for the account.**|
|DisplayName|**Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddress1`|
|RequiredLevel|None|
|Type|String|
|Format|Email|
|FormatName|Email|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EMailAddress2"></a> EMailAddress2

|Property|Value|
|---|---|
|Description|**Type the secondary email address for the account.**|
|DisplayName|**Email Address 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddress2`|
|RequiredLevel|None|
|Type|String|
|Format|Email|
|FormatName|Email|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EMailAddress3"></a> EMailAddress3

|Property|Value|
|---|---|
|Description|**Type an alternate email address for the account.**|
|DisplayName|**Email Address 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddress3`|
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
|DisplayName|**Default Image**|
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

### <a name="BKMK_Fax"></a> Fax

|Property|Value|
|---|---|
|Description|**Type the fax number for the account.**|
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

### <a name="BKMK_FollowEmail"></a> FollowEmail

|Property|Value|
|---|---|
|Description|**Information about whether to allow following email activity like opens, attachment views and link clicks for emails sent to the account.**|
|DisplayName|**Follow Email Activity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`followemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_followemail`|
|DefaultValue|True|
|True Label|Allow|
|False Label|Do Not Allow|

### <a name="BKMK_FtpSiteURL"></a> FtpSiteURL

|Property|Value|
|---|---|
|Description|**Type the URL for the account's FTP site to enable users to access data and share documents.**|
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

### <a name="BKMK_IndustryCode"></a> IndustryCode

|Property|Value|
|---|---|
|Description|**Select the account's primary industry for use in marketing segmentation and demographic analysis.**|
|DisplayName|**Industry**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`industrycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_industrycode`|

#### IndustryCode Choices/Options

|Value|Label|
|---|---|
|1|**Accounting**|
|2|**Agriculture and Non-petrol Natural Resource Extraction**|
|3|**Broadcasting Printing and Publishing**|
|4|**Brokers**|
|5|**Building Supply Retail**|
|6|**Business Services**|
|7|**Consulting**|
|8|**Consumer Services**|
|9|**Design, Direction and Creative Management**|
|10|**Distributors, Dispatchers and Processors**|
|11|**Doctor's Offices and Clinics**|
|12|**Durable Manufacturing**|
|13|**Eating and Drinking Places**|
|14|**Entertainment Retail**|
|15|**Equipment Rental and Leasing**|
|16|**Financial**|
|17|**Food and Tobacco Processing**|
|18|**Inbound Capital Intensive Processing**|
|19|**Inbound Repair and Services**|
|20|**Insurance**|
|21|**Legal Services**|
|22|**Non-Durable Merchandise Retail**|
|23|**Outbound Consumer Service**|
|24|**Petrochemical Extraction and Distribution**|
|25|**Service Retail**|
|26|**SIG Affiliations**|
|27|**Social Services**|
|28|**Special Outbound Trade Contractors**|
|29|**Specialty Realty**|
|30|**Transportation**|
|31|**Utility Creation and Distribution**|
|32|**Vehicle Retail**|
|33|**Wholesale**|

### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

|Property|Value|
|---|---|
|Description|**Contains the date and time stamp of the last on hold time.**|
|DisplayName|**Last On Hold Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastonholdtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastUsedInCampaign"></a> LastUsedInCampaign

|Property|Value|
|---|---|
|Description|**Shows the date when the account was last included in a marketing campaign or quick campaign.**|
|DisplayName|**Last Date Included in Campaign**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastusedincampaign`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_MarketCap"></a> MarketCap

|Property|Value|
|---|---|
|Description|**Type the market capitalization of the account to identify the company's equity, used as an indicator in financial performance analysis.**|
|DisplayName|**Market Capitalization**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`marketcap`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_MarketingOnly"></a> MarketingOnly

|Property|Value|
|---|---|
|Description|**Whether is only for marketing**|
|DisplayName|**Marketing Only**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`marketingonly`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_marketingonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msa_managingpartnerid"></a> msa_managingpartnerid

|Property|Value|
|---|---|
|Description|**Unique identifier for Account associated with Account.**|
|DisplayName|**Managing Partner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msa_managingpartnerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type the company or business name.**|
|DisplayName|**Account Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_NumberOfEmployees"></a> NumberOfEmployees

|Property|Value|
|---|---|
|Description|**Type the number of employees that work at the account for use in marketing segmentation and demographic analysis.**|
|DisplayName|**Number of Employees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`numberofemployees`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_OwnershipCode"></a> OwnershipCode

|Property|Value|
|---|---|
|Description|**Select the account's ownership structure, such as public or private.**|
|DisplayName|**Ownership**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownershipcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_ownershipcode`|

#### OwnershipCode Choices/Options

|Value|Label|
|---|---|
|1|**Public**|
|2|**Private**|
|3|**Subsidiary**|
|4|**Other**|

### <a name="BKMK_ParentAccountId"></a> ParentAccountId

|Property|Value|
|---|---|
|Description|**Choose the parent account associated with this account to show parent and child businesses in reporting and analytics.**|
|DisplayName|**Parent Account**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentaccountid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

### <a name="BKMK_ParticipatesInWorkflow"></a> ParticipatesInWorkflow

|Property|Value|
|---|---|
|Description|**For system use only. Legacy Microsoft Dynamics CRM 3.0 workflow data.**|
|DisplayName|**Participates in Workflow**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`participatesinworkflow`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_participatesinworkflow`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PaymentTermsCode"></a> PaymentTermsCode

|Property|Value|
|---|---|
|Description|**Select the payment terms to indicate when the customer needs to pay the total amount.**|
|DisplayName|**Payment Terms**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`paymenttermscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_paymenttermscode`|

#### PaymentTermsCode Choices/Options

|Value|Label|
|---|---|
|1|**Net 30**|
|2|**2% 10, Net 30**|
|3|**Net 45**|
|4|**Net 60**|

### <a name="BKMK_PreferredAppointmentDayCode"></a> PreferredAppointmentDayCode

|Property|Value|
|---|---|
|Description|**Select the preferred day of the week for service appointments.**|
|DisplayName|**Preferred Day**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredappointmentdaycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_preferredappointmentdaycode`|

#### PreferredAppointmentDayCode Choices/Options

|Value|Label|
|---|---|
|0|**Sunday**|
|1|**Monday**|
|2|**Tuesday**|
|3|**Wednesday**|
|4|**Thursday**|
|5|**Friday**|
|6|**Saturday**|

### <a name="BKMK_PreferredAppointmentTimeCode"></a> PreferredAppointmentTimeCode

|Property|Value|
|---|---|
|Description|**Select the preferred time of day for service appointments.**|
|DisplayName|**Preferred Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredappointmenttimecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_preferredappointmenttimecode`|

#### PreferredAppointmentTimeCode Choices/Options

|Value|Label|
|---|---|
|1|**Morning**|
|2|**Afternoon**|
|3|**Evening**|

### <a name="BKMK_PreferredContactMethodCode"></a> PreferredContactMethodCode

|Property|Value|
|---|---|
|Description|**Select the preferred method of contact.**|
|DisplayName|**Preferred Method of Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredcontactmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_preferredcontactmethodcode`|

#### PreferredContactMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Any**|
|2|**Email**|
|3|**Phone**|
|4|**Fax**|
|5|**Mail**|

### <a name="BKMK_PreferredSystemUserId"></a> PreferredSystemUserId

|Property|Value|
|---|---|
|Description|**Choose the preferred service representative for reference when you schedule service activities for the account.**|
|DisplayName|**Preferred User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredsystemuserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_PrimaryContactId"></a> PrimaryContactId

|Property|Value|
|---|---|
|Description|**Choose the primary contact for the account to provide quick access to contact details.**|
|DisplayName|**Primary Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primarycontactid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_PrimarySatoriId"></a> PrimarySatoriId

|Property|Value|
|---|---|
|Description|**Primary Satori ID for Account**|
|DisplayName|**Primary Satori ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primarysatoriid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_PrimaryTwitterId"></a> PrimaryTwitterId

|Property|Value|
|---|---|
|Description|**Primary Twitter ID for Account**|
|DisplayName|**Primary Twitter ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primarytwitterid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Revenue"></a> Revenue

|Property|Value|
|---|---|
|Description|**Type the annual revenue for the account, used as an indicator in financial performance analysis.**|
|DisplayName|**Annual Revenue**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`revenue`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_SharesOutstanding"></a> SharesOutstanding

|Property|Value|
|---|---|
|Description|**Type the number of shares available to the public for the account. This number is used as an indicator in financial performance analysis.**|
|DisplayName|**Shares Outstanding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sharesoutstanding`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_ShippingMethodCode"></a> ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Select a shipping method for deliveries sent to the account's address to designate the preferred carrier or other delivery option.**|
|DisplayName|**Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_shippingmethodcode`|

#### ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_SIC"></a> SIC

|Property|Value|
|---|---|
|Description|**Type the Standard Industrial Classification (SIC) code that indicates the account's primary industry of business, for use in marketing segmentation and demographic analysis.**|
|DisplayName|**SIC Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sic`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Choose the service level agreement (SLA) that you want to apply to the Account record.**|
|DisplayName|**SLA**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slaid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the account is active or inactive. Inactive accounts are read-only and can't be edited unless they are reactivated.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`account_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the account's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`account_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_StockExchange"></a> StockExchange

|Property|Value|
|---|---|
|Description|**Type the stock exchange at which the account is listed to track their stock and financial performance of the company.**|
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

### <a name="BKMK_Telephone1"></a> Telephone1

|Property|Value|
|---|---|
|Description|**Type the main phone number for this account.**|
|DisplayName|**Main Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Telephone2"></a> Telephone2

|Property|Value|
|---|---|
|Description|**Type a second phone number for this account.**|
|DisplayName|**Other Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Telephone3"></a> Telephone3

|Property|Value|
|---|---|
|Description|**Type a third phone number for this account.**|
|DisplayName|**Telephone 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_TerritoryCode"></a> TerritoryCode

|Property|Value|
|---|---|
|Description|**Select a region or territory for the account for use in segmentation and analysis.**|
|DisplayName|**Territory Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`territorycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`account_territorycode`|

#### TerritoryCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_TickerSymbol"></a> TickerSymbol

|Property|Value|
|---|---|
|Description|**Type the stock exchange symbol for the account to track financial performance of the company. You can click the code entered in this field to access the latest trading information from MSN Money.**|
|DisplayName|**Ticker Symbol**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tickersymbol`|
|RequiredLevel|None|
|Type|String|
|Format|TickerSymbol|
|FormatName|TickerSymbol|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

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

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

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

### <a name="BKMK_WebSiteURL"></a> WebSiteURL

|Property|Value|
|---|---|
|Description|**Type the account's website URL to get quick details about the company profile.**|
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

### <a name="BKMK_YomiName"></a> YomiName

|Property|Value|
|---|---|
|Description|**Type the phonetic spelling of the company name, if specified in Japanese, to make sure the name is pronounced correctly in phone calls and other communications.**|
|DisplayName|**Yomi Account Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yominame`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Address1_Composite](#BKMK_Address1_Composite)
- [Address2_Composite](#BKMK_Address2_Composite)
- [Aging30](#BKMK_Aging30)
- [Aging30_Base](#BKMK_Aging30_Base)
- [Aging60](#BKMK_Aging60)
- [Aging60_Base](#BKMK_Aging60_Base)
- [Aging90](#BKMK_Aging90)
- [Aging90_Base](#BKMK_Aging90_Base)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByExternalParty](#BKMK_CreatedByExternalParty)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreditLimit_Base](#BKMK_CreditLimit_Base)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsPrivate](#BKMK_IsPrivate)
- [MarketCap_Base](#BKMK_MarketCap_Base)
- [MasterId](#BKMK_MasterId)
- [Merged](#BKMK_Merged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByExternalParty](#BKMK_ModifiedByExternalParty)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Revenue_Base](#BKMK_Revenue_Base)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [TimeSpentByMeOnEmailAndMeetings](#BKMK_TimeSpentByMeOnEmailAndMeetings)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_Address1_Composite"></a> Address1_Composite

|Property|Value|
|---|---|
|Description|**Shows the complete primary address.**|
|DisplayName|**Address 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_composite`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_Address2_Composite"></a> Address2_Composite

|Property|Value|
|---|---|
|Description|**Shows the complete secondary address.**|
|DisplayName|**Address 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_composite`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_Aging30"></a> Aging30

|Property|Value|
|---|---|
|Description|**For system use only.**|
|DisplayName|**Aging 30**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aging30`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Aging30_Base"></a> Aging30_Base

|Property|Value|
|---|---|
|Description|**The base currency equivalent of the aging 30 field.**|
|DisplayName|**Aging 30 (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aging30_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Aging60"></a> Aging60

|Property|Value|
|---|---|
|Description|**For system use only.**|
|DisplayName|**Aging 60**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aging60`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Aging60_Base"></a> Aging60_Base

|Property|Value|
|---|---|
|Description|**The base currency equivalent of the aging 60 field.**|
|DisplayName|**Aging 60 (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aging60_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Aging90"></a> Aging90

|Property|Value|
|---|---|
|Description|**For system use only.**|
|DisplayName|**Aging 90**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aging90`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Aging90_Base"></a> Aging90_Base

|Property|Value|
|---|---|
|Description|**The base currency equivalent of the aging 90 field.**|
|DisplayName|**Aging 90 (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aging90_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

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

### <a name="BKMK_CreatedByExternalParty"></a> CreatedByExternalParty

|Property|Value|
|---|---|
|Description|**Shows the external party who created the record.**|
|DisplayName|**Created By (External Party)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdbyexternalparty`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|externalparty|

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

### <a name="BKMK_CreditLimit_Base"></a> CreditLimit_Base

|Property|Value|
|---|---|
|Description|**Shows the credit limit converted to the system's default base currency for reporting purposes.**|
|DisplayName|**Credit Limit (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`creditlimit_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

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

### <a name="BKMK_IsPrivate"></a> IsPrivate

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`isprivate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_isprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MarketCap_Base"></a> MarketCap_Base

|Property|Value|
|---|---|
|Description|**Shows the market capitalization converted to the system's default base currency.**|
|DisplayName|**Market Capitalization (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`marketcap_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_MasterId"></a> MasterId

|Property|Value|
|---|---|
|Description|**Shows the master account that the account was merged with.**|
|DisplayName|**Master ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`masterid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

### <a name="BKMK_Merged"></a> Merged

|Property|Value|
|---|---|
|Description|**Shows whether the account has been merged with another account.**|
|DisplayName|**Merged**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`merged`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`account_merged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_ModifiedByExternalParty"></a> ModifiedByExternalParty

|Property|Value|
|---|---|
|Description|**Shows the external party who modified the record.**|
|DisplayName|**Modified By (External Party)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedbyexternalparty`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|externalparty|

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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OnHoldTime"></a> OnHoldTime

|Property|Value|
|---|---|
|Description|**Shows how long, in minutes, that the record was on hold.**|
|DisplayName|**On Hold Time (Minutes)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onholdtime`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Shows the business unit that the record owner belongs to.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier of the team who owns the account.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the account.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Revenue_Base"></a> Revenue_Base

|Property|Value|
|---|---|
|Description|**Shows the annual revenue converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.**|
|DisplayName|**Annual Revenue (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`revenue_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|---|---|
|Description|**Last SLA that was applied to this case. This field is for internal use only.**|
|DisplayName|**Last SLA applied**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slainvokedid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_TimeSpentByMeOnEmailAndMeetings"></a> TimeSpentByMeOnEmailAndMeetings

|Property|Value|
|---|---|
|Description|**Total time spent for emails (read and write) and meetings by me in relation to account record.**|
|DisplayName|**Time Spent by me**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timespentbymeonemailandmeetings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the account.**|
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

- [account_master_account](#BKMK_account_master_account-many-to-one)
- [account_parent_account](#BKMK_account_parent_account-many-to-one)
- [account_primary_contact](#BKMK_account_primary_contact)
- [business_unit_accounts](#BKMK_business_unit_accounts)
- [lk_accountbase_createdby](#BKMK_lk_accountbase_createdby)
- [lk_accountbase_createdonbehalfby](#BKMK_lk_accountbase_createdonbehalfby)
- [lk_accountbase_modifiedby](#BKMK_lk_accountbase_modifiedby)
- [lk_accountbase_modifiedonbehalfby](#BKMK_lk_accountbase_modifiedonbehalfby)
- [manualsla_account](#BKMK_manualsla_account)
- [msa_account_managingpartner](#BKMK_msa_account_managingpartner-many-to-one)
- [owner_accounts](#BKMK_owner_accounts)
- [processstage_account](#BKMK_processstage_account)
- [sla_account](#BKMK_sla_account)
- [system_user_accounts](#BKMK_system_user_accounts)
- [team_accounts](#BKMK_team_accounts)
- [transactioncurrency_account](#BKMK_transactioncurrency_account)
- [user_accounts](#BKMK_user_accounts)

### <a name="BKMK_account_master_account-many-to-one"></a> account_master_account

One-To-Many Relationship: [account account_master_account](#BKMK_account_master_account-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`masterid`|
|ReferencingEntityNavigationPropertyName|`masterid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_account_parent_account-many-to-one"></a> account_parent_account

One-To-Many Relationship: [account account_parent_account](#BKMK_account_parent_account-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`parentaccountid`|
|ReferencingEntityNavigationPropertyName|`parentaccountid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_account_primary_contact"></a> account_primary_contact

One-To-Many Relationship: [contact account_primary_contact](contact.md#BKMK_account_primary_contact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`primarycontactid`|
|ReferencingEntityNavigationPropertyName|`primarycontactid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_accounts"></a> business_unit_accounts

One-To-Many Relationship: [businessunit business_unit_accounts](businessunit.md#BKMK_business_unit_accounts)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_accountbase_createdby"></a> lk_accountbase_createdby

One-To-Many Relationship: [systemuser lk_accountbase_createdby](systemuser.md#BKMK_lk_accountbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_accountbase_createdonbehalfby"></a> lk_accountbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_accountbase_createdonbehalfby](systemuser.md#BKMK_lk_accountbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_accountbase_modifiedby"></a> lk_accountbase_modifiedby

One-To-Many Relationship: [systemuser lk_accountbase_modifiedby](systemuser.md#BKMK_lk_accountbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_accountbase_modifiedonbehalfby"></a> lk_accountbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_accountbase_modifiedonbehalfby](systemuser.md#BKMK_lk_accountbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_manualsla_account"></a> manualsla_account

One-To-Many Relationship: [sla manualsla_account](sla.md#BKMK_manualsla_account)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slaid`|
|ReferencingEntityNavigationPropertyName|`sla_account_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msa_account_managingpartner-many-to-one"></a> msa_account_managingpartner

One-To-Many Relationship: [account msa_account_managingpartner](#BKMK_msa_account_managingpartner-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`msa_managingpartnerid`|
|ReferencingEntityNavigationPropertyName|`msa_managingpartnerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_accounts"></a> owner_accounts

One-To-Many Relationship: [owner owner_accounts](owner.md#BKMK_owner_accounts)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_account"></a> processstage_account

One-To-Many Relationship: [processstage processstage_account](processstage.md#BKMK_processstage_account)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sla_account"></a> sla_account

One-To-Many Relationship: [sla sla_account](sla.md#BKMK_sla_account)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slainvokedid`|
|ReferencingEntityNavigationPropertyName|`slainvokedid_account_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_system_user_accounts"></a> system_user_accounts

One-To-Many Relationship: [systemuser system_user_accounts](systemuser.md#BKMK_system_user_accounts)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`preferredsystemuserid`|
|ReferencingEntityNavigationPropertyName|`preferredsystemuserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_accounts"></a> team_accounts

One-To-Many Relationship: [team team_accounts](team.md#BKMK_team_accounts)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_account"></a> transactioncurrency_account

One-To-Many Relationship: [transactioncurrency transactioncurrency_account](transactioncurrency.md#BKMK_transactioncurrency_account)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_accounts"></a> user_accounts

One-To-Many Relationship: [systemuser user_accounts](systemuser.md#BKMK_user_accounts)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [account_actioncard](#BKMK_account_actioncard)
- [account_activity_parties](#BKMK_account_activity_parties)
- [Account_ActivityPointers](#BKMK_Account_ActivityPointers)
- [account_adx_inviteredemptions](#BKMK_account_adx_inviteredemptions)
- [account_adx_portalcomments](#BKMK_account_adx_portalcomments)
- [Account_Annotation](#BKMK_Account_Annotation)
- [Account_Appointments](#BKMK_Account_Appointments)
- [Account_AsyncOperations](#BKMK_Account_AsyncOperations)
- [Account_BulkDeleteFailures](#BKMK_Account_BulkDeleteFailures)
- [account_chats](#BKMK_account_chats)
- [account_connections1](#BKMK_account_connections1)
- [account_connections2](#BKMK_account_connections2)
- [Account_CustomerAddress](#BKMK_Account_CustomerAddress)
- [Account_DuplicateBaseRecord](#BKMK_Account_DuplicateBaseRecord)
- [Account_DuplicateMatchingRecord](#BKMK_Account_DuplicateMatchingRecord)
- [Account_Email_EmailSender](#BKMK_Account_Email_EmailSender)
- [Account_Email_SendersAccount](#BKMK_Account_Email_SendersAccount)
- [Account_Emails](#BKMK_Account_Emails)
- [Account_Faxes](#BKMK_Account_Faxes)
- [Account_Letters](#BKMK_Account_Letters)
- [Account_MailboxTrackingFolder](#BKMK_Account_MailboxTrackingFolder)
- [account_master_account](#BKMK_account_master_account-one-to-many)
- [account_parent_account](#BKMK_account_parent_account-one-to-many)
- [Account_Phonecalls](#BKMK_Account_Phonecalls)
- [account_PostFollows](#BKMK_account_PostFollows)
- [account_PostRegardings](#BKMK_account_PostRegardings)
- [account_principalobjectattributeaccess](#BKMK_account_principalobjectattributeaccess)
- [Account_ProcessSessions](#BKMK_Account_ProcessSessions)
- [Account_RecurringAppointmentMasters](#BKMK_Account_RecurringAppointmentMasters)
- [Account_SharepointDocumentLocation](#BKMK_Account_SharepointDocumentLocation)
- [Account_SocialActivities](#BKMK_Account_SocialActivities)
- [Account_SyncErrors](#BKMK_Account_SyncErrors)
- [Account_Tasks](#BKMK_Account_Tasks)
- [adx_invitation_assigntoaccount](#BKMK_adx_invitation_assigntoaccount)
- [contact_customer_accounts](#BKMK_contact_customer_accounts)
- [msa_account_managingpartner](#BKMK_msa_account_managingpartner-one-to-many)
- [msa_contact_managingpartner](#BKMK_msa_contact_managingpartner)
- [slakpiinstance_account](#BKMK_slakpiinstance_account)
- [SocialActivity_PostAuthor_accounts](#BKMK_SocialActivity_PostAuthor_accounts)
- [SocialActivity_PostAuthorAccount_accounts](#BKMK_SocialActivity_PostAuthorAccount_accounts)
- [Socialprofile_customer_accounts](#BKMK_Socialprofile_customer_accounts)

### <a name="BKMK_account_actioncard"></a> account_actioncard

Many-To-One Relationship: [actioncard account_actioncard](actioncard.md#BKMK_account_actioncard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`account_actioncard`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_activity_parties"></a> account_activity_parties

Many-To-One Relationship: [activityparty account_activity_parties](activityparty.md#BKMK_account_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`partyid`|
|ReferencedEntityNavigationPropertyName|`account_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_ActivityPointers"></a> Account_ActivityPointers

Many-To-One Relationship: [activitypointer Account_ActivityPointers](activitypointer.md#BKMK_Account_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_ActivityPointers`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 20<br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_account_adx_inviteredemptions"></a> account_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption account_adx_inviteredemptions](adx_inviteredemption.md#BKMK_account_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`account_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_account_adx_portalcomments"></a> account_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment account_adx_portalcomments](adx_portalcomment.md#BKMK_account_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`account_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_Account_Annotation"></a> Account_Annotation

Many-To-One Relationship: [annotation Account_Annotation](annotation.md#BKMK_Account_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Account_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Appointments"></a> Account_Appointments

Many-To-One Relationship: [appointment Account_Appointments](appointment.md#BKMK_Account_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_AsyncOperations"></a> Account_AsyncOperations

Many-To-One Relationship: [asyncoperation Account_AsyncOperations](asyncoperation.md#BKMK_Account_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_BulkDeleteFailures"></a> Account_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Account_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Account_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_chats"></a> account_chats

Many-To-One Relationship: [chat account_chats](chat.md#BKMK_account_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`account_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_account_connections1"></a> account_connections1

Many-To-One Relationship: [connection account_connections1](connection.md#BKMK_account_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`account_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_connections2"></a> account_connections2

Many-To-One Relationship: [connection account_connections2](connection.md#BKMK_account_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`account_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_CustomerAddress"></a> Account_CustomerAddress

Many-To-One Relationship: [customeraddress Account_CustomerAddress](customeraddress.md#BKMK_Account_CustomerAddress)

|Property|Value|
|---|---|
|ReferencingEntity|`customeraddress`|
|ReferencingAttribute|`parentid`|
|ReferencedEntityNavigationPropertyName|`Account_CustomerAddress`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10<br />QueryApi: null<br />ViewId: `03315b35-4585-4447-a4d2-059cf79ca0fd`|

### <a name="BKMK_Account_DuplicateBaseRecord"></a> Account_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Account_DuplicateBaseRecord](duplicaterecord.md#BKMK_Account_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Account_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_DuplicateMatchingRecord"></a> Account_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Account_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Account_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Account_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Email_EmailSender"></a> Account_Email_EmailSender

Many-To-One Relationship: [email Account_Email_EmailSender](email.md#BKMK_Account_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`emailsender`|
|ReferencedEntityNavigationPropertyName|`Account_Email_EmailSender`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Email_SendersAccount"></a> Account_Email_SendersAccount

Many-To-One Relationship: [email Account_Email_SendersAccount](email.md#BKMK_Account_Email_SendersAccount)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`sendersaccount`|
|ReferencedEntityNavigationPropertyName|`Account_Email_SendersAccount`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Emails"></a> Account_Emails

Many-To-One Relationship: [email Account_Emails](email.md#BKMK_Account_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Faxes"></a> Account_Faxes

Many-To-One Relationship: [fax Account_Faxes](fax.md#BKMK_Account_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Letters"></a> Account_Letters

Many-To-One Relationship: [letter Account_Letters](letter.md#BKMK_Account_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_MailboxTrackingFolder"></a> Account_MailboxTrackingFolder

Many-To-One Relationship: [mailboxtrackingfolder Account_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Account_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_MailboxTrackingFolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_master_account-one-to-many"></a> account_master_account

Many-To-One Relationship: [account account_master_account](#BKMK_account_master_account-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`masterid`|
|ReferencedEntityNavigationPropertyName|`account_master_account`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_parent_account-one-to-many"></a> account_parent_account

Many-To-One Relationship: [account account_parent_account](#BKMK_account_parent_account-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`parentaccountid`|
|ReferencedEntityNavigationPropertyName|`account_parent_account`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 40<br />QueryApi: `CRMAccount.RetrieveSubAccounts`<br />ViewId: `00000000-0000-0000-00aa-000010001200`|

### <a name="BKMK_Account_Phonecalls"></a> Account_Phonecalls

Many-To-One Relationship: [phonecall Account_Phonecalls](phonecall.md#BKMK_Account_Phonecalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_Phonecalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_PostFollows"></a> account_PostFollows

Many-To-One Relationship: [postfollow account_PostFollows](postfollow.md#BKMK_account_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`account_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_PostRegardings"></a> account_PostRegardings

Many-To-One Relationship: [postregarding account_PostRegardings](postregarding.md#BKMK_account_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`account_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_account_principalobjectattributeaccess"></a> account_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess account_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_account_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`account_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_ProcessSessions"></a> Account_ProcessSessions

Many-To-One Relationship: [processsession Account_ProcessSessions](processsession.md#BKMK_Account_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_RecurringAppointmentMasters"></a> Account_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster Account_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_Account_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_SharepointDocumentLocation"></a> Account_SharepointDocumentLocation

Many-To-One Relationship: [sharepointdocumentlocation Account_SharepointDocumentLocation](sharepointdocumentlocation.md#BKMK_Account_SharepointDocumentLocation)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_SharepointDocumentLocation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_SocialActivities"></a> Account_SocialActivities

Many-To-One Relationship: [socialactivity Account_SocialActivities](socialactivity.md#BKMK_Account_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_SyncErrors"></a> Account_SyncErrors

Many-To-One Relationship: [syncerror Account_SyncErrors](syncerror.md#BKMK_Account_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Account_Tasks"></a> Account_Tasks

Many-To-One Relationship: [task Account_Tasks](task.md#BKMK_Account_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Account_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_assigntoaccount"></a> adx_invitation_assigntoaccount

Many-To-One Relationship: [adx_invitation adx_invitation_assigntoaccount](adx_invitation.md#BKMK_adx_invitation_assigntoaccount)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`adx_assigntoaccount`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_assigntoaccount`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_customer_accounts"></a> contact_customer_accounts

Many-To-One Relationship: [contact contact_customer_accounts](contact.md#BKMK_contact_customer_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`parentcustomerid`|
|ReferencedEntityNavigationPropertyName|`contact_customer_accounts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 50<br />QueryApi: `CRMAccount.RetrieveSubContacts`<br />ViewId: `00000000-0000-0000-00aa-000010001210`|

### <a name="BKMK_msa_account_managingpartner-one-to-many"></a> msa_account_managingpartner

Many-To-One Relationship: [account msa_account_managingpartner](#BKMK_msa_account_managingpartner-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`msa_managingpartnerid`|
|ReferencedEntityNavigationPropertyName|`msa_account_managingpartner`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Managed Accounts<br />MenuId: null<br />Order: 100400<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msa_contact_managingpartner"></a> msa_contact_managingpartner

Many-To-One Relationship: [contact msa_contact_managingpartner](contact.md#BKMK_msa_contact_managingpartner)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`msa_managingpartnerid`|
|ReferencedEntityNavigationPropertyName|`msa_contact_managingpartner`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Managed Contacts<br />MenuId: null<br />Order: 100500<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slakpiinstance_account"></a> slakpiinstance_account

Many-To-One Relationship: [slakpiinstance slakpiinstance_account](slakpiinstance.md#BKMK_slakpiinstance_account)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`slakpiinstance_account`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SocialActivity_PostAuthor_accounts"></a> SocialActivity_PostAuthor_accounts

Many-To-One Relationship: [socialactivity SocialActivity_PostAuthor_accounts](socialactivity.md#BKMK_SocialActivity_PostAuthor_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`postauthor`|
|ReferencedEntityNavigationPropertyName|`SocialActivity_PostAuthor_accounts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SocialActivity_PostAuthorAccount_accounts"></a> SocialActivity_PostAuthorAccount_accounts

Many-To-One Relationship: [socialactivity SocialActivity_PostAuthorAccount_accounts](socialactivity.md#BKMK_SocialActivity_PostAuthorAccount_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`postauthoraccount`|
|ReferencedEntityNavigationPropertyName|`SocialActivity_PostAuthorAccount_accounts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Socialprofile_customer_accounts"></a> Socialprofile_customer_accounts

Many-To-One Relationship: [socialprofile Socialprofile_customer_accounts](socialprofile.md#BKMK_Socialprofile_customer_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`socialprofile`|
|ReferencingAttribute|`customerid`|
|ReferencedEntityNavigationPropertyName|`Socialprofile_customer_accounts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 50<br />QueryApi: null<br />ViewId: `ff0f8b49-e2cd-45f1-b878-cbd99aa4ac56`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_powerpagecomponent_mspp_webrole_account"></a> powerpagecomponent_mspp_webrole_account

See [powerpagecomponent powerpagecomponent_mspp_webrole_account Many-To-Many Relationship](powerpagecomponent.md#BKMK_powerpagecomponent_mspp_webrole_account)

|Property|Value|
|---|---|
|IntersectEntityName|`powerpagecomponent_mspp_webrole_account`|
|IsCustomizable|True|
|SchemaName|`powerpagecomponent_mspp_webrole_account`|
|IntersectAttribute|`accountid`|
|NavigationPropertyName|`powerpagecomponent_mspp_webrole_account`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.account?displayProperty=fullName>
