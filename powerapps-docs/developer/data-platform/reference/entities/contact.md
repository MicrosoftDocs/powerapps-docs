---
title: "Contact table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Contact table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Contact table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Person with whom a business unit has a relationship, such as customer, supplier, and colleague.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/contacts(*contactid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/contacts<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/contacts(*contactid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|Merge|<xref href="Microsoft.Dynamics.CRM.Merge?text=Merge Action" />|<xref:Microsoft.Crm.Sdk.Messages.MergeRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/contacts(*contactid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/contacts<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|Rollup|<xref href="Microsoft.Dynamics.CRM.Rollup?text=Rollup Function" />|<xref:Microsoft.Crm.Sdk.Messages.RollupRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/contacts(*contactid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/contacts(*contactid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Contacts|
|DisplayCollectionName|Contacts|
|DisplayName|Contact|
|EntitySetName|contacts|
|IsBPFEntity|False|
|LogicalCollectionName|contacts|
|LogicalName|contact|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|contactid|
|PrimaryNameAttribute|fullname|
|SchemaName|Contact|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccountRoleCode](#BKMK_AccountRoleCode)
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
- [Address3_AddressId](#BKMK_Address3_AddressId)
- [Address3_AddressTypeCode](#BKMK_Address3_AddressTypeCode)
- [Address3_City](#BKMK_Address3_City)
- [Address3_Country](#BKMK_Address3_Country)
- [Address3_County](#BKMK_Address3_County)
- [Address3_Fax](#BKMK_Address3_Fax)
- [Address3_FreightTermsCode](#BKMK_Address3_FreightTermsCode)
- [Address3_Latitude](#BKMK_Address3_Latitude)
- [Address3_Line1](#BKMK_Address3_Line1)
- [Address3_Line2](#BKMK_Address3_Line2)
- [Address3_Line3](#BKMK_Address3_Line3)
- [Address3_Longitude](#BKMK_Address3_Longitude)
- [Address3_Name](#BKMK_Address3_Name)
- [Address3_PostalCode](#BKMK_Address3_PostalCode)
- [Address3_PostOfficeBox](#BKMK_Address3_PostOfficeBox)
- [Address3_PrimaryContactName](#BKMK_Address3_PrimaryContactName)
- [Address3_ShippingMethodCode](#BKMK_Address3_ShippingMethodCode)
- [Address3_StateOrProvince](#BKMK_Address3_StateOrProvince)
- [Address3_Telephone1](#BKMK_Address3_Telephone1)
- [Address3_Telephone2](#BKMK_Address3_Telephone2)
- [Address3_Telephone3](#BKMK_Address3_Telephone3)
- [Address3_UPSZone](#BKMK_Address3_UPSZone)
- [Address3_UTCOffset](#BKMK_Address3_UTCOffset)
- [Anniversary](#BKMK_Anniversary)
- [AnnualIncome](#BKMK_AnnualIncome)
- [AssistantName](#BKMK_AssistantName)
- [AssistantPhone](#BKMK_AssistantPhone)
- [BirthDate](#BKMK_BirthDate)
- [Business2](#BKMK_Business2)
- [Callback](#BKMK_Callback)
- [ChildrensNames](#BKMK_ChildrensNames)
- [Company](#BKMK_Company)
- [ContactId](#BKMK_ContactId)
- [CreditLimit](#BKMK_CreditLimit)
- [CreditOnHold](#BKMK_CreditOnHold)
- [CustomerSizeCode](#BKMK_CustomerSizeCode)
- [CustomerTypeCode](#BKMK_CustomerTypeCode)
- [Department](#BKMK_Department)
- [Description](#BKMK_Description)
- [DoNotBulkEMail](#BKMK_DoNotBulkEMail)
- [DoNotBulkPostalMail](#BKMK_DoNotBulkPostalMail)
- [DoNotEMail](#BKMK_DoNotEMail)
- [DoNotFax](#BKMK_DoNotFax)
- [DoNotPhone](#BKMK_DoNotPhone)
- [DoNotPostalMail](#BKMK_DoNotPostalMail)
- [DoNotSendMM](#BKMK_DoNotSendMM)
- [EducationCode](#BKMK_EducationCode)
- [EMailAddress1](#BKMK_EMailAddress1)
- [EMailAddress2](#BKMK_EMailAddress2)
- [EMailAddress3](#BKMK_EMailAddress3)
- [EmployeeId](#BKMK_EmployeeId)
- [EntityImage](#BKMK_EntityImage)
- [ExternalUserIdentifier](#BKMK_ExternalUserIdentifier)
- [FamilyStatusCode](#BKMK_FamilyStatusCode)
- [Fax](#BKMK_Fax)
- [FirstName](#BKMK_FirstName)
- [FollowEmail](#BKMK_FollowEmail)
- [FtpSiteUrl](#BKMK_FtpSiteUrl)
- [GenderCode](#BKMK_GenderCode)
- [GovernmentId](#BKMK_GovernmentId)
- [HasChildrenCode](#BKMK_HasChildrenCode)
- [Home2](#BKMK_Home2)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsBackofficeCustomer](#BKMK_IsBackofficeCustomer)
- [JobTitle](#BKMK_JobTitle)
- [LastName](#BKMK_LastName)
- [LastOnHoldTime](#BKMK_LastOnHoldTime)
- [LastUsedInCampaign](#BKMK_LastUsedInCampaign)
- [LeadSourceCode](#BKMK_LeadSourceCode)
- [ManagerName](#BKMK_ManagerName)
- [ManagerPhone](#BKMK_ManagerPhone)
- [MarketingOnly](#BKMK_MarketingOnly)
- [MiddleName](#BKMK_MiddleName)
- [MobilePhone](#BKMK_MobilePhone)
- [NickName](#BKMK_NickName)
- [NumberOfChildren](#BKMK_NumberOfChildren)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Pager](#BKMK_Pager)
- [ParentCustomerId](#BKMK_ParentCustomerId)
- [ParentCustomerIdType](#BKMK_ParentCustomerIdType)
- [ParticipatesInWorkflow](#BKMK_ParticipatesInWorkflow)
- [PaymentTermsCode](#BKMK_PaymentTermsCode)
- [PreferredAppointmentDayCode](#BKMK_PreferredAppointmentDayCode)
- [PreferredAppointmentTimeCode](#BKMK_PreferredAppointmentTimeCode)
- [PreferredContactMethodCode](#BKMK_PreferredContactMethodCode)
- [PreferredSystemUserId](#BKMK_PreferredSystemUserId)
- [ProcessId](#BKMK_ProcessId)
- [Salutation](#BKMK_Salutation)
- [ShippingMethodCode](#BKMK_ShippingMethodCode)
- [SLAId](#BKMK_SLAId)
- [SpousesName](#BKMK_SpousesName)
- [StageId](#BKMK_StageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SubscriptionId](#BKMK_SubscriptionId)
- [Suffix](#BKMK_Suffix)
- [Telephone1](#BKMK_Telephone1)
- [Telephone2](#BKMK_Telephone2)
- [Telephone3](#BKMK_Telephone3)
- [TerritoryCode](#BKMK_TerritoryCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WebSiteUrl](#BKMK_WebSiteUrl)
- [YomiFirstName](#BKMK_YomiFirstName)
- [YomiLastName](#BKMK_YomiLastName)
- [YomiMiddleName](#BKMK_YomiMiddleName)


### <a name="BKMK_AccountRoleCode"></a> AccountRoleCode

|Property|Value|
|--------|-----|
|Description|Select the contact's role within the company or sales process, such as decision maker, employee, or influencer.|
|DisplayName|Role|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|accountrolecode|
|RequiredLevel|None|
|Type|Picklist|

#### AccountRoleCode Choices/Options

|Value|Label|
|-----|-----|
|1|Decision Maker|
|2|Employee|
|3|Influencer|



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
|Description|Select the primary address type.|
|DisplayName|Address 1: Address Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_addresstypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Address1_AddressTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Bill To|
|2|Ship To|
|3|Primary|
|4|Other|



### <a name="BKMK_Address1_City"></a> Address1_City

|Property|Value|
|--------|-----|
|Description|Type the city for the primary address.|
|DisplayName|Address 1: City|
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
|Description|Type the country or region for the primary address.|
|DisplayName|Address 1: Country/Region|
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
|Description|Type the county for the primary address.|
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
|Description|Type the fax number associated with the primary address.|
|DisplayName|Address 1: Fax|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_fax|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_FreightTermsCode"></a> Address1_FreightTermsCode

|Property|Value|
|--------|-----|
|Description|Select the freight terms for the primary address to make sure shipping orders are processed correctly.|
|DisplayName|Address 1: Freight Terms|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_freighttermscode|
|RequiredLevel|None|
|Type|Picklist|

#### Address1_FreightTermsCode Choices/Options

|Value|Label|
|-----|-----|
|1|FOB|
|2|No Charge|



### <a name="BKMK_Address1_Latitude"></a> Address1_Latitude

|Property|Value|
|--------|-----|
|Description|Type the latitude value for the primary address for use in mapping and other applications.|
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
|Description|Type the first line of the primary address.|
|DisplayName|Address 1: Street 1|
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
|Description|Type the second line of the primary address.|
|DisplayName|Address 1: Street 2|
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
|Description|Type the third line of the primary address.|
|DisplayName|Address 1: Street 3|
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
|Description|Type the longitude value for the primary address for use in mapping and other applications.|
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
|Description|Type a descriptive name for the primary address, such as Corporate Headquarters.|
|DisplayName|Address 1: Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_PostalCode"></a> Address1_PostalCode

|Property|Value|
|--------|-----|
|Description|Type the ZIP Code or postal code for the primary address.|
|DisplayName|Address 1: ZIP/Postal Code|
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
|Description|Type the post office box number of the primary address.|
|DisplayName|Address 1: Post Office Box|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_postofficebox|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_PrimaryContactName"></a> Address1_PrimaryContactName

|Property|Value|
|--------|-----|
|Description|Type the name of the main contact at the account's primary address.|
|DisplayName|Address 1: Primary Contact Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_primarycontactname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Select a shipping method for deliveries sent to this address.|
|DisplayName|Address 1: Shipping Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_shippingmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### Address1_ShippingMethodCode Choices/Options

|Value|Label|
|-----|-----|
|1|Airborne|
|2|DHL|
|3|FedEx|
|4|UPS|
|5|Postal Mail|
|6|Full Load|
|7|Will Call|



### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

|Property|Value|
|--------|-----|
|Description|Type the state or province of the primary address.|
|DisplayName|Address 1: State/Province|
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
|Description|Type the main phone number associated with the primary address.|
|DisplayName|Address 1: Phone|
|FormatName|Phone|
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
|Description|Type a second phone number associated with the primary address.|
|DisplayName|Address 1: Telephone 2|
|FormatName|Phone|
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
|Description|Type a third phone number associated with the primary address.|
|DisplayName|Address 1: Telephone 3|
|FormatName|Phone|
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
|Description|Type the UPS zone of the primary address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.|
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
|Description|Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.|
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
|Description|Select the secondary address type.|
|DisplayName|Address 2: Address Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_addresstypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Address2_AddressTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Address2_City"></a> Address2_City

|Property|Value|
|--------|-----|
|Description|Type the city for the secondary address.|
|DisplayName|Address 2: City|
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
|Description|Type the country or region for the secondary address.|
|DisplayName|Address 2: Country/Region|
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
|Description|Type the county for the secondary address.|
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
|Description|Type the fax number associated with the secondary address.|
|DisplayName|Address 2: Fax|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_fax|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_FreightTermsCode"></a> Address2_FreightTermsCode

|Property|Value|
|--------|-----|
|Description|Select the freight terms for the secondary address to make sure shipping orders are processed correctly.|
|DisplayName|Address 2: Freight Terms|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_freighttermscode|
|RequiredLevel|None|
|Type|Picklist|

#### Address2_FreightTermsCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Address2_Latitude"></a> Address2_Latitude

|Property|Value|
|--------|-----|
|Description|Type the latitude value for the secondary address for use in mapping and other applications.|
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
|Description|Type the first line of the secondary address.|
|DisplayName|Address 2: Street 1|
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
|Description|Type the second line of the secondary address.|
|DisplayName|Address 2: Street 2|
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
|Description|Type the third line of the secondary address.|
|DisplayName|Address 2: Street 3|
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
|Description|Type the longitude value for the secondary address for use in mapping and other applications.|
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
|Description|Type a descriptive name for the secondary address, such as Corporate Headquarters.|
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
|Description|Type the ZIP Code or postal code for the secondary address.|
|DisplayName|Address 2: ZIP/Postal Code|
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
|Description|Type the post office box number of the secondary address.|
|DisplayName|Address 2: Post Office Box|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_postofficebox|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_PrimaryContactName"></a> Address2_PrimaryContactName

|Property|Value|
|--------|-----|
|Description|Type the name of the main contact at the account's secondary address.|
|DisplayName|Address 2: Primary Contact Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_primarycontactname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Select a shipping method for deliveries sent to this address.|
|DisplayName|Address 2: Shipping Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_shippingmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### Address2_ShippingMethodCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

|Property|Value|
|--------|-----|
|Description|Type the state or province of the secondary address.|
|DisplayName|Address 2: State/Province|
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
|Description|Type the main phone number associated with the secondary address.|
|DisplayName|Address 2: Telephone 1|
|FormatName|Phone|
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
|Description|Type a second phone number associated with the secondary address.|
|DisplayName|Address 2: Telephone 2|
|FormatName|Phone|
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
|Description|Type a third phone number associated with the secondary address.|
|DisplayName|Address 2: Telephone 3|
|FormatName|Phone|
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
|Description|Type the UPS zone of the secondary address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.|
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
|Description|Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.|
|DisplayName|Address 2: UTC Offset|
|Format|TimeZone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_utcoffset|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Address3_AddressId"></a> Address3_AddressId

|Property|Value|
|--------|-----|
|Description|Unique identifier for address 3.|
|DisplayName|Address 3: ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|address3_addressid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Address3_AddressTypeCode"></a> Address3_AddressTypeCode

|Property|Value|
|--------|-----|
|Description|Select the third address type.|
|DisplayName|Address 3: Address Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_addresstypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Address3_AddressTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Address3_City"></a> Address3_City

|Property|Value|
|--------|-----|
|Description|Type the city for the 3rd address.|
|DisplayName|Address 3: City|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_city|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Country"></a> Address3_Country

|Property|Value|
|--------|-----|
|Description|the country or region for the 3rd address.|
|DisplayName|Address3: Country/Region|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_country|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_County"></a> Address3_County

|Property|Value|
|--------|-----|
|Description|Type the county for the third address.|
|DisplayName|Address 3: County|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_county|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Fax"></a> Address3_Fax

|Property|Value|
|--------|-----|
|Description|Type the fax number associated with the third address.|
|DisplayName|Address 3: Fax|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_fax|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_FreightTermsCode"></a> Address3_FreightTermsCode

|Property|Value|
|--------|-----|
|Description|Select the freight terms for the third address to make sure shipping orders are processed correctly.|
|DisplayName|Address 3: Freight Terms|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_freighttermscode|
|RequiredLevel|None|
|Type|Picklist|

#### Address3_FreightTermsCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Address3_Latitude"></a> Address3_Latitude

|Property|Value|
|--------|-----|
|Description|Type the latitude value for the third address for use in mapping and other applications.|
|DisplayName|Address 3: Latitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_latitude|
|MaxValue|90|
|MinValue|-90|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Address3_Line1"></a> Address3_Line1

|Property|Value|
|--------|-----|
|Description|the first line of the 3rd address.|
|DisplayName|Address3: Street 1|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_line1|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Line2"></a> Address3_Line2

|Property|Value|
|--------|-----|
|Description|the second line of the 3rd address.|
|DisplayName|Address3: Street 2|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_line2|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Line3"></a> Address3_Line3

|Property|Value|
|--------|-----|
|Description|the third line of the 3rd address.|
|DisplayName|Address3: Street 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_line3|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Longitude"></a> Address3_Longitude

|Property|Value|
|--------|-----|
|Description|Type the longitude value for the third address for use in mapping and other applications.|
|DisplayName|Address 3: Longitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_longitude|
|MaxValue|180|
|MinValue|-180|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_Address3_Name"></a> Address3_Name

|Property|Value|
|--------|-----|
|Description|Type a descriptive name for the third address, such as Corporate Headquarters.|
|DisplayName|Address 3: Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_PostalCode"></a> Address3_PostalCode

|Property|Value|
|--------|-----|
|Description|the ZIP Code or postal code for the 3rd address.|
|DisplayName|Address3: ZIP/Postal Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_postalcode|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_PostOfficeBox"></a> Address3_PostOfficeBox

|Property|Value|
|--------|-----|
|Description|the post office box number of the 3rd address.|
|DisplayName|Address 3: Post Office Box|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_postofficebox|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_PrimaryContactName"></a> Address3_PrimaryContactName

|Property|Value|
|--------|-----|
|Description|Type the name of the main contact at the account's third address.|
|DisplayName|Address 3: Primary Contact Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_primarycontactname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_ShippingMethodCode"></a> Address3_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Select a shipping method for deliveries sent to this address.|
|DisplayName|Address 3: Shipping Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_shippingmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### Address3_ShippingMethodCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Address3_StateOrProvince"></a> Address3_StateOrProvince

|Property|Value|
|--------|-----|
|Description|the state or province of the third address.|
|DisplayName|Address3: State/Province|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_stateorprovince|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Telephone1"></a> Address3_Telephone1

|Property|Value|
|--------|-----|
|Description|Type the main phone number associated with the third address.|
|DisplayName|Address 3: Telephone1|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_telephone1|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Telephone2"></a> Address3_Telephone2

|Property|Value|
|--------|-----|
|Description|Type a second phone number associated with the third address.|
|DisplayName|Address 3: Telephone2|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_telephone2|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_Telephone3"></a> Address3_Telephone3

|Property|Value|
|--------|-----|
|Description|Type a third phone number associated with the primary address.|
|DisplayName|Address 3: Telephone3|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_telephone3|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_UPSZone"></a> Address3_UPSZone

|Property|Value|
|--------|-----|
|Description|Type the UPS zone of the third address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.|
|DisplayName|Address 3: UPS Zone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_upszone|
|MaxLength|4|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address3_UTCOffset"></a> Address3_UTCOffset

|Property|Value|
|--------|-----|
|Description|Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.|
|DisplayName|Address 3: UTC Offset|
|Format|TimeZone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_utcoffset|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Anniversary"></a> Anniversary

|Property|Value|
|--------|-----|
|DateTimeBehavior|DateOnly|
|Description|Enter the date of the contact's wedding or service anniversary for use in customer gift programs or other communications.|
|DisplayName|Anniversary|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|anniversary|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_AnnualIncome"></a> AnnualIncome

|Property|Value|
|--------|-----|
|Description|Type the contact's annual income for use in profiling and financial analysis.|
|DisplayName|Annual Income|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|annualincome|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_AssistantName"></a> AssistantName

|Property|Value|
|--------|-----|
|Description|Type the name of the contact's assistant.|
|DisplayName|Assistant|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|assistantname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AssistantPhone"></a> AssistantPhone

|Property|Value|
|--------|-----|
|Description|Type the phone number for the contact's assistant.|
|DisplayName|Assistant Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|assistantphone|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BirthDate"></a> BirthDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|DateOnly|
|Description|Enter the contact's birthday for use in customer gift programs or other communications.|
|DisplayName|Birthday|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|birthdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Business2"></a> Business2

|Property|Value|
|--------|-----|
|Description|Type a second business phone number for this contact.|
|DisplayName|Business Phone 2|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|business2|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Callback"></a> Callback

|Property|Value|
|--------|-----|
|Description|Type a callback phone number for this contact.|
|DisplayName|Callback Number|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|callback|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ChildrensNames"></a> ChildrensNames

|Property|Value|
|--------|-----|
|Description|Type the names of the contact's children for reference in communications and client programs.|
|DisplayName|Children's Names|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|childrensnames|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Company"></a> Company

|Property|Value|
|--------|-----|
|Description|Type the company phone of the contact.|
|DisplayName|Company Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|company|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ContactId"></a> ContactId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the contact.|
|DisplayName|Contact|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|contactid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CreditLimit"></a> CreditLimit

|Property|Value|
|--------|-----|
|Description|Type the credit limit of the contact for reference when you address invoice and accounting issues with the customer.|
|DisplayName|Credit Limit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|creditlimit|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_CreditOnHold"></a> CreditOnHold

|Property|Value|
|--------|-----|
|Description|Select whether the contact is on a credit hold, for reference when addressing invoice and accounting issues.|
|DisplayName|Credit Hold|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|creditonhold|
|RequiredLevel|None|
|Type|Boolean|

#### CreditOnHold Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_CustomerSizeCode"></a> CustomerSizeCode

|Property|Value|
|--------|-----|
|Description|Select the size of the contact's company for segmentation and reporting purposes.|
|DisplayName|Customer Size|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customersizecode|
|RequiredLevel|None|
|Type|Picklist|

#### CustomerSizeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_CustomerTypeCode"></a> CustomerTypeCode

|Property|Value|
|--------|-----|
|Description|Select the category that best describes the relationship between the contact and your organization.|
|DisplayName|Relationship Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customertypecode|
|RequiredLevel|None|
|Type|Picklist|

#### CustomerTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Department"></a> Department

|Property|Value|
|--------|-----|
|Description|Type the department or business unit where the contact works in the parent company or business.|
|DisplayName|Department|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|department|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information to describe the contact, such as an excerpt from the company's website.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DoNotBulkEMail"></a> DoNotBulkEMail

|Property|Value|
|--------|-----|
|Description|Select whether the contact accepts bulk email sent through marketing campaigns or quick campaigns. If Do Not Allow is selected, the contact can be added to marketing lists, but will be excluded from the email.|
|DisplayName|Do not allow Bulk Emails|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotbulkemail|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotBulkEMail Choices/Options

|Value|Label|
|-----|-----|
|1|Do Not Allow|
|0|Allow|

**DefaultValue**: False



### <a name="BKMK_DoNotBulkPostalMail"></a> DoNotBulkPostalMail

|Property|Value|
|--------|-----|
|Description|Select whether the contact accepts bulk postal mail sent through marketing campaigns or quick campaigns. If Do Not Allow is selected, the contact can be added to marketing lists, but will be excluded from the letters.|
|DisplayName|Do not allow Bulk Mails|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotbulkpostalmail|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotBulkPostalMail Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_DoNotEMail"></a> DoNotEMail

|Property|Value|
|--------|-----|
|Description|Select whether the contact allows direct email sent from Microsoft Dynamics 365. If Do Not Allow is selected, Microsoft Dynamics 365 will not send the email.|
|DisplayName|Do not allow Emails|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotemail|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotEMail Choices/Options

|Value|Label|
|-----|-----|
|1|Do Not Allow|
|0|Allow|

**DefaultValue**: False



### <a name="BKMK_DoNotFax"></a> DoNotFax

|Property|Value|
|--------|-----|
|Description|Select whether the contact allows faxes. If Do Not Allow is selected, the contact will be excluded from any fax activities distributed in marketing campaigns.|
|DisplayName|Do not allow Faxes|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotfax|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotFax Choices/Options

|Value|Label|
|-----|-----|
|1|Do Not Allow|
|0|Allow|

**DefaultValue**: False



### <a name="BKMK_DoNotPhone"></a> DoNotPhone

|Property|Value|
|--------|-----|
|Description|Select whether the contact accepts phone calls. If Do Not Allow is selected, the contact will be excluded from any phone call activities distributed in marketing campaigns.|
|DisplayName|Do not allow Phone Calls|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotphone|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotPhone Choices/Options

|Value|Label|
|-----|-----|
|1|Do Not Allow|
|0|Allow|

**DefaultValue**: False



### <a name="BKMK_DoNotPostalMail"></a> DoNotPostalMail

|Property|Value|
|--------|-----|
|Description|Select whether the contact allows direct mail. If Do Not Allow is selected, the contact will be excluded from letter activities distributed in marketing campaigns.|
|DisplayName|Do not allow Mails|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotpostalmail|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotPostalMail Choices/Options

|Value|Label|
|-----|-----|
|1|Do Not Allow|
|0|Allow|

**DefaultValue**: False



### <a name="BKMK_DoNotSendMM"></a> DoNotSendMM

|Property|Value|
|--------|-----|
|Description|Select whether the contact accepts marketing materials, such as brochures or catalogs. Contacts that opt out can be excluded from marketing initiatives.|
|DisplayName|Send Marketing Materials|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|donotsendmm|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotSendMM Choices/Options

|Value|Label|
|-----|-----|
|1|Do Not Send|
|0|Send|

**DefaultValue**: False



### <a name="BKMK_EducationCode"></a> EducationCode

|Property|Value|
|--------|-----|
|Description|Select the contact's highest level of education for use in segmentation and analysis.|
|DisplayName|Education|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|educationcode|
|RequiredLevel|None|
|Type|Picklist|

#### EducationCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_EMailAddress1"></a> EMailAddress1

|Property|Value|
|--------|-----|
|Description|Type the primary email address for the contact.|
|DisplayName|Email|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailaddress1|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EMailAddress2"></a> EMailAddress2

|Property|Value|
|--------|-----|
|Description|Type the secondary email address for the contact.|
|DisplayName|Email Address 2|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailaddress2|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EMailAddress3"></a> EMailAddress3

|Property|Value|
|--------|-----|
|Description|Type an alternate email address for the contact.|
|DisplayName|Email Address 3|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailaddress3|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmployeeId"></a> EmployeeId

|Property|Value|
|--------|-----|
|Description|Type the employee ID or number for the contact for reference in orders, service cases, or other communications with the contact's organization.|
|DisplayName|Employee|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|employeeid|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|--------|-----|
|Description|Shows the default image for the record.|
|DisplayName|Entity Image|
|IsPrimaryImage|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_ExternalUserIdentifier"></a> ExternalUserIdentifier

|Property|Value|
|--------|-----|
|Description|Identifier for an external user.|
|DisplayName|External User Identifier|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|externaluseridentifier|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FamilyStatusCode"></a> FamilyStatusCode

|Property|Value|
|--------|-----|
|Description|Select the marital status of the contact for reference in follow-up phone calls and other communications.|
|DisplayName|Marital Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|familystatuscode|
|RequiredLevel|None|
|Type|Picklist|

#### FamilyStatusCode Choices/Options

|Value|Label|
|-----|-----|
|1|Single|
|2|Married|
|3|Divorced|
|4|Widowed|



### <a name="BKMK_Fax"></a> Fax

|Property|Value|
|--------|-----|
|Description|Type the fax number for the contact.|
|DisplayName|Fax|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fax|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FirstName"></a> FirstName

|Property|Value|
|--------|-----|
|Description|Type the contact's first name to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.|
|DisplayName|First Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|firstname|
|MaxLength|50|
|RequiredLevel|Recommended|
|Type|String|


### <a name="BKMK_FollowEmail"></a> FollowEmail

|Property|Value|
|--------|-----|
|Description|Information about whether to allow following email activity like opens, attachment views and link clicks for emails sent to the contact.|
|DisplayName|Follow Email Activity|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|followemail|
|RequiredLevel|None|
|Type|Boolean|

#### FollowEmail Choices/Options

|Value|Label|
|-----|-----|
|1|Allow|
|0|Do Not Allow|

**DefaultValue**: True



### <a name="BKMK_FtpSiteUrl"></a> FtpSiteUrl

|Property|Value|
|--------|-----|
|Description|Type the URL for the contact's FTP site to enable users to access data and share documents.|
|DisplayName|FTP Site|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ftpsiteurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_GenderCode"></a> GenderCode

|Property|Value|
|--------|-----|
|Description|Select the contact's gender to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.|
|DisplayName|Gender|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|gendercode|
|RequiredLevel|None|
|Type|Picklist|

#### GenderCode Choices/Options

|Value|Label|
|-----|-----|
|1|Male|
|2|Female|



### <a name="BKMK_GovernmentId"></a> GovernmentId

|Property|Value|
|--------|-----|
|Description|Type the passport number or other government ID for the contact for use in documents or reports.|
|DisplayName|Government|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|governmentid|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_HasChildrenCode"></a> HasChildrenCode

|Property|Value|
|--------|-----|
|Description|Select whether the contact has any children for reference in follow-up phone calls and other communications.|
|DisplayName|Has Children|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|haschildrencode|
|RequiredLevel|None|
|Type|Picklist|

#### HasChildrenCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_Home2"></a> Home2

|Property|Value|
|--------|-----|
|Description|Type a second home phone number for this contact.|
|DisplayName|Home Phone 2|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|home2|
|MaxLength|50|
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


### <a name="BKMK_IsBackofficeCustomer"></a> IsBackofficeCustomer

|Property|Value|
|--------|-----|
|Description|Select whether the contact exists in a separate accounting or other system, such as Microsoft Dynamics GP or another ERP database, for use in integration processes.|
|DisplayName|Back Office Customer|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isbackofficecustomer|
|RequiredLevel|None|
|Type|Boolean|

#### IsBackofficeCustomer Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_JobTitle"></a> JobTitle

|Property|Value|
|--------|-----|
|Description|Type the job title of the contact to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.|
|DisplayName|Job Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|jobtitle|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastName"></a> LastName

|Property|Value|
|--------|-----|
|Description|Type the contact's last name to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.|
|DisplayName|Last Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastname|
|MaxLength|50|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Contains the date and time stamp of the last on hold time.|
|DisplayName|Last On Hold Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastonholdtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastUsedInCampaign"></a> LastUsedInCampaign

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date when the contact was last included in a marketing campaign or quick campaign.|
|DisplayName|Last Date Included in Campaign|
|Format|DateOnly|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastusedincampaign|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LeadSourceCode"></a> LeadSourceCode

|Property|Value|
|--------|-----|
|Description|Select the primary marketing source that directed the contact to your organization.|
|DisplayName|Lead Source|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|leadsourcecode|
|RequiredLevel|None|
|Type|Picklist|

#### LeadSourceCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_ManagerName"></a> ManagerName

|Property|Value|
|--------|-----|
|Description|Type the name of the contact's manager for use in escalating issues or other follow-up communications with the contact.|
|DisplayName|Manager|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|managername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ManagerPhone"></a> ManagerPhone

|Property|Value|
|--------|-----|
|Description|Type the phone number for the contact's manager.|
|DisplayName|Manager Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|managerphone|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MarketingOnly"></a> MarketingOnly

|Property|Value|
|--------|-----|
|Description|Whether is only for marketing|
|DisplayName|Marketing Only|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|marketingonly|
|RequiredLevel|None|
|Type|Boolean|

#### MarketingOnly Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_MiddleName"></a> MiddleName

|Property|Value|
|--------|-----|
|Description|Type the contact's middle name or initial to make sure the contact is addressed correctly.|
|DisplayName|Middle Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|middlename|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobilePhone"></a> MobilePhone

|Property|Value|
|--------|-----|
|Description|Type the mobile phone number for the contact.|
|DisplayName|Mobile Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobilephone|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NickName"></a> NickName

|Property|Value|
|--------|-----|
|Description|Type the contact's nickname.|
|DisplayName|Nickname|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|nickname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NumberOfChildren"></a> NumberOfChildren

|Property|Value|
|--------|-----|
|Description|Type the number of children the contact has for reference in follow-up phone calls and other communications.|
|DisplayName|No. of Children|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|numberofchildren|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


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


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_Pager"></a> Pager

|Property|Value|
|--------|-----|
|Description|Type the pager number for the contact.|
|DisplayName|Pager|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|pager|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentCustomerId"></a> ParentCustomerId

|Property|Value|
|--------|-----|
|Description|Select the parent account or parent contact for the contact to provide a quick link to additional details, such as financial information, activities, and opportunities.|
|DisplayName|Company Name|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentcustomerid|
|RequiredLevel|None|
|Targets|account,contact|
|Type|Customer|


### <a name="BKMK_ParentCustomerIdType"></a> ParentCustomerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Parent Customer Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentcustomeridtype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_ParticipatesInWorkflow"></a> ParticipatesInWorkflow

|Property|Value|
|--------|-----|
|Description|Shows whether the contact participates in workflow rules.|
|DisplayName|Participates in Workflow|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|participatesinworkflow|
|RequiredLevel|None|
|Type|Boolean|

#### ParticipatesInWorkflow Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_PaymentTermsCode"></a> PaymentTermsCode

|Property|Value|
|--------|-----|
|Description|Select the payment terms to indicate when the customer needs to pay the total amount.|
|DisplayName|Payment Terms|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|paymenttermscode|
|RequiredLevel|None|
|Type|Picklist|

#### PaymentTermsCode Choices/Options

|Value|Label|
|-----|-----|
|1|Net 30|
|2|2% 10, Net 30|
|3|Net 45|
|4|Net 60|



### <a name="BKMK_PreferredAppointmentDayCode"></a> PreferredAppointmentDayCode

|Property|Value|
|--------|-----|
|Description|Select the preferred day of the week for service appointments.|
|DisplayName|Preferred Day|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredappointmentdaycode|
|RequiredLevel|None|
|Type|Picklist|

#### PreferredAppointmentDayCode Choices/Options

|Value|Label|
|-----|-----|
|0|Sunday|
|1|Monday|
|2|Tuesday|
|3|Wednesday|
|4|Thursday|
|5|Friday|
|6|Saturday|



### <a name="BKMK_PreferredAppointmentTimeCode"></a> PreferredAppointmentTimeCode

|Property|Value|
|--------|-----|
|Description|Select the preferred time of day for service appointments.|
|DisplayName|Preferred Time|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredappointmenttimecode|
|RequiredLevel|None|
|Type|Picklist|

#### PreferredAppointmentTimeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Morning|
|2|Afternoon|
|3|Evening|



### <a name="BKMK_PreferredContactMethodCode"></a> PreferredContactMethodCode

|Property|Value|
|--------|-----|
|Description|Select the preferred method of contact.|
|DisplayName|Preferred Method of Contact|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredcontactmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### PreferredContactMethodCode Choices/Options

|Value|Label|
|-----|-----|
|1|Any|
|2|Email|
|3|Phone|
|4|Fax|
|5|Mail|



### <a name="BKMK_PreferredSystemUserId"></a> PreferredSystemUserId

|Property|Value|
|--------|-----|
|Description|Choose the regular or preferred customer service representative for reference when scheduling service activities for the contact.|
|DisplayName|Preferred User|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredsystemuserid|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Salutation"></a> Salutation

|Property|Value|
|--------|-----|
|Description|Type the salutation of the contact to make sure the contact is addressed correctly in sales calls, email messages, and marketing campaigns.|
|DisplayName|Salutation|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|salutation|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ShippingMethodCode"></a> ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Select a shipping method for deliveries sent to this address.|
|DisplayName|Shipping Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|shippingmethodcode|
|RequiredLevel|None|
|Type|Picklist|

#### ShippingMethodCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|--------|-----|
|Description|Choose the service level agreement (SLA) that you want to apply to the Contact record.|
|DisplayName|SLA|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|slaid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SpousesName"></a> SpousesName

|Property|Value|
|--------|-----|
|Description|Type the name of the contact's spouse or partner for reference during calls, events, or other communications with the contact.|
|DisplayName|Spouse/Partner Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|spousesname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the stage.|
|DisplayName|(Deprecated) Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the contact is active or inactive. Inactive contacts are read-only and can't be edited unless they are reactivated.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the contact's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Subscription|
|IsValidForForm|False|
|IsValidForRead|False|
|IsValidForUpdate|False|
|LogicalName|subscriptionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Suffix"></a> Suffix

|Property|Value|
|--------|-----|
|Description|Type the suffix used in the contact's name, such as Jr. or Sr. to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.|
|DisplayName|Suffix|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|suffix|
|MaxLength|10|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Telephone1"></a> Telephone1

|Property|Value|
|--------|-----|
|Description|Type the main phone number for this contact.|
|DisplayName|Business Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|telephone1|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Telephone2"></a> Telephone2

|Property|Value|
|--------|-----|
|Description|Type a second phone number for this contact.|
|DisplayName|Home Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|telephone2|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Telephone3"></a> Telephone3

|Property|Value|
|--------|-----|
|Description|Type a third phone number for this contact.|
|DisplayName|Telephone 3|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|telephone3|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TerritoryCode"></a> TerritoryCode

|Property|Value|
|--------|-----|
|Description|Select a region or territory for the contact for use in segmentation and analysis.|
|DisplayName|Territory|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|territorycode|
|RequiredLevel|None|
|Type|Picklist|

#### TerritoryCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Choose the local currency for the record to make sure budgets are reported in the correct currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|(Deprecated) Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_WebSiteUrl"></a> WebSiteUrl

|Property|Value|
|--------|-----|
|Description|Type the contact's professional or personal website or blog URL.|
|DisplayName|Website|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|websiteurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiFirstName"></a> YomiFirstName

|Property|Value|
|--------|-----|
|Description|Type the phonetic spelling of the contact's first name, if the name is specified in Japanese, to make sure the name is pronounced correctly in phone calls with the contact.|
|DisplayName|Yomi First Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomifirstname|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiLastName"></a> YomiLastName

|Property|Value|
|--------|-----|
|Description|Type the phonetic spelling of the contact's last name, if the name is specified in Japanese, to make sure the name is pronounced correctly in phone calls with the contact.|
|DisplayName|Yomi Last Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomilastname|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiMiddleName"></a> YomiMiddleName

|Property|Value|
|--------|-----|
|Description|Type the phonetic spelling of the contact's middle name, if the name is specified in Japanese, to make sure the name is pronounced correctly in phone calls with the contact.|
|DisplayName|Yomi Middle Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomimiddlename|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AccountId](#BKMK_AccountId)
- [AccountIdName](#BKMK_AccountIdName)
- [AccountIdYomiName](#BKMK_AccountIdYomiName)
- [Address1_Composite](#BKMK_Address1_Composite)
- [Address2_Composite](#BKMK_Address2_Composite)
- [Address3_Composite](#BKMK_Address3_Composite)
- [Aging30](#BKMK_Aging30)
- [Aging30_Base](#BKMK_Aging30_Base)
- [Aging60](#BKMK_Aging60)
- [Aging60_Base](#BKMK_Aging60_Base)
- [Aging90](#BKMK_Aging90)
- [Aging90_Base](#BKMK_Aging90_Base)
- [AnnualIncome_Base](#BKMK_AnnualIncome_Base)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByExternalParty](#BKMK_CreatedByExternalParty)
- [CreatedByExternalPartyName](#BKMK_CreatedByExternalPartyName)
- [CreatedByExternalPartyYomiName](#BKMK_CreatedByExternalPartyYomiName)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CreditLimit_Base](#BKMK_CreditLimit_Base)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FullName](#BKMK_FullName)
- [IsAutoCreate](#BKMK_IsAutoCreate)
- [IsPrivate](#BKMK_IsPrivate)
- [MasterContactIdName](#BKMK_MasterContactIdName)
- [MasterContactIdYomiName](#BKMK_MasterContactIdYomiName)
- [MasterId](#BKMK_MasterId)
- [Merged](#BKMK_Merged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByExternalParty](#BKMK_ModifiedByExternalParty)
- [ModifiedByExternalPartyName](#BKMK_ModifiedByExternalPartyName)
- [ModifiedByExternalPartyYomiName](#BKMK_ModifiedByExternalPartyYomiName)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentContactId](#BKMK_ParentContactId)
- [ParentContactIdName](#BKMK_ParentContactIdName)
- [ParentContactIdYomiName](#BKMK_ParentContactIdYomiName)
- [ParentCustomerIdName](#BKMK_ParentCustomerIdName)
- [ParentCustomerIdYomiName](#BKMK_ParentCustomerIdYomiName)
- [PreferredSystemUserIdName](#BKMK_PreferredSystemUserIdName)
- [PreferredSystemUserIdYomiName](#BKMK_PreferredSystemUserIdYomiName)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [SLAInvokedIdName](#BKMK_SLAInvokedIdName)
- [SLAName](#BKMK_SLAName)
- [TimeSpentByMeOnEmailAndMeetings](#BKMK_TimeSpentByMeOnEmailAndMeetings)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)
- [YomiFullName](#BKMK_YomiFullName)


### <a name="BKMK_AccountId"></a> AccountId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the account with which the contact is associated.|
|DisplayName|Account|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|accountid|
|RequiredLevel|None|
|Targets|account|
|Type|Lookup|


### <a name="BKMK_AccountIdName"></a> AccountIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|accountidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AccountIdYomiName"></a> AccountIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|accountidyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Composite"></a> Address1_Composite

|Property|Value|
|--------|-----|
|Description|Shows the complete primary address.|
|DisplayName|Address 1|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_composite|
|MaxLength|1000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Address2_Composite"></a> Address2_Composite

|Property|Value|
|--------|-----|
|Description|Shows the complete secondary address.|
|DisplayName|Address 2|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_composite|
|MaxLength|1000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Address3_Composite"></a> Address3_Composite

|Property|Value|
|--------|-----|
|Description|Shows the complete third address.|
|DisplayName|Address 3|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address3_composite|
|MaxLength|1000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Aging30"></a> Aging30

|Property|Value|
|--------|-----|
|Description|For system use only.|
|DisplayName|Aging 30|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aging30|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Aging30_Base"></a> Aging30_Base

|Property|Value|
|--------|-----|
|Description|Shows the Aging 30 field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.|
|DisplayName|Aging 30 (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aging30_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Aging60"></a> Aging60

|Property|Value|
|--------|-----|
|Description|For system use only.|
|DisplayName|Aging 60|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aging60|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Aging60_Base"></a> Aging60_Base

|Property|Value|
|--------|-----|
|Description|Shows the Aging 60 field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.|
|DisplayName|Aging 60 (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aging60_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Aging90"></a> Aging90

|Property|Value|
|--------|-----|
|Description|For system use only.|
|DisplayName|Aging 90|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aging90|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Aging90_Base"></a> Aging90_Base

|Property|Value|
|--------|-----|
|Description|Shows the Aging 90 field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.|
|DisplayName|Aging 90 (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aging90_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_AnnualIncome_Base"></a> AnnualIncome_Base

|Property|Value|
|--------|-----|
|Description|Shows the Annual Income field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.|
|DisplayName|Annual Income (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|annualincome_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByExternalParty"></a> CreatedByExternalParty

|Property|Value|
|--------|-----|
|Description|Shows the external party who created the record.|
|DisplayName|Created By (External Party)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdbyexternalparty|
|RequiredLevel|None|
|Targets|externalparty|
|Type|Lookup|


### <a name="BKMK_CreatedByExternalPartyName"></a> CreatedByExternalPartyName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyexternalpartyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByExternalPartyYomiName"></a> CreatedByExternalPartyYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyexternalpartyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
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
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_CreditLimit_Base"></a> CreditLimit_Base

|Property|Value|
|--------|-----|
|Description|Shows the Credit Limit field converted to the system's default base currency for reporting purposes. The calculations use the exchange rate specified in the Currencies area.|
|DisplayName|Credit Limit (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|creditlimit_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Entity Image Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_FullName"></a> FullName

|Property|Value|
|--------|-----|
|Description|Combines and shows the contact's first and last names so that the full name can be displayed in views and reports.|
|DisplayName|Full Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fullname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsAutoCreate"></a> IsAutoCreate

|Property|Value|
|--------|-----|
|Description|Information about whether the contact was auto-created when promoting an email or an appointment.|
|DisplayName|Auto-created|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|isautocreate|
|RequiredLevel|None|
|Type|Boolean|

#### IsAutoCreate Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsPrivate"></a> IsPrivate

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|isprivate|
|RequiredLevel|None|
|Type|Boolean|

#### IsPrivate Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_MasterContactIdName"></a> MasterContactIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mastercontactidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MasterContactIdYomiName"></a> MasterContactIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mastercontactidyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MasterId"></a> MasterId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the master contact for merge.|
|DisplayName|Master ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|masterid|
|RequiredLevel|None|
|Targets|contact|
|Type|Lookup|


### <a name="BKMK_Merged"></a> Merged

|Property|Value|
|--------|-----|
|Description|Shows whether the account has been merged with a master contact.|
|DisplayName|Merged|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|merged|
|RequiredLevel|None|
|Type|Boolean|

#### Merged Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByExternalParty"></a> ModifiedByExternalParty

|Property|Value|
|--------|-----|
|Description|Shows the external party who modified the record.|
|DisplayName|Modified By (External Party)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedbyexternalparty|
|RequiredLevel|None|
|Targets|externalparty|
|Type|Lookup|


### <a name="BKMK_ModifiedByExternalPartyName"></a> ModifiedByExternalPartyName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyexternalpartyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByExternalPartyYomiName"></a> ModifiedByExternalPartyYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyexternalpartyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
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
|Description|Shows who last updated the record on behalf of another user.|
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


### <a name="BKMK_OnHoldTime"></a> OnHoldTime

|Property|Value|
|--------|-----|
|Description|Shows how long, in minutes, that the record was on hold.|
|DisplayName|On Hold Time (Minutes)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onholdtime|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the contact.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the contact.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the contact.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentContactId"></a> ParentContactId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent contact.|
|DisplayName|Parent Contact|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentcontactid|
|RequiredLevel|None|
|Targets|contact|
|Type|Lookup|


### <a name="BKMK_ParentContactIdName"></a> ParentContactIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentcontactidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentContactIdYomiName"></a> ParentContactIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentcontactidyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentCustomerIdName"></a> ParentCustomerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentcustomeridname|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_ParentCustomerIdYomiName"></a> ParentCustomerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentcustomeridyominame|
|MaxLength|450|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_PreferredSystemUserIdName"></a> PreferredSystemUserIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|preferredsystemuseridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PreferredSystemUserIdYomiName"></a> PreferredSystemUserIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|preferredsystemuseridyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|--------|-----|
|Description|Last SLA that was applied to this case. This field is for internal use only.|
|DisplayName|Last SLA applied|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SLAInvokedIdName"></a> SLAInvokedIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SLAName"></a> SLAName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slaname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TimeSpentByMeOnEmailAndMeetings"></a> TimeSpentByMeOnEmailAndMeetings

|Property|Value|
|--------|-----|
|Description|Total time spent for emails (read and write) and meetings by me in relation to the contact record.|
|DisplayName|Time Spent by me|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timespentbymeonemailandmeetings|
|MaxLength|1250|
|RequiredLevel|None|
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


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the contact.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_YomiFullName"></a> YomiFullName

|Property|Value|
|--------|-----|
|Description|Shows the combined Yomi first and last names of the contact so that the full phonetic name can be displayed in views and reports.|
|DisplayName|Yomi Full Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomifullname|
|MaxLength|450|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [contact_principalobjectattributeaccess](#BKMK_contact_principalobjectattributeaccess)
- [slakpiinstance_contact](#BKMK_slakpiinstance_contact)
- [socialactivity_postauthoraccount_contacts](#BKMK_socialactivity_postauthoraccount_contacts)
- [Contact_Email_EmailSender](#BKMK_Contact_Email_EmailSender)
- [Contact_Tasks](#BKMK_Contact_Tasks)
- [contact_PostFollows](#BKMK_contact_PostFollows)
- [Contact_RecurringAppointmentMasters](#BKMK_Contact_RecurringAppointmentMasters)
- [contact_master_contact](#BKMK_contact_master_contact)
- [lk_contact_feedback_createdby](#BKMK_lk_contact_feedback_createdby)
- [contact_actioncard](#BKMK_contact_actioncard)
- [contact_connections2](#BKMK_contact_connections2)
- [Contact_BulkDeleteFailures](#BKMK_Contact_BulkDeleteFailures)
- [contact_activity_parties](#BKMK_contact_activity_parties)
- [Contact_DuplicateBaseRecord](#BKMK_Contact_DuplicateBaseRecord)
- [Contact_Annotation](#BKMK_Contact_Annotation)
- [Contact_SocialActivities](#BKMK_Contact_SocialActivities)
- [Contact_ActivityPointers](#BKMK_Contact_ActivityPointers)
- [Contact_MailboxTrackingFolder](#BKMK_Contact_MailboxTrackingFolder)
- [account_primary_contact](#BKMK_account_primary_contact)
- [Socialprofile_customer_contacts](#BKMK_Socialprofile_customer_contacts)
- [socialactivity_postauthor_contacts](#BKMK_socialactivity_postauthor_contacts)
- [lk_contact_feedback_createdonbehalfby](#BKMK_lk_contact_feedback_createdonbehalfby)
- [Contact_Emails](#BKMK_Contact_Emails)
- [Contact_Appointments](#BKMK_Contact_Appointments)
- [Contact_Feedback](#BKMK_Contact_Feedback)
- [Contact_ProcessSessions](#BKMK_Contact_ProcessSessions)
- [Contact_AsyncOperations](#BKMK_Contact_AsyncOperations)
- [contact_connections1](#BKMK_contact_connections1)
- [Contact_CustomerAddress](#BKMK_Contact_CustomerAddress)
- [Contact_Phonecalls](#BKMK_Contact_Phonecalls)
- [contact_customer_contacts](#BKMK_contact_customer_contacts)
- [Contact_SyncErrors](#BKMK_Contact_SyncErrors)
- [Contact_DuplicateMatchingRecord](#BKMK_Contact_DuplicateMatchingRecord)
- [Contact_Faxes](#BKMK_Contact_Faxes)
- [Contact_Letters](#BKMK_Contact_Letters)


### <a name="BKMK_contact_principalobjectattributeaccess"></a> contact_principalobjectattributeaccess

Same as principalobjectattributeaccess table [contact_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_contact_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|contact_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slakpiinstance_contact"></a> slakpiinstance_contact

Same as slakpiinstance table [slakpiinstance_contact](slakpiinstance.md#BKMK_slakpiinstance_contact) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|regarding|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|slakpiinstance_contact|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_socialactivity_postauthoraccount_contacts"></a> socialactivity_postauthoraccount_contacts

Same as socialactivity table [socialactivity_postauthoraccount_contacts](socialactivity.md#BKMK_socialactivity_postauthoraccount_contacts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|postauthoraccount|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|socialactivity_postauthoraccount_contacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_Email_EmailSender"></a> Contact_Email_EmailSender

Same as email table [Contact_Email_EmailSender](email.md#BKMK_Contact_Email_EmailSender) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|emailsender|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_Email_EmailSender|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_Tasks"></a> Contact_Tasks

Same as task table [Contact_Tasks](task.md#BKMK_Contact_Tasks) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_contact_PostFollows"></a> contact_PostFollows

Same as postfollow table [contact_PostFollows](postfollow.md#BKMK_contact_PostFollows) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|contact_PostFollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_RecurringAppointmentMasters"></a> Contact_RecurringAppointmentMasters

Same as recurringappointmentmaster table [Contact_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_Contact_RecurringAppointmentMasters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_contact_master_contact"></a> contact_master_contact

Same as contact table [contact_master_contact](contact.md#BKMK_contact_master_contact) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|masterid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|contact_master_contact|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_contact_feedback_createdby"></a> lk_contact_feedback_createdby

Same as feedback table [lk_contact_feedback_createdby](feedback.md#BKMK_lk_contact_feedback_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|createdbycontact|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_contact_feedback_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_contact_actioncard"></a> contact_actioncard

Same as actioncard table [contact_actioncard](actioncard.md#BKMK_contact_actioncard) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|contact_actioncard|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_contact_connections2"></a> contact_connections2

Same as connection table [contact_connections2](connection.md#BKMK_contact_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|contact_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_BulkDeleteFailures"></a> Contact_BulkDeleteFailures

Same as bulkdeletefailure table [Contact_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Contact_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_contact_activity_parties"></a> contact_activity_parties

Same as activityparty table [contact_activity_parties](activityparty.md#BKMK_contact_activity_parties) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|partyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|contact_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_DuplicateBaseRecord"></a> Contact_DuplicateBaseRecord

Same as duplicaterecord table [Contact_DuplicateBaseRecord](duplicaterecord.md#BKMK_Contact_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_Annotation"></a> Contact_Annotation

Same as annotation table [Contact_Annotation](annotation.md#BKMK_Contact_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_SocialActivities"></a> Contact_SocialActivities

Same as socialactivity table [Contact_SocialActivities](socialactivity.md#BKMK_Contact_SocialActivities) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_ActivityPointers"></a> Contact_ActivityPointers

Same as activitypointer table [Contact_ActivityPointers](activitypointer.md#BKMK_Contact_ActivityPointers) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 20|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_MailboxTrackingFolder"></a> Contact_MailboxTrackingFolder

Same as mailboxtrackingfolder table [Contact_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Contact_MailboxTrackingFolder) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_MailboxTrackingFolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_account_primary_contact"></a> account_primary_contact

Same as account table [account_primary_contact](account.md#BKMK_account_primary_contact) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|primarycontactid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|account_primary_contact|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: Cascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Socialprofile_customer_contacts"></a> Socialprofile_customer_contacts

Same as socialprofile table [Socialprofile_customer_contacts](socialprofile.md#BKMK_Socialprofile_customer_contacts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|customerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Socialprofile_customer_contacts|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 40|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_socialactivity_postauthor_contacts"></a> socialactivity_postauthor_contacts

Same as socialactivity table [socialactivity_postauthor_contacts](socialactivity.md#BKMK_socialactivity_postauthor_contacts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|postauthor|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|socialactivity_postauthor_contacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_contact_feedback_createdonbehalfby"></a> lk_contact_feedback_createdonbehalfby

Same as feedback table [lk_contact_feedback_createdonbehalfby](feedback.md#BKMK_lk_contact_feedback_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|createdonbehalfbycontact|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_contact_feedback_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_Emails"></a> Contact_Emails

Same as email table [Contact_Emails](email.md#BKMK_Contact_Emails) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_Appointments"></a> Contact_Appointments

Same as appointment table [Contact_Appointments](appointment.md#BKMK_Contact_Appointments) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_Feedback"></a> Contact_Feedback

Same as feedback table [Contact_Feedback](feedback.md#BKMK_Contact_Feedback) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Feedback|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 150|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_ProcessSessions"></a> Contact_ProcessSessions

Same as processsession table [Contact_ProcessSessions](processsession.md#BKMK_Contact_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_AsyncOperations"></a> Contact_AsyncOperations

Same as asyncoperation table [Contact_AsyncOperations](asyncoperation.md#BKMK_Contact_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_contact_connections1"></a> contact_connections1

Same as connection table [contact_connections1](connection.md#BKMK_contact_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|contact_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_CustomerAddress"></a> Contact_CustomerAddress

Same as customeraddress table [Contact_CustomerAddress](customeraddress.md#BKMK_Contact_CustomerAddress) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customeraddress|
|ReferencingAttribute|parentid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_CustomerAddress|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_Phonecalls"></a> Contact_Phonecalls

Same as phonecall table [Contact_Phonecalls](phonecall.md#BKMK_Contact_Phonecalls) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Phonecalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_contact_customer_contacts"></a> contact_customer_contacts

Same as contact table [contact_customer_contacts](contact.md#BKMK_contact_customer_contacts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|parentcustomerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|contact_customer_contacts|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 40|
|CascadeConfiguration|Assign: Cascade<br />Delete: RemoveLink<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_SyncErrors"></a> Contact_SyncErrors

Same as syncerror table [Contact_SyncErrors](syncerror.md#BKMK_Contact_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_DuplicateMatchingRecord"></a> Contact_DuplicateMatchingRecord

Same as duplicaterecord table [Contact_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Contact_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Contact_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Contact_Faxes"></a> Contact_Faxes

Same as fax table [Contact_Faxes](fax.md#BKMK_Contact_Faxes) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Contact_Letters"></a> Contact_Letters

Same as letter table [Contact_Letters](letter.md#BKMK_Contact_Letters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Contact_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [transactioncurrency_contact](#BKMK_transactioncurrency_contact)
- [contact_master_contact](#BKMK_contact_master_contact)
- [lk_contactbase_createdby](#BKMK_lk_contactbase_createdby)
- [lk_contact_createdonbehalfby](#BKMK_lk_contact_createdonbehalfby)
- [team_contacts](#BKMK_team_contacts)
- [manualsla_contact](#BKMK_manualsla_contact)
- [system_user_contacts](#BKMK_system_user_contacts)
- [lk_contactbase_modifiedby](#BKMK_lk_contactbase_modifiedby)
- [sla_contact](#BKMK_sla_contact)
- [contact_customer_accounts](#BKMK_contact_customer_accounts)
- [lk_contact_modifiedonbehalfby](#BKMK_lk_contact_modifiedonbehalfby)
- [processstage_contact](#BKMK_processstage_contact)
- [contact_owning_user](#BKMK_contact_owning_user)
- [contact_customer_contacts](#BKMK_contact_customer_contacts)
- [business_unit_contacts](#BKMK_business_unit_contacts)


### <a name="BKMK_transactioncurrency_contact"></a> transactioncurrency_contact

See transactioncurrency Table [transactioncurrency_contact](transactioncurrency.md#BKMK_transactioncurrency_contact) One-To-Many relationship.

### <a name="BKMK_contact_master_contact"></a> contact_master_contact

See contact Table [contact_master_contact](contact.md#BKMK_contact_master_contact) One-To-Many relationship.

### <a name="BKMK_lk_contactbase_createdby"></a> lk_contactbase_createdby

See systemuser Table [lk_contactbase_createdby](systemuser.md#BKMK_lk_contactbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_contact_createdonbehalfby"></a> lk_contact_createdonbehalfby

See systemuser Table [lk_contact_createdonbehalfby](systemuser.md#BKMK_lk_contact_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_team_contacts"></a> team_contacts

See team Table [team_contacts](team.md#BKMK_team_contacts) One-To-Many relationship.

### <a name="BKMK_manualsla_contact"></a> manualsla_contact

See sla Table [manualsla_contact](sla.md#BKMK_manualsla_contact) One-To-Many relationship.

### <a name="BKMK_system_user_contacts"></a> system_user_contacts

See systemuser Table [system_user_contacts](systemuser.md#BKMK_system_user_contacts) One-To-Many relationship.

### <a name="BKMK_lk_contactbase_modifiedby"></a> lk_contactbase_modifiedby

See systemuser Table [lk_contactbase_modifiedby](systemuser.md#BKMK_lk_contactbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_sla_contact"></a> sla_contact

See sla Table [sla_contact](sla.md#BKMK_sla_contact) One-To-Many relationship.

### <a name="BKMK_contact_customer_accounts"></a> contact_customer_accounts

See account Table [contact_customer_accounts](account.md#BKMK_contact_customer_accounts) One-To-Many relationship.

### <a name="BKMK_lk_contact_modifiedonbehalfby"></a> lk_contact_modifiedonbehalfby

See systemuser Table [lk_contact_modifiedonbehalfby](systemuser.md#BKMK_lk_contact_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_processstage_contact"></a> processstage_contact

See processstage Table [processstage_contact](processstage.md#BKMK_processstage_contact) One-To-Many relationship.

### <a name="BKMK_contact_owning_user"></a> contact_owning_user

See systemuser Table [contact_owning_user](systemuser.md#BKMK_contact_owning_user) One-To-Many relationship.

### <a name="BKMK_contact_customer_contacts"></a> contact_customer_contacts

See contact Table [contact_customer_contacts](contact.md#BKMK_contact_customer_contacts) One-To-Many relationship.

### <a name="BKMK_business_unit_contacts"></a> business_unit_contacts

See businessunit Table [business_unit_contacts](businessunit.md#BKMK_business_unit_contacts) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" />