---
title: "Contact table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Contact table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Contact table/entity reference (Microsoft Dataverse)

Person with whom a business unit has a relationship, such as customer, supplier, and colleague.

## Messages

The following table lists the messages for the Contact table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /contacts(*contactid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /contacts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /contacts(*contactid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: True |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Merge`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Merge?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.MergeRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /contacts(*contactid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /contacts<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /contacts(*contactid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /contacts(*contactid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /contacts(*contactid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Contact table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Contact** |
| **DisplayCollectionName** | **Contacts** |
| **SchemaName** | `Contact` |
| **CollectionSchemaName** | `Contacts` |
| **EntitySetName** | `contacts`|
| **LogicalName** | `contact` |
| **LogicalCollectionName** | `contacts` |
| **PrimaryIdAttribute** | `contactid` |
| **PrimaryNameAttribute** |`fullname` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

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
- [adx_ConfirmRemovePassword](#BKMK_adx_ConfirmRemovePassword)
- [Adx_CreatedByIPAddress](#BKMK_Adx_CreatedByIPAddress)
- [Adx_CreatedByUsername](#BKMK_Adx_CreatedByUsername)
- [adx_identity_accessfailedcount](#BKMK_adx_identity_accessfailedcount)
- [adx_identity_emailaddress1confirmed](#BKMK_adx_identity_emailaddress1confirmed)
- [adx_identity_lastsuccessfullogin](#BKMK_adx_identity_lastsuccessfullogin)
- [adx_identity_locallogindisabled](#BKMK_adx_identity_locallogindisabled)
- [adx_identity_lockoutenabled](#BKMK_adx_identity_lockoutenabled)
- [adx_identity_lockoutenddate](#BKMK_adx_identity_lockoutenddate)
- [adx_identity_logonenabled](#BKMK_adx_identity_logonenabled)
- [adx_identity_mobilephoneconfirmed](#BKMK_adx_identity_mobilephoneconfirmed)
- [adx_identity_newpassword](#BKMK_adx_identity_newpassword)
- [adx_identity_passwordhash](#BKMK_adx_identity_passwordhash)
- [adx_identity_securitystamp](#BKMK_adx_identity_securitystamp)
- [adx_identity_twofactorenabled](#BKMK_adx_identity_twofactorenabled)
- [adx_identity_username](#BKMK_adx_identity_username)
- [Adx_ModifiedByIPAddress](#BKMK_Adx_ModifiedByIPAddress)
- [Adx_ModifiedByUsername](#BKMK_Adx_ModifiedByUsername)
- [Adx_OrganizationName](#BKMK_Adx_OrganizationName)
- [adx_preferredlcid](#BKMK_adx_preferredlcid)
- [adx_profilealert](#BKMK_adx_profilealert)
- [adx_profilealertdate](#BKMK_adx_profilealertdate)
- [adx_profilealertinstructions](#BKMK_adx_profilealertinstructions)
- [Adx_ProfileIsAnonymous](#BKMK_Adx_ProfileIsAnonymous)
- [Adx_ProfileLastActivity](#BKMK_Adx_ProfileLastActivity)
- [adx_profilemodifiedon](#BKMK_adx_profilemodifiedon)
- [adx_PublicProfileCopy](#BKMK_adx_PublicProfileCopy)
- [Adx_TimeZone](#BKMK_Adx_TimeZone)
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
- [msa_managingpartnerid](#BKMK_msa_managingpartnerid)
- [msdyn_disablewebtracking](#BKMK_msdyn_disablewebtracking)
- [msdyn_isminor](#BKMK_msdyn_isminor)
- [msdyn_isminorwithparentalconsent](#BKMK_msdyn_isminorwithparentalconsent)
- [msdyn_portaltermsagreementdate](#BKMK_msdyn_portaltermsagreementdate)
- [mspp_userpreferredlcid](#BKMK_mspp_userpreferredlcid)
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
|---|---|
|Description|**Select the contact's role within the company or sales process, such as decision maker, employee, or influencer.**|
|DisplayName|**Role**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accountrolecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_accountrolecode`|

#### AccountRoleCode Choices/Options

|Value|Label|
|---|---|
|1|**Decision Maker**|
|2|**Employee**|
|3|**Influencer**|

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
|GlobalChoiceName|`contact_address1_addresstypecode`|

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
|GlobalChoiceName|`contact_address1_freighttermscode`|

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
|GlobalChoiceName|`contact_address1_shippingmethodcode`|

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
|DisplayName|**Address 1: Phone**|
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
|GlobalChoiceName|`contact_address2_addresstypecode`|

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
|GlobalChoiceName|`contact_address2_freighttermscode`|

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
|MaxLength|100|

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
|GlobalChoiceName|`contact_address2_shippingmethodcode`|

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

### <a name="BKMK_Address3_AddressId"></a> Address3_AddressId

|Property|Value|
|---|---|
|Description|**Unique identifier for address 3.**|
|DisplayName|**Address 3: ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`address3_addressid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Address3_AddressTypeCode"></a> Address3_AddressTypeCode

|Property|Value|
|---|---|
|Description|**Select the third address type.**|
|DisplayName|**Address 3: Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_address3_addresstypecode`|

#### Address3_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address3_City"></a> Address3_City

|Property|Value|
|---|---|
|Description|**Type the city for the 3rd address.**|
|DisplayName|**Address 3: City**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_city`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Address3_Country"></a> Address3_Country

|Property|Value|
|---|---|
|Description|**the country or region for the 3rd address.**|
|DisplayName|**Address3: Country/Region**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_country`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Address3_County"></a> Address3_County

|Property|Value|
|---|---|
|Description|**Type the county for the third address.**|
|DisplayName|**Address 3: County**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_county`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address3_Fax"></a> Address3_Fax

|Property|Value|
|---|---|
|Description|**Type the fax number associated with the third address.**|
|DisplayName|**Address 3: Fax**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_fax`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address3_FreightTermsCode"></a> Address3_FreightTermsCode

|Property|Value|
|---|---|
|Description|**Select the freight terms for the third address to make sure shipping orders are processed correctly.**|
|DisplayName|**Address 3: Freight Terms**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_freighttermscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_address3_freighttermscode`|

#### Address3_FreightTermsCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address3_Latitude"></a> Address3_Latitude

|Property|Value|
|---|---|
|Description|**Type the latitude value for the third address for use in mapping and other applications.**|
|DisplayName|**Address 3: Latitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_latitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|90|
|MinValue|-90|
|Precision|5|

### <a name="BKMK_Address3_Line1"></a> Address3_Line1

|Property|Value|
|---|---|
|Description|**the first line of the 3rd address.**|
|DisplayName|**Address3: Street 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_line1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address3_Line2"></a> Address3_Line2

|Property|Value|
|---|---|
|Description|**the second line of the 3rd address.**|
|DisplayName|**Address3: Street 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_line2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address3_Line3"></a> Address3_Line3

|Property|Value|
|---|---|
|Description|**the third line of the 3rd address.**|
|DisplayName|**Address3: Street 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_line3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address3_Longitude"></a> Address3_Longitude

|Property|Value|
|---|---|
|Description|**Type the longitude value for the third address for use in mapping and other applications.**|
|DisplayName|**Address 3: Longitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_longitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|180|
|MinValue|-180|
|Precision|5|

### <a name="BKMK_Address3_Name"></a> Address3_Name

|Property|Value|
|---|---|
|Description|**Type a descriptive name for the third address, such as Corporate Headquarters.**|
|DisplayName|**Address 3: Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_Address3_PostalCode"></a> Address3_PostalCode

|Property|Value|
|---|---|
|Description|**the ZIP Code or postal code for the 3rd address.**|
|DisplayName|**Address3: ZIP/Postal Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_postalcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_Address3_PostOfficeBox"></a> Address3_PostOfficeBox

|Property|Value|
|---|---|
|Description|**the post office box number of the 3rd address.**|
|DisplayName|**Address 3: Post Office Box**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_postofficebox`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_Address3_PrimaryContactName"></a> Address3_PrimaryContactName

|Property|Value|
|---|---|
|Description|**Type the name of the main contact at the account's third address.**|
|DisplayName|**Address 3: Primary Contact Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_primarycontactname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Address3_ShippingMethodCode"></a> Address3_ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Select a shipping method for deliveries sent to this address.**|
|DisplayName|**Address 3: Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_address3_shippingmethodcode`|

#### Address3_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address3_StateOrProvince"></a> Address3_StateOrProvince

|Property|Value|
|---|---|
|Description|**the state or province of the third address.**|
|DisplayName|**Address3: State/Province**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_stateorprovince`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address3_Telephone1"></a> Address3_Telephone1

|Property|Value|
|---|---|
|Description|**Type the main phone number associated with the third address.**|
|DisplayName|**Address 3: Telephone1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address3_Telephone2"></a> Address3_Telephone2

|Property|Value|
|---|---|
|Description|**Type a second phone number associated with the third address.**|
|DisplayName|**Address 3: Telephone2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address3_Telephone3"></a> Address3_Telephone3

|Property|Value|
|---|---|
|Description|**Type a third phone number associated with the primary address.**|
|DisplayName|**Address 3: Telephone3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address3_UPSZone"></a> Address3_UPSZone

|Property|Value|
|---|---|
|Description|**Type the UPS zone of the third address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.**|
|DisplayName|**Address 3: UPS Zone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_upszone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4|

### <a name="BKMK_Address3_UTCOffset"></a> Address3_UTCOffset

|Property|Value|
|---|---|
|Description|**Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.**|
|DisplayName|**Address 3: UTC Offset**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_utcoffset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_adx_ConfirmRemovePassword"></a> adx_ConfirmRemovePassword

|Property|Value|
|---|---|
|Description||
|DisplayName|**Confirm Remove Password**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_confirmremovepassword`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_confirmremovepassword`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Adx_CreatedByIPAddress"></a> Adx_CreatedByIPAddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**Created By IP Address**|
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
|DisplayName|**Created By Username**|
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

### <a name="BKMK_adx_identity_accessfailedcount"></a> adx_identity_accessfailedcount

|Property|Value|
|---|---|
|Description|**Shows the current count of failed password attempts for the contact.**|
|DisplayName|**Access Failed Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_accessfailedcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_adx_identity_emailaddress1confirmed"></a> adx_identity_emailaddress1confirmed

|Property|Value|
|---|---|
|Description|**Determines if the email is confirmed by the contact.**|
|DisplayName|**Email Confirmed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_emailaddress1confirmed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_identity_emailaddress1confirmed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_identity_lastsuccessfullogin"></a> adx_identity_lastsuccessfullogin

|Property|Value|
|---|---|
|Description|**Indicates the last date and time the user successfully signed in to a portal.**|
|DisplayName|**Last Successful Login**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_lastsuccessfullogin`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_adx_identity_locallogindisabled"></a> adx_identity_locallogindisabled

|Property|Value|
|---|---|
|Description|**Indicates that the contact can no longer sign in to the portal using the local account.**|
|DisplayName|**Local Login Disabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_locallogindisabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_identity_locallogindisabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_identity_lockoutenabled"></a> adx_identity_lockoutenabled

|Property|Value|
|---|---|
|Description|**Determines if this contact will track failed access attempts and become locked after too many failed attempts. To prevent the contact from becoming locked, you can disable this setting.**|
|DisplayName|**Lockout Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_lockoutenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_identity_lockoutenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_identity_lockoutenddate"></a> adx_identity_lockoutenddate

|Property|Value|
|---|---|
|Description|**Shows the moment in time when the locked contact becomes unlocked again.**|
|DisplayName|**Lockout End Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_lockoutenddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_adx_identity_logonenabled"></a> adx_identity_logonenabled

|Property|Value|
|---|---|
|Description|**Determines if web authentication is enabled for the contact.**|
|DisplayName|**Login Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_logonenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_identity_logonenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_identity_mobilephoneconfirmed"></a> adx_identity_mobilephoneconfirmed

|Property|Value|
|---|---|
|Description|**Determines if the phone number is confirmed by the contact.**|
|DisplayName|**Mobile Phone Confirmed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_mobilephoneconfirmed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_identity_mobilephoneconfirmed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_identity_newpassword"></a> adx_identity_newpassword

|Property|Value|
|---|---|
|Description||
|DisplayName|**New Password Input**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_newpassword`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_adx_identity_passwordhash"></a> adx_identity_passwordhash

|Property|Value|
|---|---|
|Description||
|DisplayName|**Password Hash**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_passwordhash`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_adx_identity_securitystamp"></a> adx_identity_securitystamp

|Property|Value|
|---|---|
|Description|**A token used to manage the web authentication session.**|
|DisplayName|**Security Stamp**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_securitystamp`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_adx_identity_twofactorenabled"></a> adx_identity_twofactorenabled

|Property|Value|
|---|---|
|Description|**Determines if two-factor authentication is enabled for the contact.**|
|DisplayName|**Two Factor Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_twofactorenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_identity_twofactorenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_identity_username"></a> adx_identity_username

|Property|Value|
|---|---|
|Description|**Shows the user identity for local web authentication.**|
|DisplayName|**User Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_identity_username`|
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
|DisplayName|**Modified By IP Address**|
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
|DisplayName|**Modified By Username**|
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

### <a name="BKMK_Adx_OrganizationName"></a> Adx_OrganizationName

|Property|Value|
|---|---|
|Description||
|DisplayName|**Organization Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_organizationname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_adx_preferredlcid"></a> adx_preferredlcid

|Property|Value|
|---|---|
|Description|**User’s preferred portal LCID**|
|DisplayName|**Preferred LCID (Deprecated)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_preferredlcid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_adx_profilealert"></a> adx_profilealert

|Property|Value|
|---|---|
|Description||
|DisplayName|**Profile Alert**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_profilealert`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_contact_adx_profilealert`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_adx_profilealertdate"></a> adx_profilealertdate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Profile Alert Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_profilealertdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_adx_profilealertinstructions"></a> adx_profilealertinstructions

|Property|Value|
|---|---|
|Description||
|DisplayName|**Profile Alert Instructions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_profilealertinstructions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4096|

### <a name="BKMK_Adx_ProfileIsAnonymous"></a> Adx_ProfileIsAnonymous

|Property|Value|
|---|---|
|Description||
|DisplayName|**Profile Is Anonymous**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_profileisanonymous`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adx_profileisanonymous_contact`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Adx_ProfileLastActivity"></a> Adx_ProfileLastActivity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Profile Last Activity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_profilelastactivity`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_adx_profilemodifiedon"></a> adx_profilemodifiedon

|Property|Value|
|---|---|
|Description||
|DisplayName|**Profile Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_profilemodifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_adx_PublicProfileCopy"></a> adx_PublicProfileCopy

|Property|Value|
|---|---|
|Description||
|DisplayName|**Public Profile Copy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_publicprofilecopy`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|64000|

### <a name="BKMK_Adx_TimeZone"></a> Adx_TimeZone

|Property|Value|
|---|---|
|Description||
|DisplayName|**Time Zone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_timezone`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_Anniversary"></a> Anniversary

|Property|Value|
|---|---|
|Description|**Enter the date of the contact's wedding or service anniversary for use in customer gift programs or other communications.**|
|DisplayName|**Anniversary**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`anniversary`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|DateOnly|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_AnnualIncome"></a> AnnualIncome

|Property|Value|
|---|---|
|Description|**Type the contact's annual income for use in profiling and financial analysis.**|
|DisplayName|**Annual Income**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`annualincome`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_AssistantName"></a> AssistantName

|Property|Value|
|---|---|
|Description|**Type the name of the contact's assistant.**|
|DisplayName|**Assistant**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`assistantname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_AssistantPhone"></a> AssistantPhone

|Property|Value|
|---|---|
|Description|**Type the phone number for the contact's assistant.**|
|DisplayName|**Assistant Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`assistantphone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_BirthDate"></a> BirthDate

|Property|Value|
|---|---|
|Description|**Enter the contact's birthday for use in customer gift programs or other communications.**|
|DisplayName|**Birthday**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`birthdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|DateOnly|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Business2"></a> Business2

|Property|Value|
|---|---|
|Description|**Type a second business phone number for this contact.**|
|DisplayName|**Business Phone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`business2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Callback"></a> Callback

|Property|Value|
|---|---|
|Description|**Type a callback phone number for this contact.**|
|DisplayName|**Callback Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`callback`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_ChildrensNames"></a> ChildrensNames

|Property|Value|
|---|---|
|Description|**Type the names of the contact's children for reference in communications and client programs.**|
|DisplayName|**Children's Names**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`childrensnames`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_Company"></a> Company

|Property|Value|
|---|---|
|Description|**Type the company phone of the contact.**|
|DisplayName|**Company Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`company`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_ContactId"></a> ContactId

|Property|Value|
|---|---|
|Description|**Unique identifier of the contact.**|
|DisplayName|**Contact**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contactid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CreditLimit"></a> CreditLimit

|Property|Value|
|---|---|
|Description|**Type the credit limit of the contact for reference when you address invoice and accounting issues with the customer.**|
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
|Description|**Select whether the contact is on a credit hold, for reference when addressing invoice and accounting issues.**|
|DisplayName|**Credit Hold**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`creditonhold`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_creditonhold`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CustomerSizeCode"></a> CustomerSizeCode

|Property|Value|
|---|---|
|Description|**Select the size of the contact's company for segmentation and reporting purposes.**|
|DisplayName|**Customer Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customersizecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`contact_customersizecode`|

#### CustomerSizeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_CustomerTypeCode"></a> CustomerTypeCode

|Property|Value|
|---|---|
|Description|**Select the category that best describes the relationship between the contact and your organization.**|
|DisplayName|**Relationship Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customertypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`contact_customertypecode`|

#### CustomerTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Department"></a> Department

|Property|Value|
|---|---|
|Description|**Type the department or business unit where the contact works in the parent company or business.**|
|DisplayName|**Department**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`department`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the contact, such as an excerpt from the company's website.**|
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
|Description|**Select whether the contact accepts bulk email sent through marketing campaigns or quick campaigns. If Do Not Allow is selected, the contact can be added to marketing lists, but will be excluded from the email.**|
|DisplayName|**Do not allow Bulk Emails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotbulkemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotbulkemail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotBulkPostalMail"></a> DoNotBulkPostalMail

|Property|Value|
|---|---|
|Description|**Select whether the contact accepts bulk postal mail sent through marketing campaigns or quick campaigns. If Do Not Allow is selected, the contact can be added to marketing lists, but will be excluded from the letters.**|
|DisplayName|**Do not allow Bulk Mails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotbulkpostalmail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotbulkpostalmail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_DoNotEMail"></a> DoNotEMail

|Property|Value|
|---|---|
|Description|**Select whether the contact allows direct email sent from Microsoft Dynamics 365. If Do Not Allow is selected, Microsoft Dynamics 365 will not send the email.**|
|DisplayName|**Do not allow Emails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotemail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotFax"></a> DoNotFax

|Property|Value|
|---|---|
|Description|**Select whether the contact allows faxes. If Do Not Allow is selected, the contact will be excluded from any fax activities distributed in marketing campaigns.**|
|DisplayName|**Do not allow Faxes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotfax`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotfax`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotPhone"></a> DoNotPhone

|Property|Value|
|---|---|
|Description|**Select whether the contact accepts phone calls. If Do Not Allow is selected, the contact will be excluded from any phone call activities distributed in marketing campaigns.**|
|DisplayName|**Do not allow Phone Calls**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotphone`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotphone`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotPostalMail"></a> DoNotPostalMail

|Property|Value|
|---|---|
|Description|**Select whether the contact allows direct mail. If Do Not Allow is selected, the contact will be excluded from letter activities distributed in marketing campaigns.**|
|DisplayName|**Do not allow Mails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotpostalmail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotpostalmail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotSendMM"></a> DoNotSendMM

|Property|Value|
|---|---|
|Description|**Select whether the contact accepts marketing materials, such as brochures or catalogs. Contacts that opt out can be excluded from marketing initiatives.**|
|DisplayName|**Send Marketing Materials**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`donotsendmm`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_donotsendmm`|
|DefaultValue|False|
|True Label|Do Not Send|
|False Label|Send|

### <a name="BKMK_EducationCode"></a> EducationCode

|Property|Value|
|---|---|
|Description|**Select the contact's highest level of education for use in segmentation and analysis.**|
|DisplayName|**Education**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`educationcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`contact_educationcode`|

#### EducationCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_EMailAddress1"></a> EMailAddress1

|Property|Value|
|---|---|
|Description|**Type the primary email address for the contact.**|
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
|Description|**Type the secondary email address for the contact.**|
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
|Description|**Type an alternate email address for the contact.**|
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

### <a name="BKMK_EmployeeId"></a> EmployeeId

|Property|Value|
|---|---|
|Description|**Type the employee ID or number for the contact for reference in orders, service cases, or other communications with the contact's organization.**|
|DisplayName|**Employee**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`employeeid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

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

### <a name="BKMK_ExternalUserIdentifier"></a> ExternalUserIdentifier

|Property|Value|
|---|---|
|Description|**Identifier for an external user.**|
|DisplayName|**External User Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externaluseridentifier`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_FamilyStatusCode"></a> FamilyStatusCode

|Property|Value|
|---|---|
|Description|**Select the marital status of the contact for reference in follow-up phone calls and other communications.**|
|DisplayName|**Marital Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`familystatuscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_familystatuscode`|

#### FamilyStatusCode Choices/Options

|Value|Label|
|---|---|
|1|**Single**|
|2|**Married**|
|3|**Divorced**|
|4|**Widowed**|

### <a name="BKMK_Fax"></a> Fax

|Property|Value|
|---|---|
|Description|**Type the fax number for the contact.**|
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

### <a name="BKMK_FirstName"></a> FirstName

|Property|Value|
|---|---|
|Description|**Type the contact's first name to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.**|
|DisplayName|**First Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`firstname`|
|RequiredLevel|Recommended|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_FollowEmail"></a> FollowEmail

|Property|Value|
|---|---|
|Description|**Information about whether to allow following email activity like opens, attachment views and link clicks for emails sent to the contact.**|
|DisplayName|**Follow Email Activity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`followemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_followemail`|
|DefaultValue|True|
|True Label|Allow|
|False Label|Do Not Allow|

### <a name="BKMK_FtpSiteUrl"></a> FtpSiteUrl

|Property|Value|
|---|---|
|Description|**Type the URL for the contact's FTP site to enable users to access data and share documents.**|
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

### <a name="BKMK_GenderCode"></a> GenderCode

|Property|Value|
|---|---|
|Description|**Select the contact's gender to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.**|
|DisplayName|**Gender**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`gendercode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_gendercode`|

#### GenderCode Choices/Options

|Value|Label|
|---|---|
|1|**Male**|
|2|**Female**|

### <a name="BKMK_GovernmentId"></a> GovernmentId

|Property|Value|
|---|---|
|Description|**Type the passport number or other government ID for the contact for use in documents or reports.**|
|DisplayName|**Government**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`governmentid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_HasChildrenCode"></a> HasChildrenCode

|Property|Value|
|---|---|
|Description|**Select whether the contact has any children for reference in follow-up phone calls and other communications.**|
|DisplayName|**Has Children**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`haschildrencode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`contact_haschildrencode`|

#### HasChildrenCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Home2"></a> Home2

|Property|Value|
|---|---|
|Description|**Type a second home phone number for this contact.**|
|DisplayName|**Home Phone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`home2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

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

### <a name="BKMK_IsBackofficeCustomer"></a> IsBackofficeCustomer

|Property|Value|
|---|---|
|Description|**Select whether the contact exists in a separate accounting or other system, such as Microsoft Dynamics GP or another ERP database, for use in integration processes.**|
|DisplayName|**Back Office Customer**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isbackofficecustomer`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_isbackofficecustomer`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_JobTitle"></a> JobTitle

|Property|Value|
|---|---|
|Description|**Type the job title of the contact to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.**|
|DisplayName|**Job Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`jobtitle`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_LastName"></a> LastName

|Property|Value|
|---|---|
|Description|**Type the contact's last name to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.**|
|DisplayName|**Last Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

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
|Description|**Shows the date when the contact was last included in a marketing campaign or quick campaign.**|
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

### <a name="BKMK_LeadSourceCode"></a> LeadSourceCode

|Property|Value|
|---|---|
|Description|**Select the primary marketing source that directed the contact to your organization.**|
|DisplayName|**Lead Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`leadsourcecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`contact_leadsourcecode`|

#### LeadSourceCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_ManagerName"></a> ManagerName

|Property|Value|
|---|---|
|Description|**Type the name of the contact's manager for use in escalating issues or other follow-up communications with the contact.**|
|DisplayName|**Manager**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ManagerPhone"></a> ManagerPhone

|Property|Value|
|---|---|
|Description|**Type the phone number for the contact's manager.**|
|DisplayName|**Manager Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managerphone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

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
|GlobalChoiceName|`contact_marketingonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MiddleName"></a> MiddleName

|Property|Value|
|---|---|
|Description|**Type the contact's middle name or initial to make sure the contact is addressed correctly.**|
|DisplayName|**Middle Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`middlename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_MobilePhone"></a> MobilePhone

|Property|Value|
|---|---|
|Description|**Type the mobile phone number for the contact.**|
|DisplayName|**Mobile Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mobilephone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Phone|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_msa_managingpartnerid"></a> msa_managingpartnerid

|Property|Value|
|---|---|
|Description|**Unique identifier for Account associated with Contact.**|
|DisplayName|**Managing Partner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msa_managingpartnerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

### <a name="BKMK_msdyn_disablewebtracking"></a> msdyn_disablewebtracking

|Property|Value|
|---|---|
|Description|**Indicates that the contact has opted out of web tracking.**|
|DisplayName|**Disable Web Tracking**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_disablewebtracking`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_contact_msdyn_disablewebtracking`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_isminor"></a> msdyn_isminor

|Property|Value|
|---|---|
|Description|**Indicates that the contact is considered a minor in their jurisdiction.**|
|DisplayName|**Is Minor**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isminor`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_contact_msdyn_isminor`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_isminorwithparentalconsent"></a> msdyn_isminorwithparentalconsent

|Property|Value|
|---|---|
|Description|**Indicates that the contact is considered a minor in their jurisdiction and has parental consent.**|
|DisplayName|**Is Minor with Parental Consent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isminorwithparentalconsent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_contact_msdyn_isminorwithparentalconsent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_portaltermsagreementdate"></a> msdyn_portaltermsagreementdate

|Property|Value|
|---|---|
|Description|**Indicates the date and time that the person agreed to the portal terms and conditions.**|
|DisplayName|**Portal Terms Agreement Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_portaltermsagreementdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_mspp_userpreferredlcid"></a> mspp_userpreferredlcid

|Property|Value|
|---|---|
|Description|**User’s preferred portal language**|
|DisplayName|**Preferred Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_userpreferredlcid`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`powerpagelanguages`|

#### mspp_userpreferredlcid Choices/Options

|Value|Label|
|---|---|
|1025|**Arabic**|
|1026|**Bulgarian - Bulgaria**|
|1027|**Catalan - Catalan**|
|1028|**Chinese - Traditional**|
|1029|**Czech - Czech Republic**|
|1030|**Danish - Denmark**|
|1031|**German - Germany**|
|1032|**Greek - Greece**|
|1033|**English**|
|1035|**Finnish - Finland**|
|1036|**French - France**|
|1037|**Hebrew**|
|1038|**Hungarian - Hungary**|
|1040|**Italian - Italy**|
|1041|**Japanese - Japan**|
|1042|**Korean - Korea**|
|1043|**Dutch - Netherlands**|
|1044|**Norwegian (Bokmål) - Norway**|
|1045|**Polish - Poland**|
|1046|**Portuguese - Brazil**|
|1048|**Romanian - Romania**|
|1049|**Russian - Russia**|
|1050|**Croatian - Croatia**|
|1051|**Slovak - Slovakia**|
|1053|**Swedish - Sweden**|
|1054|**Thai - Thailand**|
|1055|**Turkish - Türkiye**|
|1057|**Indonesian - Indonesia**|
|1058|**Ukrainian - Ukraine**|
|1060|**Slovenian - Slovenia**|
|1061|**Estonian - Estonia**|
|1062|**Latvian - Latvia**|
|1063|**Lithuanian - Lithuania**|
|1066|**Vietnamese - Vietnam**|
|1069|**Basque - Basque**|
|1081|**Hindi - India**|
|1086|**Malay - Malaysia**|
|1087|**Kazakh - Kazakhstan**|
|1110|**Galician - Spain**|
|2052|**Chinese - China**|
|2070|**Portuguese - Portugal**|
|2074|**Serbian (Latin) - Serbia**|
|3076|**Chinese - Hong Kong SAR**|
|3082|**Spanish (Traditional Sort) - Spain**|
|3098|**Serbian (Cyrillic) - Serbia**|

### <a name="BKMK_NickName"></a> NickName

|Property|Value|
|---|---|
|Description|**Type the contact's nickname.**|
|DisplayName|**Nickname**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`nickname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_NumberOfChildren"></a> NumberOfChildren

|Property|Value|
|---|---|
|Description|**Type the number of children the contact has for reference in follow-up phone calls and other communications.**|
|DisplayName|**No. of Children**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`numberofchildren`|
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

### <a name="BKMK_Pager"></a> Pager

|Property|Value|
|---|---|
|Description|**Type the pager number for the contact.**|
|DisplayName|**Pager**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pager`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_ParentCustomerId"></a> ParentCustomerId

|Property|Value|
|---|---|
|Description|**Select the parent account or parent contact for the contact to provide a quick link to additional details, such as financial information, activities, and opportunities.**|
|DisplayName|**Company Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentcustomerid`|
|RequiredLevel|None|
|Type|Customer|
|Targets|account, contact|

### <a name="BKMK_ParentCustomerIdType"></a> ParentCustomerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Parent Customer Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentcustomeridtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ParticipatesInWorkflow"></a> ParticipatesInWorkflow

|Property|Value|
|---|---|
|Description|**Shows whether the contact participates in workflow rules.**|
|DisplayName|**Participates in Workflow**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`participatesinworkflow`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_participatesinworkflow`|
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
|GlobalChoiceName|`contact_paymenttermscode`|

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
|GlobalChoiceName|`contact_preferredappointmentdaycode`|

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
|DefaultFormValue|1|
|GlobalChoiceName|`contact_preferredappointmenttimecode`|

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
|GlobalChoiceName|`contact_preferredcontactmethodcode`|

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
|Description|**Choose the regular or preferred customer service representative for reference when scheduling service activities for the contact.**|
|DisplayName|**Preferred User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredsystemuserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_Salutation"></a> Salutation

|Property|Value|
|---|---|
|Description|**Type the salutation of the contact to make sure the contact is addressed correctly in sales calls, email messages, and marketing campaigns.**|
|DisplayName|**Salutation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`salutation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|DefaultFormValue|1|
|GlobalChoiceName|`contact_shippingmethodcode`|

#### ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Choose the service level agreement (SLA) that you want to apply to the Contact record.**|
|DisplayName|**SLA**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slaid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_SpousesName"></a> SpousesName

|Property|Value|
|---|---|
|Description|**Type the name of the contact's spouse or partner for reference during calls, events, or other communications with the contact.**|
|DisplayName|**Spouse/Partner Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`spousesname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|Description|**Shows whether the contact is active or inactive. Inactive contacts are read-only and can't be edited unless they are reactivated.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`contact_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the contact's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`contact_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Subscription**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`subscriptionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Suffix"></a> Suffix

|Property|Value|
|---|---|
|Description|**Type the suffix used in the contact's name, such as Jr. or Sr. to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns.**|
|DisplayName|**Suffix**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`suffix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_Telephone1"></a> Telephone1

|Property|Value|
|---|---|
|Description|**Type the main phone number for this contact.**|
|DisplayName|**Business Phone**|
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
|Description|**Type a second phone number for this contact.**|
|DisplayName|**Home Phone**|
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
|Description|**Type a third phone number for this contact.**|
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
|Description|**Select a region or territory for the contact for use in segmentation and analysis.**|
|DisplayName|**Territory**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`territorycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`contact_territorycode`|

#### TerritoryCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

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

### <a name="BKMK_WebSiteUrl"></a> WebSiteUrl

|Property|Value|
|---|---|
|Description|**Type the contact's professional or personal website or blog URL.**|
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

### <a name="BKMK_YomiFirstName"></a> YomiFirstName

|Property|Value|
|---|---|
|Description|**Type the phonetic spelling of the contact's first name, if the name is specified in Japanese, to make sure the name is pronounced correctly in phone calls with the contact.**|
|DisplayName|**Yomi First Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yomifirstname`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_YomiLastName"></a> YomiLastName

|Property|Value|
|---|---|
|Description|**Type the phonetic spelling of the contact's last name, if the name is specified in Japanese, to make sure the name is pronounced correctly in phone calls with the contact.**|
|DisplayName|**Yomi Last Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yomilastname`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_YomiMiddleName"></a> YomiMiddleName

|Property|Value|
|---|---|
|Description|**Type the phonetic spelling of the contact's middle name, if the name is specified in Japanese, to make sure the name is pronounced correctly in phone calls with the contact.**|
|DisplayName|**Yomi Middle Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yomimiddlename`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|150|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AccountId](#BKMK_AccountId)
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
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreditLimit_Base](#BKMK_CreditLimit_Base)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FullName](#BKMK_FullName)
- [IsAutoCreate](#BKMK_IsAutoCreate)
- [IsPrivate](#BKMK_IsPrivate)
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
- [ParentContactId](#BKMK_ParentContactId)
- [ParentCustomerIdName](#BKMK_ParentCustomerIdName)
- [ParentCustomerIdYomiName](#BKMK_ParentCustomerIdYomiName)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [TimeSpentByMeOnEmailAndMeetings](#BKMK_TimeSpentByMeOnEmailAndMeetings)
- [VersionNumber](#BKMK_VersionNumber)
- [YomiFullName](#BKMK_YomiFullName)

### <a name="BKMK_AccountId"></a> AccountId

|Property|Value|
|---|---|
|Description|**Unique identifier of the account with which the contact is associated.**|
|DisplayName|**Account**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`accountid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

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

### <a name="BKMK_Address3_Composite"></a> Address3_Composite

|Property|Value|
|---|---|
|Description|**Shows the complete third address.**|
|DisplayName|**Address 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address3_composite`|
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
|Description|**Shows the Aging 30 field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.**|
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
|Description|**Shows the Aging 60 field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.**|
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
|Description|**Shows the Aging 90 field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.**|
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

### <a name="BKMK_AnnualIncome_Base"></a> AnnualIncome_Base

|Property|Value|
|---|---|
|Description|**Shows the Annual Income field converted to the system's default base currency. The calculations use the exchange rate specified in the Currencies area.**|
|DisplayName|**Annual Income (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`annualincome_base`|
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
|Description|**Shows the Credit Limit field converted to the system's default base currency for reporting purposes. The calculations use the exchange rate specified in the Currencies area.**|
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
|ImeMode|Auto|
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

### <a name="BKMK_FullName"></a> FullName

|Property|Value|
|---|---|
|Description|**Combines and shows the contact's first and last names so that the full name can be displayed in views and reports.**|
|DisplayName|**Full Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fullname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_IsAutoCreate"></a> IsAutoCreate

|Property|Value|
|---|---|
|Description|**Information about whether the contact was auto-created when promoting an email or an appointment.**|
|DisplayName|**Auto-created**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`isautocreate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_isautocreate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|GlobalChoiceName|`contact_isprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MasterId"></a> MasterId

|Property|Value|
|---|---|
|Description|**Unique identifier of the master contact for merge.**|
|DisplayName|**Master ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`masterid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_Merged"></a> Merged

|Property|Value|
|---|---|
|Description|**Shows whether the account has been merged with a master contact.**|
|DisplayName|**Merged**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`merged`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`contact_merged`|
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
|Description|**Shows who last updated the record on behalf of another user.**|
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
|Description|**Unique identifier of the business unit that owns the contact.**|
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
|Description|**Unique identifier of the team who owns the contact.**|
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
|Description|**Unique identifier of the user who owns the contact.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ParentContactId"></a> ParentContactId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent contact.**|
|DisplayName|**Parent Contact**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentcontactid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_ParentCustomerIdName"></a> ParentCustomerIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentcustomeridname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_ParentCustomerIdYomiName"></a> ParentCustomerIdYomiName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentcustomeridyominame`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|450|

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
|Description|**Total time spent for emails (read and write) and meetings by me in relation to the contact record.**|
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
|Description|**Version number of the contact.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_YomiFullName"></a> YomiFullName

|Property|Value|
|---|---|
|Description|**Shows the combined Yomi first and last names of the contact so that the full phonetic name can be displayed in views and reports.**|
|DisplayName|**Yomi Full Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yomifullname`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|450|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_contacts](#BKMK_business_unit_contacts)
- [contact_customer_accounts](#BKMK_contact_customer_accounts)
- [contact_customer_contacts](#BKMK_contact_customer_contacts-many-to-one)
- [contact_master_contact](#BKMK_contact_master_contact-many-to-one)
- [contact_owning_user](#BKMK_contact_owning_user)
- [lk_contact_createdonbehalfby](#BKMK_lk_contact_createdonbehalfby)
- [lk_contact_modifiedonbehalfby](#BKMK_lk_contact_modifiedonbehalfby)
- [lk_contactbase_createdby](#BKMK_lk_contactbase_createdby)
- [lk_contactbase_modifiedby](#BKMK_lk_contactbase_modifiedby)
- [manualsla_contact](#BKMK_manualsla_contact)
- [msa_contact_managingpartner](#BKMK_msa_contact_managingpartner)
- [owner_contacts](#BKMK_owner_contacts)
- [processstage_contact](#BKMK_processstage_contact)
- [sla_contact](#BKMK_sla_contact)
- [system_user_contacts](#BKMK_system_user_contacts)
- [team_contacts](#BKMK_team_contacts)
- [transactioncurrency_contact](#BKMK_transactioncurrency_contact)

### <a name="BKMK_business_unit_contacts"></a> business_unit_contacts

One-To-Many Relationship: [businessunit business_unit_contacts](businessunit.md#BKMK_business_unit_contacts)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_customer_accounts"></a> contact_customer_accounts

One-To-Many Relationship: [account contact_customer_accounts](account.md#BKMK_contact_customer_accounts)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`parentcustomerid`|
|ReferencingEntityNavigationPropertyName|`parentcustomerid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_contact_customer_contacts-many-to-one"></a> contact_customer_contacts

One-To-Many Relationship: [contact contact_customer_contacts](#BKMK_contact_customer_contacts-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`parentcustomerid`|
|ReferencingEntityNavigationPropertyName|`parentcustomerid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_contact_master_contact-many-to-one"></a> contact_master_contact

One-To-Many Relationship: [contact contact_master_contact](#BKMK_contact_master_contact-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`masterid`|
|ReferencingEntityNavigationPropertyName|`masterid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_owning_user"></a> contact_owning_user

One-To-Many Relationship: [systemuser contact_owning_user](systemuser.md#BKMK_contact_owning_user)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_contact_createdonbehalfby"></a> lk_contact_createdonbehalfby

One-To-Many Relationship: [systemuser lk_contact_createdonbehalfby](systemuser.md#BKMK_lk_contact_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_contact_modifiedonbehalfby"></a> lk_contact_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_contact_modifiedonbehalfby](systemuser.md#BKMK_lk_contact_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_contactbase_createdby"></a> lk_contactbase_createdby

One-To-Many Relationship: [systemuser lk_contactbase_createdby](systemuser.md#BKMK_lk_contactbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_contactbase_modifiedby"></a> lk_contactbase_modifiedby

One-To-Many Relationship: [systemuser lk_contactbase_modifiedby](systemuser.md#BKMK_lk_contactbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_manualsla_contact"></a> manualsla_contact

One-To-Many Relationship: [sla manualsla_contact](sla.md#BKMK_manualsla_contact)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slaid`|
|ReferencingEntityNavigationPropertyName|`sla_contact_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msa_contact_managingpartner"></a> msa_contact_managingpartner

One-To-Many Relationship: [account msa_contact_managingpartner](account.md#BKMK_msa_contact_managingpartner)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`msa_managingpartnerid`|
|ReferencingEntityNavigationPropertyName|`msa_managingpartnerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_contacts"></a> owner_contacts

One-To-Many Relationship: [owner owner_contacts](owner.md#BKMK_owner_contacts)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_contact"></a> processstage_contact

One-To-Many Relationship: [processstage processstage_contact](processstage.md#BKMK_processstage_contact)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sla_contact"></a> sla_contact

One-To-Many Relationship: [sla sla_contact](sla.md#BKMK_sla_contact)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slainvokedid`|
|ReferencingEntityNavigationPropertyName|`slainvokedid_contact_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_system_user_contacts"></a> system_user_contacts

One-To-Many Relationship: [systemuser system_user_contacts](systemuser.md#BKMK_system_user_contacts)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`preferredsystemuserid`|
|ReferencingEntityNavigationPropertyName|`preferredsystemuserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_contacts"></a> team_contacts

One-To-Many Relationship: [team team_contacts](team.md#BKMK_team_contacts)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_contact"></a> transactioncurrency_contact

One-To-Many Relationship: [transactioncurrency transactioncurrency_contact](transactioncurrency.md#BKMK_transactioncurrency_contact)

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

- [account_primary_contact](#BKMK_account_primary_contact)
- [adx_contact_externalidentity](#BKMK_adx_contact_externalidentity)
- [adx_invitation_invitecontact](#BKMK_adx_invitation_invitecontact)
- [adx_invitation_invitercontact](#BKMK_adx_invitation_invitercontact)
- [adx_invitation_redeemedContact](#BKMK_adx_invitation_redeemedContact)
- [adx_webformsession_contact](#BKMK_adx_webformsession_contact)
- [contact_actioncard](#BKMK_contact_actioncard)
- [contact_activity_parties](#BKMK_contact_activity_parties)
- [Contact_ActivityPointers](#BKMK_Contact_ActivityPointers)
- [contact_adx_inviteredemptions](#BKMK_contact_adx_inviteredemptions)
- [contact_adx_portalcomments](#BKMK_contact_adx_portalcomments)
- [Contact_Annotation](#BKMK_Contact_Annotation)
- [Contact_Appointments](#BKMK_Contact_Appointments)
- [Contact_AsyncOperations](#BKMK_Contact_AsyncOperations)
- [Contact_BulkDeleteFailures](#BKMK_Contact_BulkDeleteFailures)
- [contact_chats](#BKMK_contact_chats)
- [contact_connections1](#BKMK_contact_connections1)
- [contact_connections2](#BKMK_contact_connections2)
- [contact_customer_contacts](#BKMK_contact_customer_contacts-one-to-many)
- [Contact_CustomerAddress](#BKMK_Contact_CustomerAddress)
- [Contact_DuplicateBaseRecord](#BKMK_Contact_DuplicateBaseRecord)
- [Contact_DuplicateMatchingRecord](#BKMK_Contact_DuplicateMatchingRecord)
- [Contact_Email_EmailSender](#BKMK_Contact_Email_EmailSender)
- [Contact_Emails](#BKMK_Contact_Emails)
- [Contact_Faxes](#BKMK_Contact_Faxes)
- [Contact_Feedback](#BKMK_Contact_Feedback)
- [Contact_Letters](#BKMK_Contact_Letters)
- [Contact_MailboxTrackingFolder](#BKMK_Contact_MailboxTrackingFolder)
- [contact_master_contact](#BKMK_contact_master_contact-one-to-many)
- [Contact_Phonecalls](#BKMK_Contact_Phonecalls)
- [contact_PostFollows](#BKMK_contact_PostFollows)
- [contact_PostRegardings](#BKMK_contact_PostRegardings)
- [contact_principalobjectattributeaccess](#BKMK_contact_principalobjectattributeaccess)
- [Contact_ProcessSessions](#BKMK_Contact_ProcessSessions)
- [Contact_RecurringAppointmentMasters](#BKMK_Contact_RecurringAppointmentMasters)
- [Contact_SocialActivities](#BKMK_Contact_SocialActivities)
- [Contact_SyncErrors](#BKMK_Contact_SyncErrors)
- [Contact_Tasks](#BKMK_Contact_Tasks)
- [lk_contact_feedback_createdby](#BKMK_lk_contact_feedback_createdby)
- [lk_contact_feedback_createdonbehalfby](#BKMK_lk_contact_feedback_createdonbehalfby)
- [PowerPagesSiteAIFeedback_Contact_Contact](#BKMK_PowerPagesSiteAIFeedback_Contact_Contact)
- [slakpiinstance_contact](#BKMK_slakpiinstance_contact)
- [socialactivity_postauthor_contacts](#BKMK_socialactivity_postauthor_contacts)
- [socialactivity_postauthoraccount_contacts](#BKMK_socialactivity_postauthoraccount_contacts)
- [Socialprofile_customer_contacts](#BKMK_Socialprofile_customer_contacts)

### <a name="BKMK_account_primary_contact"></a> account_primary_contact

Many-To-One Relationship: [account account_primary_contact](account.md#BKMK_account_primary_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`primarycontactid`|
|ReferencedEntityNavigationPropertyName|`account_primary_contact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_contact_externalidentity"></a> adx_contact_externalidentity

Many-To-One Relationship: [adx_externalidentity adx_contact_externalidentity](adx_externalidentity.md#BKMK_adx_contact_externalidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_externalidentity`|
|ReferencingAttribute|`adx_contactid`|
|ReferencedEntityNavigationPropertyName|`adx_contact_externalidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_invitecontact"></a> adx_invitation_invitecontact

Many-To-One Relationship: [adx_invitation adx_invitation_invitecontact](adx_invitation.md#BKMK_adx_invitation_invitecontact)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`adx_invitecontact`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_invitecontact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_invitercontact"></a> adx_invitation_invitercontact

Many-To-One Relationship: [adx_invitation adx_invitation_invitercontact](adx_invitation.md#BKMK_adx_invitation_invitercontact)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`adx_invitercontact`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_invitercontact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_redeemedContact"></a> adx_invitation_redeemedContact

Many-To-One Relationship: [adx_invitation adx_invitation_redeemedContact](adx_invitation.md#BKMK_adx_invitation_redeemedContact)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`adx_redeemedcontact`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_redeemedContact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_webformsession_contact"></a> adx_webformsession_contact

Many-To-One Relationship: [adx_webformsession adx_webformsession_contact](adx_webformsession.md#BKMK_adx_webformsession_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_webformsession`|
|ReferencingAttribute|`adx_contact`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_contact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_actioncard"></a> contact_actioncard

Many-To-One Relationship: [actioncard contact_actioncard](actioncard.md#BKMK_contact_actioncard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`contact_actioncard`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_activity_parties"></a> contact_activity_parties

Many-To-One Relationship: [activityparty contact_activity_parties](activityparty.md#BKMK_contact_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`partyid`|
|ReferencedEntityNavigationPropertyName|`contact_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_ActivityPointers"></a> Contact_ActivityPointers

Many-To-One Relationship: [activitypointer Contact_ActivityPointers](activitypointer.md#BKMK_Contact_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_ActivityPointers`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 20<br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_contact_adx_inviteredemptions"></a> contact_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption contact_adx_inviteredemptions](adx_inviteredemption.md#BKMK_contact_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`contact_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_contact_adx_portalcomments"></a> contact_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment contact_adx_portalcomments](adx_portalcomment.md#BKMK_contact_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`contact_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_Contact_Annotation"></a> Contact_Annotation

Many-To-One Relationship: [annotation Contact_Annotation](annotation.md#BKMK_Contact_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Appointments"></a> Contact_Appointments

Many-To-One Relationship: [appointment Contact_Appointments](appointment.md#BKMK_Contact_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_AsyncOperations"></a> Contact_AsyncOperations

Many-To-One Relationship: [asyncoperation Contact_AsyncOperations](asyncoperation.md#BKMK_Contact_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_BulkDeleteFailures"></a> Contact_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Contact_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Contact_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_chats"></a> contact_chats

Many-To-One Relationship: [chat contact_chats](chat.md#BKMK_contact_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`contact_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RollupRelatedByParty`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_contact_connections1"></a> contact_connections1

Many-To-One Relationship: [connection contact_connections1](connection.md#BKMK_contact_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`contact_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_connections2"></a> contact_connections2

Many-To-One Relationship: [connection contact_connections2](connection.md#BKMK_contact_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`contact_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_customer_contacts-one-to-many"></a> contact_customer_contacts

Many-To-One Relationship: [contact contact_customer_contacts](#BKMK_contact_customer_contacts-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`parentcustomerid`|
|ReferencedEntityNavigationPropertyName|`contact_customer_contacts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 40<br />QueryApi: `CRMContact.RetrieveSubContacts`<br />ViewId: `00000000-0000-0000-00aa-000010001210`|

### <a name="BKMK_Contact_CustomerAddress"></a> Contact_CustomerAddress

Many-To-One Relationship: [customeraddress Contact_CustomerAddress](customeraddress.md#BKMK_Contact_CustomerAddress)

|Property|Value|
|---|---|
|ReferencingEntity|`customeraddress`|
|ReferencingAttribute|`parentid`|
|ReferencedEntityNavigationPropertyName|`Contact_CustomerAddress`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10<br />QueryApi: null<br />ViewId: `03315b35-4585-4447-a4d2-059cf79ca0fd`|

### <a name="BKMK_Contact_DuplicateBaseRecord"></a> Contact_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Contact_DuplicateBaseRecord](duplicaterecord.md#BKMK_Contact_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Contact_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_DuplicateMatchingRecord"></a> Contact_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Contact_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Contact_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Contact_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Email_EmailSender"></a> Contact_Email_EmailSender

Many-To-One Relationship: [email Contact_Email_EmailSender](email.md#BKMK_Contact_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`emailsender`|
|ReferencedEntityNavigationPropertyName|`Contact_Email_EmailSender`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Emails"></a> Contact_Emails

Many-To-One Relationship: [email Contact_Emails](email.md#BKMK_Contact_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Faxes"></a> Contact_Faxes

Many-To-One Relationship: [fax Contact_Faxes](fax.md#BKMK_Contact_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Feedback"></a> Contact_Feedback

Many-To-One Relationship: [feedback Contact_Feedback](feedback.md#BKMK_Contact_Feedback)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Feedback`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 150<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Letters"></a> Contact_Letters

Many-To-One Relationship: [letter Contact_Letters](letter.md#BKMK_Contact_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_MailboxTrackingFolder"></a> Contact_MailboxTrackingFolder

Many-To-One Relationship: [mailboxtrackingfolder Contact_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Contact_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_MailboxTrackingFolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_master_contact-one-to-many"></a> contact_master_contact

Many-To-One Relationship: [contact contact_master_contact](#BKMK_contact_master_contact-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`masterid`|
|ReferencedEntityNavigationPropertyName|`contact_master_contact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Phonecalls"></a> Contact_Phonecalls

Many-To-One Relationship: [phonecall Contact_Phonecalls](phonecall.md#BKMK_Contact_Phonecalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Phonecalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_PostFollows"></a> contact_PostFollows

Many-To-One Relationship: [postfollow contact_PostFollows](postfollow.md#BKMK_contact_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`contact_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_PostRegardings"></a> contact_PostRegardings

Many-To-One Relationship: [postregarding contact_PostRegardings](postregarding.md#BKMK_contact_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`contact_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_contact_principalobjectattributeaccess"></a> contact_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess contact_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_contact_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`contact_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_ProcessSessions"></a> Contact_ProcessSessions

Many-To-One Relationship: [processsession Contact_ProcessSessions](processsession.md#BKMK_Contact_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_RecurringAppointmentMasters"></a> Contact_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster Contact_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_Contact_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_SocialActivities"></a> Contact_SocialActivities

Many-To-One Relationship: [socialactivity Contact_SocialActivities](socialactivity.md#BKMK_Contact_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_SyncErrors"></a> Contact_SyncErrors

Many-To-One Relationship: [syncerror Contact_SyncErrors](syncerror.md#BKMK_Contact_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Contact_Tasks"></a> Contact_Tasks

Many-To-One Relationship: [task Contact_Tasks](task.md#BKMK_Contact_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Contact_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_contact_feedback_createdby"></a> lk_contact_feedback_createdby

Many-To-One Relationship: [feedback lk_contact_feedback_createdby](feedback.md#BKMK_lk_contact_feedback_createdby)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`createdbycontact`|
|ReferencedEntityNavigationPropertyName|`lk_contact_feedback_createdby`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_contact_feedback_createdonbehalfby"></a> lk_contact_feedback_createdonbehalfby

Many-To-One Relationship: [feedback lk_contact_feedback_createdonbehalfby](feedback.md#BKMK_lk_contact_feedback_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`createdonbehalfbycontact`|
|ReferencedEntityNavigationPropertyName|`lk_contact_feedback_createdonbehalfby`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_PowerPagesSiteAIFeedback_Contact_Contact"></a> PowerPagesSiteAIFeedback_Contact_Contact

Many-To-One Relationship: [powerpagessiteaifeedback PowerPagesSiteAIFeedback_Contact_Contact](powerpagessiteaifeedback.md#BKMK_PowerPagesSiteAIFeedback_Contact_Contact)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagessiteaifeedback`|
|ReferencingAttribute|`contact`|
|ReferencedEntityNavigationPropertyName|`PowerPagesSiteAIFeedback_Contact_Contact`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slakpiinstance_contact"></a> slakpiinstance_contact

Many-To-One Relationship: [slakpiinstance slakpiinstance_contact](slakpiinstance.md#BKMK_slakpiinstance_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`slakpiinstance_contact`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_socialactivity_postauthor_contacts"></a> socialactivity_postauthor_contacts

Many-To-One Relationship: [socialactivity socialactivity_postauthor_contacts](socialactivity.md#BKMK_socialactivity_postauthor_contacts)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`postauthor`|
|ReferencedEntityNavigationPropertyName|`socialactivity_postauthor_contacts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_socialactivity_postauthoraccount_contacts"></a> socialactivity_postauthoraccount_contacts

Many-To-One Relationship: [socialactivity socialactivity_postauthoraccount_contacts](socialactivity.md#BKMK_socialactivity_postauthoraccount_contacts)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`postauthoraccount`|
|ReferencedEntityNavigationPropertyName|`socialactivity_postauthoraccount_contacts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Socialprofile_customer_contacts"></a> Socialprofile_customer_contacts

Many-To-One Relationship: [socialprofile Socialprofile_customer_contacts](socialprofile.md#BKMK_Socialprofile_customer_contacts)

|Property|Value|
|---|---|
|ReferencingEntity|`socialprofile`|
|ReferencingAttribute|`customerid`|
|ReferencedEntityNavigationPropertyName|`Socialprofile_customer_contacts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 40<br />QueryApi: null<br />ViewId: `ff0f8b49-e2cd-45f1-b878-cbd99aa4ac56`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [adx_invitation_invitecontacts](#BKMK_adx_invitation_invitecontacts)
- [adx_invitation_redeemedcontacts](#BKMK_adx_invitation_redeemedcontacts)
- [powerpagecomponent_mspp_webrole_contact](#BKMK_powerpagecomponent_mspp_webrole_contact)

### <a name="BKMK_adx_invitation_invitecontacts"></a> adx_invitation_invitecontacts

See [adx_invitation adx_invitation_invitecontacts Many-To-Many Relationship](adx_invitation.md#BKMK_adx_invitation_invitecontacts)

|Property|Value|
|---|---|
|IntersectEntityName|`adx_invitation_invitecontacts`|
|IsCustomizable|True|
|SchemaName|`adx_invitation_invitecontacts`|
|IntersectAttribute|`contactid`|
|NavigationPropertyName|`adx_invitation_invitecontacts`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Invite Contacts<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_redeemedcontacts"></a> adx_invitation_redeemedcontacts

See [adx_invitation adx_invitation_redeemedcontacts Many-To-Many Relationship](adx_invitation.md#BKMK_adx_invitation_redeemedcontacts)

|Property|Value|
|---|---|
|IntersectEntityName|`adx_invitation_redeemedcontacts`|
|IsCustomizable|True|
|SchemaName|`adx_invitation_redeemedcontacts`|
|IntersectAttribute|`contactid`|
|NavigationPropertyName|`adx_invitation_redeemedcontacts`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Redeemed Contacts<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_mspp_webrole_contact"></a> powerpagecomponent_mspp_webrole_contact

See [powerpagecomponent powerpagecomponent_mspp_webrole_contact Many-To-Many Relationship](powerpagecomponent.md#BKMK_powerpagecomponent_mspp_webrole_contact)

|Property|Value|
|---|---|
|IntersectEntityName|`powerpagecomponent_mspp_webrole_contact`|
|IsCustomizable|True|
|SchemaName|`powerpagecomponent_mspp_webrole_contact`|
|IntersectAttribute|`contactid`|
|NavigationPropertyName|`powerpagecomponent_mspp_webrole_contact`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100300<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.contact?displayProperty=fullName>
