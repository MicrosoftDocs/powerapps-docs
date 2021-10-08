---
title: "User (SystemUser) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the User (SystemUser) table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# User (SystemUser) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Person with access to the Microsoft CRM system and who owns objects in the Microsoft CRM database.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/systemusers<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/systemusers(*systemuserid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|ReassignObjectsSystemUser|<xref href="Microsoft.Dynamics.CRM.ReassignObjectsSystemUser?text=ReassignObjectsSystemUser Action" />|<xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsSystemUserRequest>|
|RemoveParent|<xref href="Microsoft.Dynamics.CRM.RemoveParent?text=RemoveParent Action" />|<xref:Microsoft.Crm.Sdk.Messages.RemoveParentRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/systemusers(*systemuserid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveAllChildUsersSystemUser|<xref href="Microsoft.Dynamics.CRM.RetrieveAllChildUsersSystemUser?text=RetrieveAllChildUsersSystemUser Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAllChildUsersSystemUserRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/systemusers<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetBusinessSystemUser|<xref href="Microsoft.Dynamics.CRM.SetBusinessSystemUser?text=SetBusinessSystemUser Action" />|<xref:Microsoft.Crm.Sdk.Messages.SetBusinessSystemUserRequest>|
|SetParentBusinessUnit|[Associate and disassociate entities](/powerapps/developer/common-data-service/webapi/associate-disassociate-entities-using-web-api)|<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|
|SetParentSystemUser|<xref href="Microsoft.Dynamics.CRM.SetParentSystemUser?text=SetParentSystemUser Action" />|<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|
|SetParentTeam|[Associate and disassociate entities](/powerapps/developer/common-data-service/webapi/associate-disassociate-entities-using-web-api)|<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/systemusers(*systemuserid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/systemusers(*systemuserid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SystemUsers|
|DisplayCollectionName|Users|
|DisplayName|User|
|EntitySetName|systemusers|
|IsBPFEntity|False|
|LogicalCollectionName|systemusers|
|LogicalName|systemuser|
|OwnershipType|BusinessOwned|
|PrimaryIdAttribute|systemuserid|
|PrimaryNameAttribute|fullname|
|SchemaName|SystemUser|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessMode](#BKMK_AccessMode)
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
- [ApplicationId](#BKMK_ApplicationId)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CalendarId](#BKMK_CalendarId)
- [CALType](#BKMK_CALType)
- [DisplayInServiceViews](#BKMK_DisplayInServiceViews)
- [DomainName](#BKMK_DomainName)
- [EmailRouterAccessApproval](#BKMK_EmailRouterAccessApproval)
- [EmployeeId](#BKMK_EmployeeId)
- [EntityImage](#BKMK_EntityImage)
- [FirstName](#BKMK_FirstName)
- [GovernmentId](#BKMK_GovernmentId)
- [HomePhone](#BKMK_HomePhone)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IncomingEmailDeliveryMethod](#BKMK_IncomingEmailDeliveryMethod)
- [InternalEMailAddress](#BKMK_InternalEMailAddress)
- [InviteStatusCode](#BKMK_InviteStatusCode)
- [IsDisabled](#BKMK_IsDisabled)
- [IsIntegrationUser](#BKMK_IsIntegrationUser)
- [IsLicensed](#BKMK_IsLicensed)
- [IsSyncWithDirectory](#BKMK_IsSyncWithDirectory)
- [JobTitle](#BKMK_JobTitle)
- [LastName](#BKMK_LastName)
- [MiddleName](#BKMK_MiddleName)
- [MobileAlertEMail](#BKMK_MobileAlertEMail)
- [MobileOfflineProfileId](#BKMK_MobileOfflineProfileId)
- [MobileOfflineProfileIdName](#BKMK_MobileOfflineProfileIdName)
- [MobilePhone](#BKMK_MobilePhone)
- [NickName](#BKMK_NickName)
- [OutgoingEmailDeliveryMethod](#BKMK_OutgoingEmailDeliveryMethod)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentSystemUserId](#BKMK_ParentSystemUserId)
- [PassportHi](#BKMK_PassportHi)
- [PassportLo](#BKMK_PassportLo)
- [PersonalEMailAddress](#BKMK_PersonalEMailAddress)
- [PhotoUrl](#BKMK_PhotoUrl)
- [PositionId](#BKMK_PositionId)
- [PreferredAddressCode](#BKMK_PreferredAddressCode)
- [PreferredEmailCode](#BKMK_PreferredEmailCode)
- [PreferredPhoneCode](#BKMK_PreferredPhoneCode)
- [ProcessId](#BKMK_ProcessId)
- [QueueId](#BKMK_QueueId)
- [Salutation](#BKMK_Salutation)
- [SetupUser](#BKMK_SetupUser)
- [SharePointEmailAddress](#BKMK_SharePointEmailAddress)
- [Skills](#BKMK_Skills)
- [StageId](#BKMK_StageId)
- [SystemUserId](#BKMK_SystemUserId)
- [TerritoryId](#BKMK_TerritoryId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UserLicenseType](#BKMK_UserLicenseType)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WindowsLiveID](#BKMK_WindowsLiveID)
- [YammerEmailAddress](#BKMK_YammerEmailAddress)
- [YammerUserId](#BKMK_YammerUserId)
- [YomiFirstName](#BKMK_YomiFirstName)
- [YomiLastName](#BKMK_YomiLastName)
- [YomiMiddleName](#BKMK_YomiMiddleName)


### <a name="BKMK_AccessMode"></a> AccessMode

|Property|Value|
|--------|-----|
|Description|Type of user.|
|DisplayName|Access Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|accessmode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### AccessMode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Read-Write||
|1|Administrative||
|2|Read||
|3|Support User||
|4|Non-interactive||
|5|Delegated Admin||



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
|IsValidForForm|False|
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
|DisplayName|City|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_city|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Country"></a> Address1_Country

|Property|Value|
|--------|-----|
|Description|Country/region name in address 1.|
|DisplayName|Country/Region|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_country|
|MaxLength|128|
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
|MaxLength|128|
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
|MaxLength|64|
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
|DisplayName|Street 1|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_line1|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Line2"></a> Address1_Line2

|Property|Value|
|--------|-----|
|Description|Second line for entering address 1 information.|
|DisplayName|Street 2|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_line2|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Line3"></a> Address1_Line3

|Property|Value|
|--------|-----|
|Description|Third line for entering address 1 information.|
|DisplayName|Street 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_line3|
|MaxLength|1024|
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
|DisplayName|ZIP/Postal Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_postalcode|
|MaxLength|40|
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
|MaxLength|40|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Method of shipment for address 1.|
|DisplayName|Address 1: Shipping Method|
|IsValidForForm|False|
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
|DisplayName|State/Province|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_stateorprovince|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Telephone1"></a> Address1_Telephone1

|Property|Value|
|--------|-----|
|Description|First telephone number associated with address 1.|
|DisplayName|Main Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address1_telephone1|
|MaxLength|64|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address1_Telephone2"></a> Address1_Telephone2

|Property|Value|
|--------|-----|
|Description|Second telephone number associated with address 1.|
|DisplayName|Other Phone|
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
|Description|Third telephone number associated with address 1.|
|DisplayName|Pager|
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
|Description|United Parcel Service (UPS) zone for address 1.|
|DisplayName|Address 1: UPS Zone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
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
|IsValidForForm|False|
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
|IsValidForForm|False|
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
|DisplayName|Other City|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_city|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Country"></a> Address2_Country

|Property|Value|
|--------|-----|
|Description|Country/region name in address 2.|
|DisplayName|Other Country/Region|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_country|
|MaxLength|128|
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
|MaxLength|128|
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
|DisplayName|Other Street 1|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_line1|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Line2"></a> Address2_Line2

|Property|Value|
|--------|-----|
|Description|Second line for entering address 2 information.|
|DisplayName|Other Street 2|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_line2|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Line3"></a> Address2_Line3

|Property|Value|
|--------|-----|
|Description|Third line for entering address 2 information.|
|DisplayName|Other Street 3|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_line3|
|MaxLength|1024|
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
|DisplayName|Other ZIP/Postal Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_postalcode|
|MaxLength|40|
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
|MaxLength|40|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

|Property|Value|
|--------|-----|
|Description|Method of shipment for address 2.|
|DisplayName|Address 2: Shipping Method|
|IsValidForForm|False|
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
|DisplayName|Other State/Province|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_stateorprovince|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Address2_Telephone1"></a> Address2_Telephone1

|Property|Value|
|--------|-----|
|Description|First telephone number associated with address 2.|
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
|Description|Second telephone number associated with address 2.|
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
|Description|Third telephone number associated with address 2.|
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
|Description|United Parcel Service (UPS) zone for address 2.|
|DisplayName|Address 2: UPS Zone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|address2_utcoffset|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ApplicationId"></a> ApplicationId

|Property|Value|
|--------|-----|
|Description|The identifier for the application. This is used to access data in another application.|
|DisplayName|Application ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|applicationid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the user is associated.|
|DisplayName|Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|SystemRequired|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_CalendarId"></a> CalendarId

|Property|Value|
|--------|-----|
|Description|Fiscal calendar associated with the user.|
|DisplayName|Calendar|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|calendarid|
|RequiredLevel|None|
|Targets|calendar|
|Type|Lookup|


### <a name="BKMK_CALType"></a> CALType

|Property|Value|
|--------|-----|
|Description|License type of user. This is used only in the on-premises version of the product. Online licenses are managed through Microsoft 365 Office Portal|
|DisplayName|License Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|caltype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### CALType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Professional||
|1|Administrative||
|2|Basic||
|3|Device Professional||
|4|Device Basic||
|5|Essential||
|6|Device Essential||
|7|Enterprise||
|8|Device Enterprise||
|9|Sales||
|10|Service||
|11|Field Service||
|12|Project Service||



### <a name="BKMK_DisplayInServiceViews"></a> DisplayInServiceViews

|Property|Value|
|--------|-----|
|Description|Whether to display the user in service views.|
|DisplayName|Display in Service Views|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|displayinserviceviews|
|RequiredLevel|None|
|Type|Boolean|

#### DisplayInServiceViews Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_DomainName"></a> DomainName

|Property|Value|
|--------|-----|
|Description|Active Directory domain of which the user is a member.|
|DisplayName|User Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|domainname|
|MaxLength|1024|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_EmailRouterAccessApproval"></a> EmailRouterAccessApproval

|Property|Value|
|--------|-----|
|Description|Shows the status of the primary email address.|
|DisplayName|Primary Email Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailrouteraccessapproval|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### EmailRouterAccessApproval Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Empty||
|1|Approved||
|2|Pending Approval||
|3|Rejected||



### <a name="BKMK_EmployeeId"></a> EmployeeId

|Property|Value|
|--------|-----|
|Description|Employee identifier for the user.|
|DisplayName|Employee|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|employeeid|
|MaxLength|100|
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


### <a name="BKMK_FirstName"></a> FirstName

|Property|Value|
|--------|-----|
|Description|First name of the user.|
|DisplayName|First Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|firstname|
|MaxLength|256|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_GovernmentId"></a> GovernmentId

|Property|Value|
|--------|-----|
|Description|Government identifier for the user.|
|DisplayName|Government|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|governmentid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_HomePhone"></a> HomePhone

|Property|Value|
|--------|-----|
|Description|Home phone number for the user.|
|DisplayName|Home Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|homephone|
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


### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Incoming email delivery method for the user.|
|DisplayName|Incoming Email Delivery Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingemaildeliverymethod|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### IncomingEmailDeliveryMethod Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|Microsoft Dynamics 365 for Outlook||
|2|Server-Side Synchronization or Email Router||
|3|Forward Mailbox||



### <a name="BKMK_InternalEMailAddress"></a> InternalEMailAddress

|Property|Value|
|--------|-----|
|Description|Internal email address for the user.|
|DisplayName|Primary Email|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|internalemailaddress|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_InviteStatusCode"></a> InviteStatusCode

|Property|Value|
|--------|-----|
|Description|User invitation status.|
|DisplayName|Invitation Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|invitestatuscode|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### InviteStatusCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Invitation Not Sent||
|1|Invited||
|2|Invitation Near Expired||
|3|Invitation Expired||
|4|Invitation Accepted||
|5|Invitation Rejected||
|6|Invitation Revoked||



### <a name="BKMK_IsDisabled"></a> IsDisabled

|Property|Value|
|--------|-----|
|Description|Information about whether the user is enabled.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isdisabled|
|RequiredLevel|None|
|Type|Boolean|

#### IsDisabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Disabled|
|0|Enabled|

**DefaultValue**: False



### <a name="BKMK_IsIntegrationUser"></a> IsIntegrationUser

|Property|Value|
|--------|-----|
|Description|Check if user is an integration user.|
|DisplayName|Integration user mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isintegrationuser|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsIntegrationUser Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsLicensed"></a> IsLicensed

|Property|Value|
|--------|-----|
|Description|Information about whether the user is licensed.|
|DisplayName|User Licensed|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|islicensed|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsLicensed Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsSyncWithDirectory"></a> IsSyncWithDirectory

|Property|Value|
|--------|-----|
|Description|Information about whether the user is synced with the directory.|
|DisplayName|User Synced|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|issyncwithdirectory|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsSyncWithDirectory Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_JobTitle"></a> JobTitle

|Property|Value|
|--------|-----|
|Description|Job title of the user.|
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
|Description|Last name of the user.|
|DisplayName|Last Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastname|
|MaxLength|256|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_MiddleName"></a> MiddleName

|Property|Value|
|--------|-----|
|Description|Middle name of the user.|
|DisplayName|Middle Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|middlename|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobileAlertEMail"></a> MobileAlertEMail

|Property|Value|
|--------|-----|
|Description|Mobile alert email address for the user.|
|DisplayName|Mobile Alert Email|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobilealertemail|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobileOfflineProfileId"></a> MobileOfflineProfileId

|Property|Value|
|--------|-----|
|Description|Items contained with a particular SystemUser.|
|DisplayName|Mobile Offline Profile|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileid|
|RequiredLevel|None|
|Targets|mobileofflineprofile|
|Type|Lookup|


### <a name="BKMK_MobileOfflineProfileIdName"></a> MobileOfflineProfileIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobilePhone"></a> MobilePhone

|Property|Value|
|--------|-----|
|Description|Mobile phone number for the user.|
|DisplayName|Mobile Phone|
|FormatName|Phone|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobilephone|
|MaxLength|64|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NickName"></a> NickName

|Property|Value|
|--------|-----|
|Description|Nickname of the user.|
|DisplayName|Nickname|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|nickname|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Outgoing email delivery method for the user.|
|DisplayName|Outgoing Email Delivery Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingemaildeliverymethod|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### OutgoingEmailDeliveryMethod Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|Microsoft Dynamics 365 for Outlook||
|2|Server-Side Synchronization or Email Router||



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


### <a name="BKMK_ParentSystemUserId"></a> ParentSystemUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the manager of the user.|
|DisplayName|Manager|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentsystemuserid|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_PassportHi"></a> PassportHi

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Passport Hi|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|passporthi|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_PassportLo"></a> PassportLo

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Passport Lo|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|passportlo|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_PersonalEMailAddress"></a> PersonalEMailAddress

|Property|Value|
|--------|-----|
|Description|Personal email address of the user.|
|DisplayName|Email 2|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|personalemailaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PhotoUrl"></a> PhotoUrl

|Property|Value|
|--------|-----|
|Description|URL for the Website on which a photo of the user is located.|
|DisplayName|Photo URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|photourl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PositionId"></a> PositionId

|Property|Value|
|--------|-----|
|Description|User's position in hierarchical security model.|
|DisplayName|Position|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|positionid|
|RequiredLevel|None|
|Targets|position|
|Type|Lookup|


### <a name="BKMK_PreferredAddressCode"></a> PreferredAddressCode

|Property|Value|
|--------|-----|
|Description|Preferred address for the user.|
|DisplayName|Preferred Address|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredaddresscode|
|RequiredLevel|None|
|Type|Picklist|

#### PreferredAddressCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Mailing Address||
|2|Other Address||



### <a name="BKMK_PreferredEmailCode"></a> PreferredEmailCode

|Property|Value|
|--------|-----|
|Description|Preferred email address for the user.|
|DisplayName|Preferred Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredemailcode|
|RequiredLevel|None|
|Type|Picklist|

#### PreferredEmailCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Default Value||



### <a name="BKMK_PreferredPhoneCode"></a> PreferredPhoneCode

|Property|Value|
|--------|-----|
|Description|Preferred phone number for the user.|
|DisplayName|Preferred Phone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredphonecode|
|RequiredLevel|None|
|Type|Picklist|

#### PreferredPhoneCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Main Phone||
|2|Other Phone||
|3|Home Phone||
|4|Mobile Phone||



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


### <a name="BKMK_QueueId"></a> QueueId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the default queue for the user.|
|DisplayName|Default Queue|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|queueid|
|RequiredLevel|None|
|Targets|queue|
|Type|Lookup|


### <a name="BKMK_Salutation"></a> Salutation

|Property|Value|
|--------|-----|
|Description|Salutation for correspondence with the user.|
|DisplayName|Salutation|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|salutation|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SetupUser"></a> SetupUser

|Property|Value|
|--------|-----|
|Description|Check if user is a setup user.|
|DisplayName|Restricted Access Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|setupuser|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### SetupUser Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_SharePointEmailAddress"></a> SharePointEmailAddress

|Property|Value|
|--------|-----|
|Description|SharePoint Work Email Address|
|DisplayName|SharePoint Email Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sharepointemailaddress|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Skills"></a> Skills

|Property|Value|
|--------|-----|
|Description|Skill set of the user.|
|DisplayName|Skills|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|skills|
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


### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user.|
|DisplayName|User|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|systemuserid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TerritoryId"></a> TerritoryId

**Added by**: Application Common Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the territory to which the user is assigned.|
|DisplayName|Territory|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|territoryid|
|RequiredLevel|None|
|Targets|territory|
|Type|Lookup|


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


### <a name="BKMK_Title"></a> Title

|Property|Value|
|--------|-----|
|Description|Title of the user.|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the systemuser.|
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


### <a name="BKMK_UserLicenseType"></a> UserLicenseType

|Property|Value|
|--------|-----|
|Description|Shows the type of user license.|
|DisplayName|User License Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|userlicensetype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


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


### <a name="BKMK_WindowsLiveID"></a> WindowsLiveID

|Property|Value|
|--------|-----|
|Description|Windows Live ID|
|DisplayName|Windows Live ID|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|windowsliveid|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YammerEmailAddress"></a> YammerEmailAddress

|Property|Value|
|--------|-----|
|Description|User's Yammer login email address|
|DisplayName|Yammer Email|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yammeremailaddress|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YammerUserId"></a> YammerUserId

|Property|Value|
|--------|-----|
|Description|User's Yammer ID|
|DisplayName|Yammer User ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yammeruserid|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiFirstName"></a> YomiFirstName

|Property|Value|
|--------|-----|
|Description|Pronunciation of the first name of the user, written in phonetic hiragana or katakana characters.|
|DisplayName|Yomi First Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomifirstname|
|MaxLength|64|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiLastName"></a> YomiLastName

|Property|Value|
|--------|-----|
|Description|Pronunciation of the last name of the user, written in phonetic hiragana or katakana characters.|
|DisplayName|Yomi Last Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomilastname|
|MaxLength|64|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiMiddleName"></a> YomiMiddleName

|Property|Value|
|--------|-----|
|Description|Pronunciation of the middle name of the user, written in phonetic hiragana or katakana characters.|
|DisplayName|Yomi Middle Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomimiddlename|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActiveDirectoryGuid](#BKMK_ActiveDirectoryGuid)
- [Address1_Composite](#BKMK_Address1_Composite)
- [Address2_Composite](#BKMK_Address2_Composite)
- [ApplicationIdUri](#BKMK_ApplicationIdUri)
- [AzureActiveDirectoryObjectId](#BKMK_AzureActiveDirectoryObjectId)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DefaultFiltersPopulated](#BKMK_DefaultFiltersPopulated)
- [DefaultMailbox](#BKMK_DefaultMailbox)
- [DefaultMailboxName](#BKMK_DefaultMailboxName)
- [DefaultOdbFolderName](#BKMK_DefaultOdbFolderName)
- [DeletedState](#BKMK_DeletedState)
- [DisabledReason](#BKMK_DisabledReason)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FullName](#BKMK_FullName)
- [IdentityId](#BKMK_IdentityId)
- [IsActiveDirectoryUser](#BKMK_IsActiveDirectoryUser)
- [IsEmailAddressApprovedByO365Admin](#BKMK_IsEmailAddressApprovedByO365Admin)
- [LatestUpdateTime](#BKMK_LatestUpdateTime)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [ParentSystemUserIdName](#BKMK_ParentSystemUserIdName)
- [ParentSystemUserIdYomiName](#BKMK_ParentSystemUserIdYomiName)
- [PositionIdName](#BKMK_PositionIdName)
- [QueueIdName](#BKMK_QueueIdName)
- [TerritoryIdName](#BKMK_TerritoryIdName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [UserPuid](#BKMK_UserPuid)
- [VersionNumber](#BKMK_VersionNumber)
- [YomiFullName](#BKMK_YomiFullName)


### <a name="BKMK_ActiveDirectoryGuid"></a> ActiveDirectoryGuid

|Property|Value|
|--------|-----|
|Description|Active Directory object GUID for the system user.|
|DisplayName|Active Directory Guid|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|activedirectoryguid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Address1_Composite"></a> Address1_Composite

|Property|Value|
|--------|-----|
|Description|Shows the complete primary address.|
|DisplayName|Address|
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
|DisplayName|Other Address|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|address2_composite|
|MaxLength|1000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ApplicationIdUri"></a> ApplicationIdUri

|Property|Value|
|--------|-----|
|Description|The URI used as a unique logical identifier for the external app. This can be used to validate the application.|
|DisplayName|Application ID URI|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|applicationiduri|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AzureActiveDirectoryObjectId"></a> AzureActiveDirectoryObjectId

|Property|Value|
|--------|-----|
|Description|This is the application directory object Id.|
|DisplayName|Azure AD Object ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|azureactivedirectoryobjectid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the user.|
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
|Description|Date and time when the user was created.|
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
|Description|Unique identifier of the delegate user who created the systemuser.|
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


### <a name="BKMK_DefaultFiltersPopulated"></a> DefaultFiltersPopulated

|Property|Value|
|--------|-----|
|Description|Indicates if default outlook filters have been populated.|
|DisplayName|Default Filters Populated|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultfilterspopulated|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### DefaultFiltersPopulated Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_DefaultMailbox"></a> DefaultMailbox

|Property|Value|
|--------|-----|
|Description|Select the mailbox associated with this user.|
|DisplayName|Mailbox|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultmailbox|
|RequiredLevel|None|
|Targets|mailbox|
|Type|Lookup|


### <a name="BKMK_DefaultMailboxName"></a> DefaultMailboxName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultmailboxname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DefaultOdbFolderName"></a> DefaultOdbFolderName

|Property|Value|
|--------|-----|
|Description|Type a default folder name for the user's OneDrive For Business location.|
|DisplayName|Default OneDrive for Business Folder Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultodbfoldername|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_DeletedState"></a> DeletedState

**Added by**: AuthorizationCore Solution

|Property|Value|
|--------|-----|
|Description|User delete state|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|deletedstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### DeletedState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not deleted||
|1|Soft deleted||



### <a name="BKMK_DisabledReason"></a> DisabledReason

|Property|Value|
|--------|-----|
|Description|Reason for disabling the user.|
|DisplayName|Disabled Reason|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|disabledreason|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


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
|Description|Exchange rate for the currency associated with the systemuser with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_FullName"></a> FullName

|Property|Value|
|--------|-----|
|Description|Full name of the user.|
|DisplayName|Full Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fullname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IdentityId"></a> IdentityId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Unique user identity id|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|identityid|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_IsActiveDirectoryUser"></a> IsActiveDirectoryUser

|Property|Value|
|--------|-----|
|Description|Information about whether the user is an AD user.|
|DisplayName|Is Active Directory User|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|isactivedirectoryuser|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsActiveDirectoryUser Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

|Property|Value|
|--------|-----|
|Description|Shows the status of approval of the email address by O365 Admin.|
|DisplayName|Email Address O365 Admin Approval Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isemailaddressapprovedbyo365admin|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsEmailAddressApprovedByO365Admin Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LatestUpdateTime"></a> LatestUpdateTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Time stamp of the latest update for the user|
|DisplayName|Latest User Update Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|latestupdatetime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the user.|
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
|Description|Date and time when the user was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the systemuser.|
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
|Description|Unique identifier of the organization associated with the user.|
|DisplayName|Organization |
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_ParentSystemUserIdName"></a> ParentSystemUserIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentsystemuseridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentSystemUserIdYomiName"></a> ParentSystemUserIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentsystemuseridyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PositionIdName"></a> PositionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|positionidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_QueueIdName"></a> QueueIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|queueidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TerritoryIdName"></a> TerritoryIdName

**Added by**: Application Common Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|territoryidname|
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


### <a name="BKMK_UserPuid"></a> UserPuid

|Property|Value|
|--------|-----|
|Description| User PUID User Identifiable Information|
|DisplayName|User PUID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|userpuid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the user.|
|DisplayName|Version number|
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
|Description|Pronunciation of the full name of the user, written in phonetic hiragana or katakana characters.|
|DisplayName|Yomi Full Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yomifullname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [lk_appmodule_modifiedby](#BKMK_lk_appmodule_modifiedby)
- [systemuser_principalobjectattributeaccess_principalid](#BKMK_systemuser_principalobjectattributeaccess_principalid)
- [user_exchangesyncidmapping](#BKMK_user_exchangesyncidmapping)
- [lk_theme_createdby](#BKMK_lk_theme_createdby)
- [lk_theme_createdonbehalfby](#BKMK_lk_theme_createdonbehalfby)
- [lk_theme_modifiedby](#BKMK_lk_theme_modifiedby)
- [lk_theme_modifiedonbehalfby](#BKMK_lk_theme_modifiedonbehalfby)
- [lk_usermapping_createdby](#BKMK_lk_usermapping_createdby)
- [lk_usermapping_createdonbehalfby](#BKMK_lk_usermapping_createdonbehalfby)
- [lk_usermapping_modifiedby](#BKMK_lk_usermapping_modifiedby)
- [lk_usermapping_modifiedonbehalfby](#BKMK_lk_usermapping_modifiedonbehalfby)
- [lk_interactionforemail_createdby](#BKMK_lk_interactionforemail_createdby)
- [lk_interactionforemail_createdonbehalfby](#BKMK_lk_interactionforemail_createdonbehalfby)
- [lk_interactionforemail_modifiedby](#BKMK_lk_interactionforemail_modifiedby)
- [lk_interactionforemail_modifiedonbehalfby](#BKMK_lk_interactionforemail_modifiedonbehalfby)
- [user_interactionforemail](#BKMK_user_interactionforemail)
- [lk_knowledgearticle_createdby](#BKMK_lk_knowledgearticle_createdby)
- [lk_knowledgearticle_createdonbehalfby](#BKMK_lk_knowledgearticle_createdonbehalfby)
- [lk_knowledgearticle_modifiedby](#BKMK_lk_knowledgearticle_modifiedby)
- [lk_knowledgearticle_modifiedonbehalfby](#BKMK_lk_knowledgearticle_modifiedonbehalfby)
- [user_knowledgearticle](#BKMK_user_knowledgearticle)
- [user_sharepointsite](#BKMK_user_sharepointsite)
- [user_sharepointdocumentlocation](#BKMK_user_sharepointdocumentlocation)
- [lk_goal_createdby](#BKMK_lk_goal_createdby)
- [lk_goal_createdonbehalfby](#BKMK_lk_goal_createdonbehalfby)
- [lk_goal_modifiedby](#BKMK_lk_goal_modifiedby)
- [lk_goal_modifiedonbehalfby](#BKMK_lk_goal_modifiedonbehalfby)
- [user_goal](#BKMK_user_goal)
- [user_goal_goalowner](#BKMK_user_goal_goalowner)
- [lk_metric_createdby](#BKMK_lk_metric_createdby)
- [lk_metric_createdonbehalfby](#BKMK_lk_metric_createdonbehalfby)
- [lk_metric_modifiedby](#BKMK_lk_metric_modifiedby)
- [lk_metric_modifiedonbehalfby](#BKMK_lk_metric_modifiedonbehalfby)
- [lk_rollupfield_createdby](#BKMK_lk_rollupfield_createdby)
- [lk_rollupfield_createdonbehalfby](#BKMK_lk_rollupfield_createdonbehalfby)
- [lk_rollupfield_modifiedby](#BKMK_lk_rollupfield_modifiedby)
- [lk_rollupfield_modifiedonbehalfby](#BKMK_lk_rollupfield_modifiedonbehalfby)
- [lk_goalrollupquery_createdby](#BKMK_lk_goalrollupquery_createdby)
- [lk_goalrollupquery_createdonbehalfby](#BKMK_lk_goalrollupquery_createdonbehalfby)
- [lk_goalrollupquery_modifiedby](#BKMK_lk_goalrollupquery_modifiedby)
- [lk_goalrollupquery_modifiedonbehalfby](#BKMK_lk_goalrollupquery_modifiedonbehalfby)
- [lk_emailserverprofile_createdonbehalfby](#BKMK_lk_emailserverprofile_createdonbehalfby)
- [lk_emailserverprofile_modifiedonbehalfby](#BKMK_lk_emailserverprofile_modifiedonbehalfby)
- [lk_mailbox_createdby](#BKMK_lk_mailbox_createdby)
- [lk_mailbox_createdonbehalfby](#BKMK_lk_mailbox_createdonbehalfby)
- [lk_mailbox_modifiedby](#BKMK_lk_mailbox_modifiedby)
- [lk_mailbox_modifiedonbehalfby](#BKMK_lk_mailbox_modifiedonbehalfby)
- [user_mailbox](#BKMK_user_mailbox)
- [mailbox_regarding_systemuser](#BKMK_mailbox_regarding_systemuser)
- [lk_post_modifiedonbehalfby](#BKMK_lk_post_modifiedonbehalfby)
- [lk_position_createdby](#BKMK_lk_position_createdby)
- [lk_position_createdonbehalfby](#BKMK_lk_position_createdonbehalfby)
- [lk_position_modifiedby](#BKMK_lk_position_modifiedby)
- [lk_position_modifiedonbehalfby](#BKMK_lk_position_modifiedonbehalfby)
- [lk_solution_createdby](#BKMK_lk_solution_createdby)
- [lk_solution_modifiedby](#BKMK_lk_solution_modifiedby)
- [lk_publisher_createdby](#BKMK_lk_publisher_createdby)
- [lk_publisher_modifiedby](#BKMK_lk_publisher_modifiedby)
- [lk_officegraphdocument_createdonbehalfby](#BKMK_lk_officegraphdocument_createdonbehalfby)
- [lk_officegraphdocument_modifiedonbehalfby](#BKMK_lk_officegraphdocument_modifiedonbehalfby)
- [lk_recommendeddocument_createdby](#BKMK_lk_recommendeddocument_createdby)
- [lk_recommendeddocument_createdonbehalfby](#BKMK_lk_recommendeddocument_createdonbehalfby)
- [lk_recommendeddocument_modifiedby](#BKMK_lk_recommendeddocument_modifiedby)
- [lk_recommendeddocument_modifiedonbehalfby](#BKMK_lk_recommendeddocument_modifiedonbehalfby)
- [lk_KnowledgeBaseRecord_createdby](#BKMK_lk_KnowledgeBaseRecord_createdby)
- [lk_KnowledgeBaseRecord_createdonbehalfby](#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby)
- [lk_KnowledgeBaseRecord_modifiedby](#BKMK_lk_KnowledgeBaseRecord_modifiedby)
- [lk_KnowledgeBaseRecord_modifiedonbehalfby](#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby)
- [lk_lookupmapping_modifiedby](#BKMK_lk_lookupmapping_modifiedby)
- [lk_usersettings_createdonbehalfby](#BKMK_lk_usersettings_createdonbehalfby)
- [lk_kbarticletemplatebase_modifiedby](#BKMK_lk_kbarticletemplatebase_modifiedby)
- [lk_fax_modifiedby](#BKMK_lk_fax_modifiedby)
- [lk_processsession_completedby](#BKMK_lk_processsession_completedby)
- [modifiedby_sdkmessageprocessingstepsecureconfig](#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig)
- [lk_businessunit_createdonbehalfby](#BKMK_lk_businessunit_createdonbehalfby)
- [lk_duplicaterule_createdonbehalfby](#BKMK_lk_duplicaterule_createdonbehalfby)
- [lk_sdkmessage_modifiedonbehalfby](#BKMK_lk_sdkmessage_modifiedonbehalfby)
- [lk_translationprocess_modifiedonbehalfby](#BKMK_lk_translationprocess_modifiedonbehalfby)
- [lk_actioncardbase_createdonbehalfby](#BKMK_lk_actioncardbase_createdonbehalfby)
- [lk_sdkmessagefilter_createdonbehalfby](#BKMK_lk_sdkmessagefilter_createdonbehalfby)
- [lk_slabase_modifiedonbehalfby](#BKMK_lk_slabase_modifiedonbehalfby)
- [lk_feedback_modifiedby](#BKMK_lk_feedback_modifiedby)
- [lk_templatebase_modifiedby](#BKMK_lk_templatebase_modifiedby)
- [lk_kbarticletemplate_modifiedonbehalfby](#BKMK_lk_kbarticletemplate_modifiedonbehalfby)
- [lk_slakpiinstancebase_createdby](#BKMK_lk_slakpiinstancebase_createdby)
- [lk_ACIViewMapper_createdby](#BKMK_lk_ACIViewMapper_createdby)
- [lk_userqueryvisualization_modifiedby](#BKMK_lk_userqueryvisualization_modifiedby)
- [lk_recurringappointmentmaster_createdonbehalfby](#BKMK_lk_recurringappointmentmaster_createdonbehalfby)
- [lk_lookupmapping_createdonbehalfby](#BKMK_lk_lookupmapping_createdonbehalfby)
- [lk_MobileOfflineProfileItem_createdby](#BKMK_lk_MobileOfflineProfileItem_createdby)
- [lk_recurringappointmentmaster_modifiedby](#BKMK_lk_recurringappointmentmaster_modifiedby)
- [lk_fax_createdby](#BKMK_lk_fax_createdby)
- [lk_letter_modifiedonbehalfby](#BKMK_lk_letter_modifiedonbehalfby)
- [lk_transformationmapping_createdby](#BKMK_lk_transformationmapping_createdby)
- [lk_reportcategorybase_createdby](#BKMK_lk_reportcategorybase_createdby)
- [lk_letter_createdby](#BKMK_lk_letter_createdby)
- [lk_customcontrolresource_modifiedby](#BKMK_lk_customcontrolresource_modifiedby)
- [lk_expiredprocess_createdonbehalfby](#BKMK_lk_expiredprocess_createdonbehalfby)
- [lk_appmodulecomponent_modifiedby](#BKMK_lk_appmodulecomponent_modifiedby)
- [lk_calendar_modifiedby](#BKMK_lk_calendar_modifiedby)
- [SystemUser_DuplicateRules](#BKMK_SystemUser_DuplicateRules)
- [lk_plugintype_createdonbehalfby](#BKMK_lk_plugintype_createdonbehalfby)
- [lk_mobileofflineprofileitem_createdonbehalfby](#BKMK_lk_mobileofflineprofileitem_createdonbehalfby)
- [lk_fax_createdonbehalfby](#BKMK_lk_fax_createdonbehalfby)
- [lk_timezonedefinition_modifiedby](#BKMK_lk_timezonedefinition_modifiedby)
- [lk_columnmapping_createdby](#BKMK_lk_columnmapping_createdby)
- [lk_reportcategorybase_modifiedby](#BKMK_lk_reportcategorybase_modifiedby)
- [lk_sharepointsitebase_createdonbehalfby](#BKMK_lk_sharepointsitebase_createdonbehalfby)
- [lk_workflowlog_modifiedby](#BKMK_lk_workflowlog_modifiedby)
- [lk_syncerrorbase_createdonbehalfby](#BKMK_lk_syncerrorbase_createdonbehalfby)
- [lk_bulkdeleteoperation_modifiedonbehalfby](#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby)
- [lk_serviceendpointbase_createdonbehalfby](#BKMK_lk_serviceendpointbase_createdonbehalfby)
- [lk_solutioncomponentbase_createdonbehalfby](#BKMK_lk_solutioncomponentbase_createdonbehalfby)
- [lk_plugintype_modifiedonbehalfby](#BKMK_lk_plugintype_modifiedonbehalfby)
- [lk_lookupmapping_modifiedonbehalfby](#BKMK_lk_lookupmapping_modifiedonbehalfby)
- [lk_phonecall_modifiedby](#BKMK_lk_phonecall_modifiedby)
- [lk_slabase_modifiedby](#BKMK_lk_slabase_modifiedby)
- [lk_workflowlog_modifiedonbehalfby](#BKMK_lk_workflowlog_modifiedonbehalfby)
- [lk_importfilebase_createdonbehalfby](#BKMK_lk_importfilebase_createdonbehalfby)
- [lk_fieldsecurityprofile_createdonbehalfby](#BKMK_lk_fieldsecurityprofile_createdonbehalfby)
- [lk_importmapbase_createdby](#BKMK_lk_importmapbase_createdby)
- [lk_PostFollow_createdby](#BKMK_lk_PostFollow_createdby)
- [systemuser_PostFollows](#BKMK_systemuser_PostFollows)
- [lk_post_createdby](#BKMK_lk_post_createdby)
- [lk_post_createdonbehalfby](#BKMK_lk_post_createdonbehalfby)
- [lk_post_modifiedby](#BKMK_lk_post_modifiedby)
- [lk_postcomment_createdby](#BKMK_lk_postcomment_createdby)
- [user_owner_postfollows](#BKMK_user_owner_postfollows)
- [lk_postfollow_createdonbehalfby](#BKMK_lk_postfollow_createdonbehalfby)
- [lk_postcomment_createdonbehalfby](#BKMK_lk_postcomment_createdonbehalfby)
- [lk_postlike_createdonbehalfby](#BKMK_lk_postlike_createdonbehalfby)
- [lk_postlike_createdby](#BKMK_lk_postlike_createdby)
- [lk_queueitem_modifiedonbehalfby](#BKMK_lk_queueitem_modifiedonbehalfby)
- [user_socialactivity](#BKMK_user_socialactivity)
- [lk_translationprocess_createdonbehalfby](#BKMK_lk_translationprocess_createdonbehalfby)
- [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby)
- [lk_feedback_modifiedonbehalfby](#BKMK_lk_feedback_modifiedonbehalfby)
- [lk_workflowlog_createdonbehalfby](#BKMK_lk_workflowlog_createdonbehalfby)
- [lk_role_createdonbehalfby](#BKMK_lk_role_createdonbehalfby)
- [lk_transactioncurrency_modifiedonbehalfby](#BKMK_lk_transactioncurrency_modifiedonbehalfby)
- [lk_rolebase_modifiedby](#BKMK_lk_rolebase_modifiedby)
- [lk_navigationsetting_createdby](#BKMK_lk_navigationsetting_createdby)
- [lk_subject_modifiedonbehalfby](#BKMK_lk_subject_modifiedonbehalfby)
- [lk_duplicaterule_modifiedonbehalfby](#BKMK_lk_duplicaterule_modifiedonbehalfby)
- [lk_task_modifiedonbehalfby](#BKMK_lk_task_modifiedonbehalfby)
- [lk_subjectbase_modifiedby](#BKMK_lk_subjectbase_modifiedby)
- [lk_mailboxtrackingfolder_modifiedby](#BKMK_lk_mailboxtrackingfolder_modifiedby)
- [impersonatinguserid_sdkmessageprocessingstep](#BKMK_impersonatinguserid_sdkmessageprocessingstep)
- [lk_kbarticle_createdonbehalfby](#BKMK_lk_kbarticle_createdonbehalfby)
- [lk_calendar_createdonbehalfby](#BKMK_lk_calendar_createdonbehalfby)
- [lk_businessunitnewsarticlebase_modifiedby](#BKMK_lk_businessunitnewsarticlebase_modifiedby)
- [user_userqueryvisualizations](#BKMK_user_userqueryvisualizations)
- [lk_tracelog_createdonbehalfby](#BKMK_lk_tracelog_createdonbehalfby)
- [lk_queueitembase_workerid](#BKMK_lk_queueitembase_workerid)
- [lk_mobileofflineprofileitem_modifiedby](#BKMK_lk_mobileofflineprofileitem_modifiedby)
- [lk_customeraddressbase_modifiedby](#BKMK_lk_customeraddressbase_modifiedby)
- [lk_activitypointer_modifiedby](#BKMK_lk_activitypointer_modifiedby)
- [lk_customeraddressbase_createdby](#BKMK_lk_customeraddressbase_createdby)
- [lk_syncerrorbase_modifiedonbehalfby](#BKMK_lk_syncerrorbase_modifiedonbehalfby)
- [SystemUser_BulkDeleteFailures](#BKMK_SystemUser_BulkDeleteFailures)
- [lk_teambase_modifiedby](#BKMK_lk_teambase_modifiedby)
- [workflow_createdby](#BKMK_workflow_createdby)
- [lk_queue_modifiedonbehalfby](#BKMK_lk_queue_modifiedonbehalfby)
- [lk_customeraddress_modifiedonbehalfby](#BKMK_lk_customeraddress_modifiedonbehalfby)
- [lk_rolebase_createdby](#BKMK_lk_rolebase_createdby)
- [lk_reportcategory_modifiedonbehalfby](#BKMK_lk_reportcategory_modifiedonbehalfby)
- [lk_transformationmapping_modifiedby](#BKMK_lk_transformationmapping_modifiedby)
- [lk_duplicaterulecondition_modifiedonbehalfby](#BKMK_lk_duplicaterulecondition_modifiedonbehalfby)
- [lk_picklistmapping_createdby](#BKMK_lk_picklistmapping_createdby)
- [lk_savedqueryvisualizationbase_modifiedby](#BKMK_lk_savedqueryvisualizationbase_modifiedby)
- [lk_kbarticlecommentbase_modifiedby](#BKMK_lk_kbarticlecommentbase_modifiedby)
- [lk_email_modifiedonbehalfby](#BKMK_lk_email_modifiedonbehalfby)
- [lk_asyncoperation_createdonbehalfby](#BKMK_lk_asyncoperation_createdonbehalfby)
- [lk_pluginassembly_modifiedonbehalfby](#BKMK_lk_pluginassembly_modifiedonbehalfby)
- [lk_team_createdonbehalfby](#BKMK_lk_team_createdonbehalfby)
- [createdby_connection](#BKMK_createdby_connection)
- [workflow_modifiedby](#BKMK_workflow_modifiedby)
- [lk_businessunitnewsarticle_createdonbehalfby](#BKMK_lk_businessunitnewsarticle_createdonbehalfby)
- [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby)
- [lk_processsessionbase_createdonbehalfby](#BKMK_lk_processsessionbase_createdonbehalfby)
- [lk_appmodule_modifiedonbehalfby](#BKMK_lk_appmodule_modifiedonbehalfby)
- [lk_customcontroldefaultconfig_modifiedonbehalfby](#BKMK_lk_customcontroldefaultconfig_modifiedonbehalfby)
- [lk_tracelog_modifiedby](#BKMK_lk_tracelog_modifiedby)
- [user_appointment](#BKMK_user_appointment)
- [lk_appconfig_createdonbehalfby](#BKMK_lk_appconfig_createdonbehalfby)
- [lk_appconfiginstance_createdonbehalfby](#BKMK_lk_appconfiginstance_createdonbehalfby)
- [lk_DisplayStringbase_modifiedby](#BKMK_lk_DisplayStringbase_modifiedby)
- [lk_importlog_modifiedonbehalfby](#BKMK_lk_importlog_modifiedonbehalfby)
- [lk_navigationsetting_modifiedby](#BKMK_lk_navigationsetting_modifiedby)
- [SystemUser_Email_EmailSender](#BKMK_SystemUser_Email_EmailSender)
- [user_activity](#BKMK_user_activity)
- [lk_monthlyfiscalcalendar_salespersonid](#BKMK_lk_monthlyfiscalcalendar_salespersonid)
- [lk_businessunit_modifiedonbehalfby](#BKMK_lk_businessunit_modifiedonbehalfby)
- [lk_asyncoperation_modifiedonbehalfby](#BKMK_lk_asyncoperation_modifiedonbehalfby)
- [lk_teambase_createdby](#BKMK_lk_teambase_createdby)
- [lk_emailserverprofile_modifiedby](#BKMK_lk_emailserverprofile_modifiedby)
- [lk_processtriggerbase_modifiedonbehalfby](#BKMK_lk_processtriggerbase_modifiedonbehalfby)
- [lk_mailmergetemplate_modifiedonbehalfby](#BKMK_lk_mailmergetemplate_modifiedonbehalfby)
- [lk_connectionbase_modifiedonbehalfby](#BKMK_lk_connectionbase_modifiedonbehalfby)
- [lk_queueitem_createdonbehalfby](#BKMK_lk_queueitem_createdonbehalfby)
- [lk_teamtemplate_modifiedonbehalfby](#BKMK_lk_teamtemplate_modifiedonbehalfby)
- [lk_documenttemplatebase_modifiedby](#BKMK_lk_documenttemplatebase_modifiedby)
- [lk_transformationparametermapping_createdonbehalfby](#BKMK_lk_transformationparametermapping_createdonbehalfby)
- [user_userquery](#BKMK_user_userquery)
- [lk_appmodule_createdby](#BKMK_lk_appmodule_createdby)
- [lk_kbarticlecommentbase_createdby](#BKMK_lk_kbarticlecommentbase_createdby)
- [workflow_createdonbehalfby](#BKMK_workflow_createdonbehalfby)
- [lk_recurrencerule_modifiedby](#BKMK_lk_recurrencerule_modifiedby)
- [lk_category_modifiedonbehalfby](#BKMK_lk_category_modifiedonbehalfby)
- [lk_appconfig_modifiedby](#BKMK_lk_appconfig_modifiedby)
- [lk_bulkdeleteoperationbase_createdby](#BKMK_lk_bulkdeleteoperationbase_createdby)
- [lk_asyncoperation_createdby](#BKMK_lk_asyncoperation_createdby)
- [lk_sdkmessagefilter_modifiedonbehalfby](#BKMK_lk_sdkmessagefilter_modifiedonbehalfby)
- [user_recurringappointmentmaster](#BKMK_user_recurringappointmentmaster)
- [lk_slaitembase_modifiedby](#BKMK_lk_slaitembase_modifiedby)
- [lk_publisheraddressbase_modifiedonbehalfby](#BKMK_lk_publisheraddressbase_modifiedonbehalfby)
- [lk_documenttemplatebase_createdby](#BKMK_lk_documenttemplatebase_createdby)
- [lk_transformationparametermapping_modifiedby](#BKMK_lk_transformationparametermapping_modifiedby)
- [lk_slabase_createdby](#BKMK_lk_slabase_createdby)
- [lk_organizationbase_createdby](#BKMK_lk_organizationbase_createdby)
- [lk_report_modifiedonbehalfby](#BKMK_lk_report_modifiedonbehalfby)
- [lk_quarterlyfiscalcalendar_modifiedby](#BKMK_lk_quarterlyfiscalcalendar_modifiedby)
- [createdby_serviceendpoint](#BKMK_createdby_serviceendpoint)
- [lk_duplicaterulecondition_createdonbehalfby](#BKMK_lk_duplicaterulecondition_createdonbehalfby)
- [lk_transactioncurrencybase_modifiedby](#BKMK_lk_transactioncurrencybase_modifiedby)
- [lk_DisplayStringbase_createdby](#BKMK_lk_DisplayStringbase_createdby)
- [lk_slaitembase_modifiedonbehalfby](#BKMK_lk_slaitembase_modifiedonbehalfby)
- [annotation_owning_user](#BKMK_annotation_owning_user)
- [system_user_contacts](#BKMK_system_user_contacts)
- [lk_transformationparametermapping_createdby](#BKMK_lk_transformationparametermapping_createdby)
- [lk_phonecall_createdonbehalfby](#BKMK_lk_phonecall_createdonbehalfby)
- [lk_email_modifiedby](#BKMK_lk_email_modifiedby)
- [lk_usersettingsbase_createdby](#BKMK_lk_usersettingsbase_createdby)
- [lk_teamtemplate_createdonbehalfby](#BKMK_lk_teamtemplate_createdonbehalfby)
- [lk_appmodule_createdonbehalfby](#BKMK_lk_appmodule_createdonbehalfby)
- [lk_importlogbase_createdby](#BKMK_lk_importlogbase_createdby)
- [lk_sharepointdocumentlocationbase_createdby](#BKMK_lk_sharepointdocumentlocationbase_createdby)
- [user_accounts](#BKMK_user_accounts)
- [user_settings](#BKMK_user_settings)
- [modifiedby_plugintype](#BKMK_modifiedby_plugintype)
- [lk_importentitymapping_modifiedonbehalfby](#BKMK_lk_importentitymapping_modifiedonbehalfby)
- [lk_savedquerybase_createdby](#BKMK_lk_savedquerybase_createdby)
- [lk_activitypointer_createdby](#BKMK_lk_activitypointer_createdby)
- [lk_columnmapping_createdonbehalfby](#BKMK_lk_columnmapping_createdonbehalfby)
- [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby)
- [lk_subject_createdonbehalfby](#BKMK_lk_subject_createdonbehalfby)
- [lk_appconfigmaster_createdonbehalfby](#BKMK_lk_appconfigmaster_createdonbehalfby)
- [lk_kbarticle_modifiedonbehalfby](#BKMK_lk_kbarticle_modifiedonbehalfby)
- [createdby_sdkmessageprocessingstepsecureconfig](#BKMK_createdby_sdkmessageprocessingstepsecureconfig)
- [createdby_sdkmessageprocessingstep](#BKMK_createdby_sdkmessageprocessingstep)
- [lk_appconfig_modifiedonbehalfby](#BKMK_lk_appconfig_modifiedonbehalfby)
- [lk_quarterlyfiscalcalendar_salespersonid](#BKMK_lk_quarterlyfiscalcalendar_salespersonid)
- [lk_transformationparametermapping_modifiedonbehalfby](#BKMK_lk_transformationparametermapping_modifiedonbehalfby)
- [lk_importentitymapping_createdonbehalfby](#BKMK_lk_importentitymapping_createdonbehalfby)
- [SystemUser_ProcessSessions](#BKMK_SystemUser_ProcessSessions)
- [lk_templatebase_createdonbehalfby](#BKMK_lk_templatebase_createdonbehalfby)
- [lk_lookupmapping_createdby](#BKMK_lk_lookupmapping_createdby)
- [lk_mobileofflineprofileitem_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby)
- [lk_processsessionbase_modifiedonbehalfby](#BKMK_lk_processsessionbase_modifiedonbehalfby)
- [lk_processsession_createdby](#BKMK_lk_processsession_createdby)
- [lk_personaldocumenttemplatebase_createdby](#BKMK_lk_personaldocumenttemplatebase_createdby)
- [lk_publisherbase_modifiedonbehalfby](#BKMK_lk_publisherbase_modifiedonbehalfby)
- [lk_MobileOfflineProfile_createdonbehalfby](#BKMK_lk_MobileOfflineProfile_createdonbehalfby)
- [lk_timezonerule_createdby](#BKMK_lk_timezonerule_createdby)
- [lk_contactbase_createdby](#BKMK_lk_contactbase_createdby)
- [lk_slakpiinstancebase_createdonbehalfby](#BKMK_lk_slakpiinstancebase_createdonbehalfby)
- [system_user_workflow](#BKMK_system_user_workflow)
- [lk_duplicaterulebase_createdby](#BKMK_lk_duplicaterulebase_createdby)
- [lk_appointment_createdonbehalfby](#BKMK_lk_appointment_createdonbehalfby)
- [createdby_connection_role](#BKMK_createdby_connection_role)
- [lk_appconfigmaster_modifiedby](#BKMK_lk_appconfigmaster_modifiedby)
- [lk_newprocess_modifiedby](#BKMK_lk_newprocess_modifiedby)
- [lk_columnmapping_modifiedonbehalfby](#BKMK_lk_columnmapping_modifiedonbehalfby)
- [lk_translationprocess_createdby](#BKMK_lk_translationprocess_createdby)
- [lk_monthlyfiscalcalendar_modifiedby](#BKMK_lk_monthlyfiscalcalendar_modifiedby)
- [lk_systemuserbase_modifiedby](#BKMK_lk_systemuserbase_modifiedby)
- [lk_expiredprocess_modifiedby](#BKMK_lk_expiredprocess_modifiedby)
- [lk_SocialProfile_createdonbehalfby](#BKMK_lk_SocialProfile_createdonbehalfby)
- [lk_importmap_createdonbehalfby](#BKMK_lk_importmap_createdonbehalfby)
- [modifiedby_connection](#BKMK_modifiedby_connection)
- [lk_import_createdonbehalfby](#BKMK_lk_import_createdonbehalfby)
- [lk_slaitembase_createdonbehalfby](#BKMK_lk_slaitembase_createdonbehalfby)
- [lk_navigationsetting_createdonbehalfby](#BKMK_lk_navigationsetting_createdonbehalfby)
- [lk_savedquery_modifiedonbehalfby](#BKMK_lk_savedquery_modifiedonbehalfby)
- [lk_solutioncomponentbase_modifiedonbehalfby](#BKMK_lk_solutioncomponentbase_modifiedonbehalfby)
- [lk_connectionrolebase_createdonbehalfby](#BKMK_lk_connectionrolebase_createdonbehalfby)
- [lk_actioncardbase_createdby](#BKMK_lk_actioncardbase_createdby)
- [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby)
- [lk_webresourcebase_modifiedonbehalfby](#BKMK_lk_webresourcebase_modifiedonbehalfby)
- [user_letter](#BKMK_user_letter)
- [lk_tracelog_modifiedonbehalfby](#BKMK_lk_tracelog_modifiedonbehalfby)
- [lk_timezonedefinition_createdby](#BKMK_lk_timezonedefinition_createdby)
- [lk_reportcategory_createdonbehalfby](#BKMK_lk_reportcategory_createdonbehalfby)
- [createdby_plugintype](#BKMK_createdby_plugintype)
- [lk_organization_createdonbehalfby](#BKMK_lk_organization_createdonbehalfby)
- [lk_calendar_modifiedonbehalfby](#BKMK_lk_calendar_modifiedonbehalfby)
- [lk_slakpiinstancebase_modifiedby](#BKMK_lk_slakpiinstancebase_modifiedby)
- [createdby_plugintracelog](#BKMK_createdby_plugintracelog)
- [lk_appconfiginstance_modifiedby](#BKMK_lk_appconfiginstance_modifiedby)
- [lk_picklistmapping_createdonbehalfby](#BKMK_lk_picklistmapping_createdonbehalfby)
- [lk_knowledgearticleviews_createdby](#BKMK_lk_knowledgearticleviews_createdby)
- [SystemUser_Imports](#BKMK_SystemUser_Imports)
- [modifiedby_sdkmessage](#BKMK_modifiedby_sdkmessage)
- [lk_ownermapping_createdonbehalfby](#BKMK_lk_ownermapping_createdonbehalfby)
- [lk_kbarticlecomment_createdonbehalfby](#BKMK_lk_kbarticlecomment_createdonbehalfby)
- [lk_navigationsetting_modifiedonbehalfby](#BKMK_lk_navigationsetting_modifiedonbehalfby)
- [lk_timezonerule_createdonbehalfby](#BKMK_lk_timezonerule_createdonbehalfby)
- [lk_templatebase_createdby](#BKMK_lk_templatebase_createdby)
- [lk_userformbase_modifiedonbehalfby](#BKMK_lk_userformbase_modifiedonbehalfby)
- [lk_mobileofflineprofileitemassociation_createdonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby)
- [lk_customeraddress_createdonbehalfby](#BKMK_lk_customeraddress_createdonbehalfby)
- [lk_importfilebase_modifiedby](#BKMK_lk_importfilebase_modifiedby)
- [lk_accountbase_modifiedby](#BKMK_lk_accountbase_modifiedby)
- [lk_personaldocumenttemplatebase_modifiedonbehalfby](#BKMK_lk_personaldocumenttemplatebase_modifiedonbehalfby)
- [lk_category_createdby](#BKMK_lk_category_createdby)
- [lk_customcontroldefaultconfig_modifiedby](#BKMK_lk_customcontroldefaultconfig_modifiedby)
- [lk_SocialProfile_modifiedonbehalfby](#BKMK_lk_SocialProfile_modifiedonbehalfby)
- [user_fax](#BKMK_user_fax)
- [lk_activitypointer_modifiedonbehalfby](#BKMK_lk_activitypointer_modifiedonbehalfby)
- [lk_feedback_createdonbehalfby](#BKMK_lk_feedback_createdonbehalfby)
- [lk_appmodulecomponent_createdby](#BKMK_lk_appmodulecomponent_createdby)
- [lk_sharepointsitebase_modifiedby](#BKMK_lk_sharepointsitebase_modifiedby)
- [lk_sdkmessageprocessingstepimage_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby)
- [lk_importlog_createdonbehalfby](#BKMK_lk_importlog_createdonbehalfby)
- [lk_processsession_executedby](#BKMK_lk_processsession_executedby)
- [lk_customcontrol_modifiedby](#BKMK_lk_customcontrol_modifiedby)
- [lk_customcontrolresource_createdonbehalfby](#BKMK_lk_customcontrolresource_createdonbehalfby)
- [SystemUser_DuplicateMatchingRecord](#BKMK_SystemUser_DuplicateMatchingRecord)
- [createdby_sdkmessageprocessingstepimage](#BKMK_createdby_sdkmessageprocessingstepimage)
- [lk_connectionbase_createdonbehalfby](#BKMK_lk_connectionbase_createdonbehalfby)
- [lk_customcontrol_createdby](#BKMK_lk_customcontrol_createdby)
- [lk_customcontrolresource_modifiedonbehalfby](#BKMK_lk_customcontrolresource_modifiedonbehalfby)
- [lk_timezonerule_modifiedby](#BKMK_lk_timezonerule_modifiedby)
- [lk_ACIViewMapper_createdonbehalfby](#BKMK_lk_ACIViewMapper_createdonbehalfby)
- [lk_audit_userid](#BKMK_lk_audit_userid)
- [lk_solutionbase_createdonbehalfby](#BKMK_lk_solutionbase_createdonbehalfby)
- [lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby)
- [OwnerMapping_SystemUser](#BKMK_OwnerMapping_SystemUser)
- [lk_columnmapping_modifiedby](#BKMK_lk_columnmapping_modifiedby)
- [lk_publisheraddressbase_modifiedby](#BKMK_lk_publisheraddressbase_modifiedby)
- [lk_accountbase_createdby](#BKMK_lk_accountbase_createdby)
- [lk_savedquerybase_modifiedby](#BKMK_lk_savedquerybase_modifiedby)
- [lk_MobileOfflineProfile_modifiedby](#BKMK_lk_MobileOfflineProfile_modifiedby)
- [lk_quarterlyfiscalcalendar_createdby](#BKMK_lk_quarterlyfiscalcalendar_createdby)
- [lk_timezonedefinition_modifiedonbehalfby](#BKMK_lk_timezonedefinition_modifiedonbehalfby)
- [lk_organization_modifiedonbehalfby](#BKMK_lk_organization_modifiedonbehalfby)
- [systemuser_connections1](#BKMK_systemuser_connections1)
- [lk_SiteMap_modifiedby](#BKMK_lk_SiteMap_modifiedby)
- [lk_documenttemplatebase_createdonbehalfby](#BKMK_lk_documenttemplatebase_createdonbehalfby)
- [lk_kbarticlebase_createdby](#BKMK_lk_kbarticlebase_createdby)
- [lk_emailserverprofile_createdby](#BKMK_lk_emailserverprofile_createdby)
- [lk_quarterlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby)
- [lk_userquery_modifiedby](#BKMK_lk_userquery_modifiedby)
- [lk_mobileofflineprofileitemassociation_modifiedby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedby)
- [lk_knowledgearticleviews_createdonbehalfby](#BKMK_lk_knowledgearticleviews_createdonbehalfby)
- [lk_processtriggerbase_createdonbehalfby](#BKMK_lk_processtriggerbase_createdonbehalfby)
- [modifiedby_sdkmessageprocessingstepimage](#BKMK_modifiedby_sdkmessageprocessingstepimage)
- [lk_phonecall_modifiedonbehalfby](#BKMK_lk_phonecall_modifiedonbehalfby)
- [lk_workflowlog_createdby](#BKMK_lk_workflowlog_createdby)
- [lk_fixedmonthlyfiscalcalendar_salespersonid](#BKMK_lk_fixedmonthlyfiscalcalendar_salespersonid)
- [lk_quarterlyfiscalcalendar_createdonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby)
- [lk_teamtemplate_modifiedby](#BKMK_lk_teamtemplate_modifiedby)
- [user_userform](#BKMK_user_userform)
- [lk_processsession_startedby](#BKMK_lk_processsession_startedby)
- [lk_knowledgearticleviews_modifiedonbehalfby](#BKMK_lk_knowledgearticleviews_modifiedonbehalfby)
- [lk_role_modifiedonbehalfby](#BKMK_lk_role_modifiedonbehalfby)
- [lk_reportbase_modifiedby](#BKMK_lk_reportbase_modifiedby)
- [lk_fixedmonthlyfiscalcalendar_createdby](#BKMK_lk_fixedmonthlyfiscalcalendar_createdby)
- [lk_appconfigmaster_createdby](#BKMK_lk_appconfigmaster_createdby)
- [lk_businessunitbase_modifiedby](#BKMK_lk_businessunitbase_modifiedby)
- [socialProfile_owning_user](#BKMK_socialProfile_owning_user)
- [lk_task_modifiedby](#BKMK_lk_task_modifiedby)
- [lk_slaitembase_createdby](#BKMK_lk_slaitembase_createdby)
- [lk_mailboxtrackingfolder_createdonbehalfby](#BKMK_lk_mailboxtrackingfolder_createdonbehalfby)
- [modifiedby_sdkmessageprocessingstep](#BKMK_modifiedby_sdkmessageprocessingstep)
- [lk_duplicaterulebase_modifiedby](#BKMK_lk_duplicaterulebase_modifiedby)
- [lk_recurrencerulebase_createdonbehalfby](#BKMK_lk_recurrencerulebase_createdonbehalfby)
- [lk_organizationbase_modifiedby](#BKMK_lk_organizationbase_modifiedby)
- [lk_mailboxtrackingfolder_modifiedonbehalfby](#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby)
- [lk_task_createdby](#BKMK_lk_task_createdby)
- [lk_mailboxtrackingfolder_createdby](#BKMK_lk_mailboxtrackingfolder_createdby)
- [lk_personaldocumenttemplatebase_modifiedby](#BKMK_lk_personaldocumenttemplatebase_modifiedby)
- [lk_processtriggerbase_modifiedby](#BKMK_lk_processtriggerbase_modifiedby)
- [lk_userquery_createdby](#BKMK_lk_userquery_createdby)
- [contact_owning_user](#BKMK_contact_owning_user)
- [lk_mailmergetemplate_createdonbehalfby](#BKMK_lk_mailmergetemplate_createdonbehalfby)
- [lk_importjobbase_modifiedonbehalfby](#BKMK_lk_importjobbase_modifiedonbehalfby)
- [lk_customcontroldefaultconfig_createdby](#BKMK_lk_customcontroldefaultconfig_createdby)
- [lk_savedquery_createdonbehalfby](#BKMK_lk_savedquery_createdonbehalfby)
- [system_user_accounts](#BKMK_system_user_accounts)
- [lk_systemuser_createdonbehalfby](#BKMK_lk_systemuser_createdonbehalfby)
- [lk_customcontrol_modifiedonbehalfby](#BKMK_lk_customcontrol_modifiedonbehalfby)
- [lk_appointment_modifiedonbehalfby](#BKMK_lk_appointment_modifiedonbehalfby)
- [lk_knowledgearticleviews_modifiedby](#BKMK_lk_knowledgearticleviews_modifiedby)
- [lk_appconfigmaster_modifiedonbehalfby](#BKMK_lk_appconfigmaster_modifiedonbehalfby)
- [lk_importbase_createdby](#BKMK_lk_importbase_createdby)
- [lk_ACIViewMapper_modifiedonbehalfby](#BKMK_lk_ACIViewMapper_modifiedonbehalfby)
- [lk_solutionbase_modifiedonbehalfby](#BKMK_lk_solutionbase_modifiedonbehalfby)
- [lk_DisplayStringbase_modifiedonbehalfby](#BKMK_lk_DisplayStringbase_modifiedonbehalfby)
- [lk_annotationbase_modifiedby](#BKMK_lk_annotationbase_modifiedby)
- [lk_timezonerule_modifiedonbehalfby](#BKMK_lk_timezonerule_modifiedonbehalfby)
- [lk_importjobbase_createdby](#BKMK_lk_importjobbase_createdby)
- [lk_feedback_createdby](#BKMK_lk_feedback_createdby)
- [lk_timezonelocalizedname_modifiedby](#BKMK_lk_timezonelocalizedname_modifiedby)
- [lk_mailmergetemplatebase_createdby](#BKMK_lk_mailmergetemplatebase_createdby)
- [createdby_pluginassembly](#BKMK_createdby_pluginassembly)
- [lk_appconfiginstance_modifiedonbehalfby](#BKMK_lk_appconfiginstance_modifiedonbehalfby)
- [lk_userform_modifiedby](#BKMK_lk_userform_modifiedby)
- [lk_publisherbase_createdonbehalfby](#BKMK_lk_publisherbase_createdonbehalfby)
- [lk_recurrencerule_createdby](#BKMK_lk_recurrencerule_createdby)
- [lk_slakpiinstancebase_modifiedonbehalfby](#BKMK_lk_slakpiinstancebase_modifiedonbehalfby)
- [SystemUser_ImportFiles](#BKMK_SystemUser_ImportFiles)
- [lk_processsession_modifiedby](#BKMK_lk_processsession_modifiedby)
- [lk_translationprocess_modifiedby](#BKMK_lk_translationprocess_modifiedby)
- [lk_annualfiscalcalendar_modifiedby](#BKMK_lk_annualfiscalcalendar_modifiedby)
- [user_task](#BKMK_user_task)
- [lk_recurrencerulebase_modifiedonbehalfby](#BKMK_lk_recurrencerulebase_modifiedonbehalfby)
- [lk_phonecall_createdby](#BKMK_lk_phonecall_createdby)
- [lk_templatebase_modifiedonbehalfby](#BKMK_lk_templatebase_modifiedonbehalfby)
- [lk_fax_modifiedonbehalfby](#BKMK_lk_fax_modifiedonbehalfby)
- [lk_contact_createdonbehalfby](#BKMK_lk_contact_createdonbehalfby)
- [lk_customcontroldefaultconfig_createdonbehalfby](#BKMK_lk_customcontroldefaultconfig_createdonbehalfby)
- [lk_publisheraddressbase_createdonbehalfby](#BKMK_lk_publisheraddressbase_createdonbehalfby)
- [lk_annualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_modifiedby](#BKMK_lk_semiannualfiscalcalendar_modifiedby)
- [lk_socialactivity_createdby](#BKMK_lk_socialactivity_createdby)
- [lk_SiteMap_createdby](#BKMK_lk_SiteMap_createdby)
- [lk_syncerrorbase_modifiedby](#BKMK_lk_syncerrorbase_modifiedby)
- [lk_calendar_createdby](#BKMK_lk_calendar_createdby)
- [lk_semiannualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby)
- [lk_fixedmonthlyfiscalcalendar_modifiedby](#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedby)
- [SystemUser_DuplicateBaseRecord](#BKMK_SystemUser_DuplicateBaseRecord)
- [lk_importentitymapping_createdby](#BKMK_lk_importentitymapping_createdby)
- [lk_queueitembase_createdby](#BKMK_lk_queueitembase_createdby)
- [lk_sdkmessage_createdonbehalfby](#BKMK_lk_sdkmessage_createdonbehalfby)
- [createdby_plugintypestatistic](#BKMK_createdby_plugintypestatistic)
- [lk_picklistmapping_modifiedby](#BKMK_lk_picklistmapping_modifiedby)
- [lk_team_modifiedonbehalfby](#BKMK_lk_team_modifiedonbehalfby)
- [lk_businessunitnewsarticle_modifiedonbehalfby](#BKMK_lk_businessunitnewsarticle_modifiedonbehalfby)
- [SystemUser_ImportLogs](#BKMK_SystemUser_ImportLogs)
- [lk_plugintypestatisticbase_modifiedonbehalfby](#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby)
- [lk_tracelog_createdby](#BKMK_lk_tracelog_createdby)
- [lk_teambase_administratorid](#BKMK_lk_teambase_administratorid)
- [lk_savedqueryvisualizationbase_createdby](#BKMK_lk_savedqueryvisualizationbase_createdby)
- [knowledgearticle_primaryauthorid](#BKMK_knowledgearticle_primaryauthorid)
- [lk_fixedmonthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_fixedmonthlyfiscalcalendar_createdonbehalfby)
- [lk_email_createdby](#BKMK_lk_email_createdby)
- [lk_monthlyfiscalcalendar_createdby](#BKMK_lk_monthlyfiscalcalendar_createdby)
- [lk_queuebase_createdby](#BKMK_lk_queuebase_createdby)
- [lk_appmodulecomponent_createdonbehalfby](#BKMK_lk_appmodulecomponent_createdonbehalfby)
- [lk_personaldocumenttemplatebase_createdonbehalfby](#BKMK_lk_personaldocumenttemplatebase_createdonbehalfby)
- [lk_savedqueryvisualizationbase_createdonbehalfby](#BKMK_lk_savedqueryvisualizationbase_createdonbehalfby)
- [lk_newprocess_createdby](#BKMK_lk_newprocess_createdby)
- [lk_category_createdonbehalfby](#BKMK_lk_category_createdonbehalfby)
- [lk_newprocess_modifiedonbehalfby](#BKMK_lk_newprocess_modifiedonbehalfby)
- [lk_feedback_closedby](#BKMK_lk_feedback_closedby)
- [lk_semiannualfiscalcalendar_createdby](#BKMK_lk_semiannualfiscalcalendar_createdby)
- [lk_duplicateruleconditionbase_modifiedby](#BKMK_lk_duplicateruleconditionbase_modifiedby)
- [queue_primary_user](#BKMK_queue_primary_user)
- [user_email](#BKMK_user_email)
- [lk_reportbase_createdby](#BKMK_lk_reportbase_createdby)
- [lk_appointment_createdby](#BKMK_lk_appointment_createdby)
- [lk_letter_modifiedby](#BKMK_lk_letter_modifiedby)
- [lk_customcontrol_createdonbehalfby](#BKMK_lk_customcontrol_createdonbehalfby)
- [lk_usersettingsbase_modifiedby](#BKMK_lk_usersettingsbase_modifiedby)
- [lk_queueitembase_modifiedby](#BKMK_lk_queueitembase_modifiedby)
- [lk_sdkmessageprocessingstep_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby)
- [modifiedby_pluginassembly](#BKMK_modifiedby_pluginassembly)
- [lk_sharepointdocumentlocationbase_modifiedby](#BKMK_lk_sharepointdocumentlocationbase_modifiedby)
- [system_user_activity_parties](#BKMK_system_user_activity_parties)
- [lk_annualfiscalcalendar_salespersonid](#BKMK_lk_annualfiscalcalendar_salespersonid)
- [SystemUser_AsyncOperations](#BKMK_SystemUser_AsyncOperations)
- [lk_publisheraddressbase_createdby](#BKMK_lk_publisheraddressbase_createdby)
- [lk_import_modifiedonbehalfby](#BKMK_lk_import_modifiedonbehalfby)
- [lk_queuebase_modifiedby](#BKMK_lk_queuebase_modifiedby)
- [SystemUser_ImportMaps](#BKMK_SystemUser_ImportMaps)
- [workflow_modifiedonbehalfby](#BKMK_workflow_modifiedonbehalfby)
- [lk_category_modifiedby](#BKMK_lk_category_modifiedby)
- [lk_SiteMap_createdonbehalfby](#BKMK_lk_SiteMap_createdonbehalfby)
- [webresource_modifiedby](#BKMK_webresource_modifiedby)
- [createdby_sdkmessage](#BKMK_createdby_sdkmessage)
- [lk_importlogbase_modifiedby](#BKMK_lk_importlogbase_modifiedby)
- [lk_importjobbase_createdonbehalfby](#BKMK_lk_importjobbase_createdonbehalfby)
- [lk_monthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby)
- [lk_transactioncurrency_createdonbehalfby](#BKMK_lk_transactioncurrency_createdonbehalfby)
- [lk_bulkdeleteoperation_createdonbehalfby](#BKMK_lk_bulkdeleteoperation_createdonbehalfby)
- [modifiedby_plugintypestatistic](#BKMK_modifiedby_plugintypestatistic)
- [lk_actioncardbase_modifiedonbehalfby](#BKMK_lk_actioncardbase_modifiedonbehalfby)
- [lk_recurringappointmentmaster_createdby](#BKMK_lk_recurringappointmentmaster_createdby)
- [lk_DisplayStringbase_createdonbehalfby](#BKMK_lk_DisplayStringbase_createdonbehalfby)
- [lk_audit_callinguserid](#BKMK_lk_audit_callinguserid)
- [lk_importfilebase_createdby](#BKMK_lk_importfilebase_createdby)
- [lk_importmap_modifiedonbehalfby](#BKMK_lk_importmap_modifiedonbehalfby)
- [lk_expiredprocess_modifiedonbehalfby](#BKMK_lk_expiredprocess_modifiedonbehalfby)
- [lk_userqueryvisualizationbase_modifiedonbehalfby](#BKMK_lk_userqueryvisualizationbase_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_salespersonid](#BKMK_lk_semiannualfiscalcalendar_salespersonid)
- [lk_report_createdonbehalfby](#BKMK_lk_report_createdonbehalfby)
- [lk_processsession_canceledby](#BKMK_lk_processsession_canceledby)
- [lk_SiteMap_modifiedonbehalfby](#BKMK_lk_SiteMap_modifiedonbehalfby)
- [SystemUser_SyncError](#BKMK_SystemUser_SyncError)
- [lk_socialactivity_modifiedby](#BKMK_lk_socialactivity_modifiedby)
- [lk_accountbase_modifiedonbehalfby](#BKMK_lk_accountbase_modifiedonbehalfby)
- [lk_subjectbase_createdby](#BKMK_lk_subjectbase_createdby)
- [lk_MobileOfflineProfile_modifiedonbehalfby](#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby)
- [lk_annotationbase_modifiedonbehalfby](#BKMK_lk_annotationbase_modifiedonbehalfby)
- [lk_kbarticletemplatebase_createdby](#BKMK_lk_kbarticletemplatebase_createdby)
- [lk_importbase_modifiedby](#BKMK_lk_importbase_modifiedby)
- [modifiedby_connection_role](#BKMK_modifiedby_connection_role)
- [lk_sharepointdocumentlocationbase_createdonbehalfby](#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby)
- [lk_mailmergetemplatebase_modifiedby](#BKMK_lk_mailmergetemplatebase_modifiedby)
- [lk_userquery_createdonbehalfby](#BKMK_lk_userquery_createdonbehalfby)
- [lk_transactioncurrencybase_createdby](#BKMK_lk_transactioncurrencybase_createdby)
- [lk_queue_createdonbehalfby](#BKMK_lk_queue_createdonbehalfby)
- [lk_MobileOfflineProfile_createdby](#BKMK_lk_MobileOfflineProfile_createdby)
- [modifiedby_serviceendpoint](#BKMK_modifiedby_serviceendpoint)
- [lk_appointment_modifiedby](#BKMK_lk_appointment_modifiedby)
- [lk_picklistmapping_modifiedonbehalfby](#BKMK_lk_picklistmapping_modifiedonbehalfby)
- [lk_transformationmapping_createdonbehalfby](#BKMK_lk_transformationmapping_createdonbehalfby)
- [lk_plugintypestatisticbase_createdonbehalfby](#BKMK_lk_plugintypestatisticbase_createdonbehalfby)
- [lk_kbarticletemplate_createdonbehalfby](#BKMK_lk_kbarticletemplate_createdonbehalfby)
- [ImportFile_SystemUser](#BKMK_ImportFile_SystemUser)
- [lk_importmapbase_modifiedby](#BKMK_lk_importmapbase_modifiedby)
- [lk_userform_createdby](#BKMK_lk_userform_createdby)
- [lk_expiredprocess_createdby](#BKMK_lk_expiredprocess_createdby)
- [lk_userqueryvisualization_createdby](#BKMK_lk_userqueryvisualization_createdby)
- [lk_ACIViewMapper_modifiedby](#BKMK_lk_ACIViewMapper_modifiedby)
- [user_slabase](#BKMK_user_slabase)
- [lk_annotationbase_createdby](#BKMK_lk_annotationbase_createdby)
- [webresource_createdby](#BKMK_webresource_createdby)
- [lk_userqueryvisualizationbase_createdonbehalfby](#BKMK_lk_userqueryvisualizationbase_createdonbehalfby)
- [lk_usersettings_modifiedonbehalfby](#BKMK_lk_usersettings_modifiedonbehalfby)
- [user_parent_user](#BKMK_user_parent_user)
- [lk_appconfiginstance_createdby](#BKMK_lk_appconfiginstance_createdby)
- [lk_annualfiscalcalendar_createdonbehalfby](#BKMK_lk_annualfiscalcalendar_createdonbehalfby)
- [lk_userformbase_createdonbehalfby](#BKMK_lk_userformbase_createdonbehalfby)
- [lk_fieldsecurityprofile_createdby](#BKMK_lk_fieldsecurityprofile_createdby)
- [lk_asyncoperation_modifiedby](#BKMK_lk_asyncoperation_modifiedby)
- [lk_pluginassembly_createdonbehalfby](#BKMK_lk_pluginassembly_createdonbehalfby)
- [lk_importentitymapping_modifiedby](#BKMK_lk_importentitymapping_modifiedby)
- [lk_sdkmessageprocessingstep_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby)
- [lk_activitypointer_createdonbehalfby](#BKMK_lk_activitypointer_createdonbehalfby)
- [lk_contact_modifiedonbehalfby](#BKMK_lk_contact_modifiedonbehalfby)
- [lk_savedqueryvisualizationbase_modifiedonbehalfby](#BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby)
- [lk_accountbase_createdonbehalfby](#BKMK_lk_accountbase_createdonbehalfby)
- [modifiedby_sdkmessagefilter](#BKMK_modifiedby_sdkmessagefilter)
- [system_user_email_templates](#BKMK_system_user_email_templates)
- [lk_ownermapping_modifiedonbehalfby](#BKMK_lk_ownermapping_modifiedonbehalfby)
- [lk_systemuser_modifiedonbehalfby](#BKMK_lk_systemuser_modifiedonbehalfby)
- [lk_annualfiscalcalendar_createdby](#BKMK_lk_annualfiscalcalendar_createdby)
- [lk_email_createdonbehalfby](#BKMK_lk_email_createdonbehalfby)
- [lk_recurringappointmentmaster_modifiedonbehalfby](#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby)
- [lk_timezonelocalizedname_createdby](#BKMK_lk_timezonelocalizedname_createdby)
- [lk_bulkdeleteoperationbase_modifiedby](#BKMK_lk_bulkdeleteoperationbase_modifiedby)
- [lk_sharepointsitebase_modifiedonbehalfby](#BKMK_lk_sharepointsitebase_modifiedonbehalfby)
- [lk_ownermapping_modifiedby](#BKMK_lk_ownermapping_modifiedby)
- [lk_sharepointsitebase_createdby](#BKMK_lk_sharepointsitebase_createdby)
- [lk_actioncardbase_modifiedby](#BKMK_lk_actioncardbase_modifiedby)
- [lk_webresourcebase_createdonbehalfby](#BKMK_lk_webresourcebase_createdonbehalfby)
- [lk_connectionrolebase_modifiedonbehalfby](#BKMK_lk_connectionrolebase_modifiedonbehalfby)
- [lk_timezonelocalizedname_modifiedonbehalfby](#BKMK_lk_timezonelocalizedname_modifiedonbehalfby)
- [lk_transformationmapping_modifiedonbehalfby](#BKMK_lk_transformationmapping_modifiedonbehalfby)
- [lk_documenttemplatebase_modifiedonbehalfby](#BKMK_lk_documenttemplatebase_modifiedonbehalfby)
- [user_phonecall](#BKMK_user_phonecall)
- [lk_serviceendpointbase_modifiedonbehalfby](#BKMK_lk_serviceendpointbase_modifiedonbehalfby)
- [lk_slabase_createdonbehalfby](#BKMK_lk_slabase_createdonbehalfby)
- [lk_importjobbase_modifiedby](#BKMK_lk_importjobbase_modifiedby)
- [lk_MobileOfflineProfileItemAssociation_createdby](#BKMK_lk_MobileOfflineProfileItemAssociation_createdby)
- [lk_processtriggerbase_createdby](#BKMK_lk_processtriggerbase_createdby)
- [lk_timezonedefinition_createdonbehalfby](#BKMK_lk_timezonedefinition_createdonbehalfby)
- [lk_kbarticlecomment_modifiedonbehalfby](#BKMK_lk_kbarticlecomment_modifiedonbehalfby)
- [lk_timezonelocalizedname_createdonbehalfby](#BKMK_lk_timezonelocalizedname_createdonbehalfby)
- [lk_systemuserbase_createdby](#BKMK_lk_systemuserbase_createdby)
- [systemuser_principalobjectattributeaccess](#BKMK_systemuser_principalobjectattributeaccess)
- [system_user_asyncoperation](#BKMK_system_user_asyncoperation)
- [lk_plugintracelogbase_createdonbehalfby](#BKMK_lk_plugintracelogbase_createdonbehalfby)
- [lk_teamtemplate_createdby](#BKMK_lk_teamtemplate_createdby)
- [lk_annotationbase_createdonbehalfby](#BKMK_lk_annotationbase_createdonbehalfby)
- [lk_fieldsecurityprofile_modifiedonbehalfby](#BKMK_lk_fieldsecurityprofile_modifiedonbehalfby)
- [lk_appmodulecomponent_modifiedonbehalfby](#BKMK_lk_appmodulecomponent_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_createdonbehalfby](#BKMK_lk_semiannualfiscalcalendar_createdonbehalfby)
- [lk_userquery_modifiedonbehalfby](#BKMK_lk_userquery_modifiedonbehalfby)
- [lk_businessunitnewsarticlebase_createdby](#BKMK_lk_businessunitnewsarticlebase_createdby)
- [systemuser_connections2](#BKMK_systemuser_connections2)
- [lk_task_createdonbehalfby](#BKMK_lk_task_createdonbehalfby)
- [lk_contactbase_modifiedby](#BKMK_lk_contactbase_modifiedby)
- [lk_letter_createdonbehalfby](#BKMK_lk_letter_createdonbehalfby)
- [lk_customcontrolresource_createdby](#BKMK_lk_customcontrolresource_createdby)
- [lk_socialactivitybase_modifiedonbehalfby](#BKMK_lk_socialactivitybase_modifiedonbehalfby)
- [lk_socialactivitybase_createdonbehalfby](#BKMK_lk_socialactivitybase_createdonbehalfby)
- [lk_importfilebase_modifiedonbehalfby](#BKMK_lk_importfilebase_modifiedonbehalfby)
- [lk_fieldsecurityprofile_modifiedby](#BKMK_lk_fieldsecurityprofile_modifiedby)
- [lk_newprocess_createdonbehalfby](#BKMK_lk_newprocess_createdonbehalfby)
- [lk_appconfig_createdby](#BKMK_lk_appconfig_createdby)
- [lk_businessunitbase_createdby](#BKMK_lk_businessunitbase_createdby)
- [lk_monthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby)
- [lk_sharepointdocumentlocationbase_modifiedonbehalfby](#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby)
- [lk_syncerrorbase_createdby](#BKMK_lk_syncerrorbase_createdby)
- [createdby_sdkmessagefilter](#BKMK_createdby_sdkmessagefilter)
- [lk_kbarticlebase_modifiedby](#BKMK_lk_kbarticlebase_modifiedby)
- [lk_ownermapping_createdby](#BKMK_lk_ownermapping_createdby)
- [SystemUser_SyncErrors](#BKMK_SystemUser_SyncErrors)
- [lk_duplicateruleconditionbase_createdby](#BKMK_lk_duplicateruleconditionbase_createdby)
- [lk_callbackregistration_modifiedonbehalfby](#BKMK_lk_callbackregistration_modifiedonbehalfby)
- [lk_callbackregistration_modifiedby](#BKMK_lk_callbackregistration_modifiedby)
- [lk_callbackregistration_createdonbehalfby](#BKMK_lk_callbackregistration_createdonbehalfby)
- [lk_callbackregistration_createdby](#BKMK_lk_callbackregistration_createdby)
- [lk_solutioncomponentattributeconfiguration_createdby](#BKMK_lk_solutioncomponentattributeconfiguration_createdby)
- [lk_solutioncomponentattributeconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentattributeconfiguration_createdonbehalfby)
- [lk_solutioncomponentattributeconfiguration_modifiedby](#BKMK_lk_solutioncomponentattributeconfiguration_modifiedby)
- [lk_solutioncomponentattributeconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentattributeconfiguration_modifiedonbehalfby)
- [lk_solutioncomponentbatchconfiguration_createdby](#BKMK_lk_solutioncomponentbatchconfiguration_createdby)
- [lk_solutioncomponentbatchconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentbatchconfiguration_createdonbehalfby)
- [lk_solutioncomponentbatchconfiguration_modifiedby](#BKMK_lk_solutioncomponentbatchconfiguration_modifiedby)
- [lk_solutioncomponentbatchconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentbatchconfiguration_modifiedonbehalfby)
- [user_solutioncomponentbatchconfiguration](#BKMK_user_solutioncomponentbatchconfiguration)
- [lk_solutioncomponentconfiguration_createdby](#BKMK_lk_solutioncomponentconfiguration_createdby)
- [lk_solutioncomponentconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentconfiguration_createdonbehalfby)
- [lk_solutioncomponentconfiguration_modifiedby](#BKMK_lk_solutioncomponentconfiguration_modifiedby)
- [lk_solutioncomponentconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby)
- [lk_solutioncomponentrelationshipconfiguration_createdby](#BKMK_lk_solutioncomponentrelationshipconfiguration_createdby)
- [lk_solutioncomponentrelationshipconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby)
- [lk_solutioncomponentrelationshipconfiguration_modifiedby](#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby)
- [lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby)
- [lk_package_createdby](#BKMK_lk_package_createdby)
- [lk_package_createdonbehalfby](#BKMK_lk_package_createdonbehalfby)
- [lk_package_modifiedby](#BKMK_lk_package_modifiedby)
- [lk_package_modifiedonbehalfby](#BKMK_lk_package_modifiedonbehalfby)
- [lk_stagesolutionupload_createdby](#BKMK_lk_stagesolutionupload_createdby)
- [lk_stagesolutionupload_createdonbehalfby](#BKMK_lk_stagesolutionupload_createdonbehalfby)
- [lk_stagesolutionupload_modifiedby](#BKMK_lk_stagesolutionupload_modifiedby)
- [lk_stagesolutionupload_modifiedonbehalfby](#BKMK_lk_stagesolutionupload_modifiedonbehalfby)
- [user_stagesolutionupload](#BKMK_user_stagesolutionupload)
- [lk_exportsolutionupload_createdby](#BKMK_lk_exportsolutionupload_createdby)
- [lk_exportsolutionupload_createdonbehalfby](#BKMK_lk_exportsolutionupload_createdonbehalfby)
- [lk_exportsolutionupload_modifiedby](#BKMK_lk_exportsolutionupload_modifiedby)
- [lk_exportsolutionupload_modifiedonbehalfby](#BKMK_lk_exportsolutionupload_modifiedonbehalfby)
- [user_exportsolutionupload](#BKMK_user_exportsolutionupload)
- [lk_featurecontrolsetting_createdby](#BKMK_lk_featurecontrolsetting_createdby)
- [lk_featurecontrolsetting_createdonbehalfby](#BKMK_lk_featurecontrolsetting_createdonbehalfby)
- [lk_featurecontrolsetting_modifiedby](#BKMK_lk_featurecontrolsetting_modifiedby)
- [lk_featurecontrolsetting_modifiedonbehalfby](#BKMK_lk_featurecontrolsetting_modifiedonbehalfby)
- [user_featurecontrolsetting](#BKMK_user_featurecontrolsetting)
- [lk_catalog_createdby](#BKMK_lk_catalog_createdby)
- [lk_catalog_createdonbehalfby](#BKMK_lk_catalog_createdonbehalfby)
- [lk_catalog_modifiedby](#BKMK_lk_catalog_modifiedby)
- [lk_catalog_modifiedonbehalfby](#BKMK_lk_catalog_modifiedonbehalfby)
- [lk_catalogassignment_createdby](#BKMK_lk_catalogassignment_createdby)
- [lk_catalogassignment_createdonbehalfby](#BKMK_lk_catalogassignment_createdonbehalfby)
- [lk_catalogassignment_modifiedby](#BKMK_lk_catalogassignment_modifiedby)
- [lk_catalogassignment_modifiedonbehalfby](#BKMK_lk_catalogassignment_modifiedonbehalfby)
- [lk_customapi_createdby](#BKMK_lk_customapi_createdby)
- [lk_customapi_createdonbehalfby](#BKMK_lk_customapi_createdonbehalfby)
- [lk_customapi_modifiedby](#BKMK_lk_customapi_modifiedby)
- [lk_customapi_modifiedonbehalfby](#BKMK_lk_customapi_modifiedonbehalfby)
- [user_customapi](#BKMK_user_customapi)
- [lk_customapirequestparameter_createdby](#BKMK_lk_customapirequestparameter_createdby)
- [lk_customapirequestparameter_createdonbehalfby](#BKMK_lk_customapirequestparameter_createdonbehalfby)
- [lk_customapirequestparameter_modifiedby](#BKMK_lk_customapirequestparameter_modifiedby)
- [lk_customapirequestparameter_modifiedonbehalfby](#BKMK_lk_customapirequestparameter_modifiedonbehalfby)
- [user_customapirequestparameter](#BKMK_user_customapirequestparameter)
- [lk_customapiresponseproperty_createdby](#BKMK_lk_customapiresponseproperty_createdby)
- [lk_customapiresponseproperty_createdonbehalfby](#BKMK_lk_customapiresponseproperty_createdonbehalfby)
- [lk_customapiresponseproperty_modifiedby](#BKMK_lk_customapiresponseproperty_modifiedby)
- [lk_customapiresponseproperty_modifiedonbehalfby](#BKMK_lk_customapiresponseproperty_modifiedonbehalfby)
- [user_customapiresponseproperty](#BKMK_user_customapiresponseproperty)
- [lk_datalakefolder_createdby](#BKMK_lk_datalakefolder_createdby)
- [lk_datalakefolder_createdonbehalfby](#BKMK_lk_datalakefolder_createdonbehalfby)
- [lk_datalakefolder_modifiedby](#BKMK_lk_datalakefolder_modifiedby)
- [lk_datalakefolder_modifiedonbehalfby](#BKMK_lk_datalakefolder_modifiedonbehalfby)
- [user_datalakefolder](#BKMK_user_datalakefolder)
- [lk_datalakefolderpermission_createdby](#BKMK_lk_datalakefolderpermission_createdby)
- [lk_datalakefolderpermission_createdonbehalfby](#BKMK_lk_datalakefolderpermission_createdonbehalfby)
- [lk_datalakefolderpermission_modifiedby](#BKMK_lk_datalakefolderpermission_modifiedby)
- [lk_datalakefolderpermission_modifiedonbehalfby](#BKMK_lk_datalakefolderpermission_modifiedonbehalfby)
- [user_datalakefolderpermission](#BKMK_user_datalakefolderpermission)
- [lk_datalakeworkspace_createdby](#BKMK_lk_datalakeworkspace_createdby)
- [lk_datalakeworkspace_createdonbehalfby](#BKMK_lk_datalakeworkspace_createdonbehalfby)
- [lk_datalakeworkspace_modifiedby](#BKMK_lk_datalakeworkspace_modifiedby)
- [lk_datalakeworkspace_modifiedonbehalfby](#BKMK_lk_datalakeworkspace_modifiedonbehalfby)
- [lk_datalakeworkspacepermission_createdby](#BKMK_lk_datalakeworkspacepermission_createdby)
- [lk_datalakeworkspacepermission_createdonbehalfby](#BKMK_lk_datalakeworkspacepermission_createdonbehalfby)
- [lk_datalakeworkspacepermission_modifiedby](#BKMK_lk_datalakeworkspacepermission_modifiedby)
- [lk_datalakeworkspacepermission_modifiedonbehalfby](#BKMK_lk_datalakeworkspacepermission_modifiedonbehalfby)
- [lk_msdyn_dataflow_createdby](#BKMK_lk_msdyn_dataflow_createdby)
- [lk_msdyn_dataflow_createdonbehalfby](#BKMK_lk_msdyn_dataflow_createdonbehalfby)
- [lk_msdyn_dataflow_modifiedby](#BKMK_lk_msdyn_dataflow_modifiedby)
- [lk_msdyn_dataflow_modifiedonbehalfby](#BKMK_lk_msdyn_dataflow_modifiedonbehalfby)
- [user_msdyn_dataflow](#BKMK_user_msdyn_dataflow)
- [lk_serviceplan_createdby](#BKMK_lk_serviceplan_createdby)
- [lk_serviceplan_createdonbehalfby](#BKMK_lk_serviceplan_createdonbehalfby)
- [lk_serviceplan_modifiedby](#BKMK_lk_serviceplan_modifiedby)
- [lk_serviceplan_modifiedonbehalfby](#BKMK_lk_serviceplan_modifiedonbehalfby)
- [lk_serviceplanmapping_createdby](#BKMK_lk_serviceplanmapping_createdby)
- [lk_serviceplanmapping_createdonbehalfby](#BKMK_lk_serviceplanmapping_createdonbehalfby)
- [lk_serviceplanmapping_modifiedby](#BKMK_lk_serviceplanmapping_modifiedby)
- [lk_serviceplanmapping_modifiedonbehalfby](#BKMK_lk_serviceplanmapping_modifiedonbehalfby)
- [lk_applicationuser_createdby](#BKMK_lk_applicationuser_createdby)
- [lk_applicationuser_createdonbehalfby](#BKMK_lk_applicationuser_createdonbehalfby)
- [lk_applicationuser_modifiedby](#BKMK_lk_applicationuser_modifiedby)
- [lk_applicationuser_modifiedonbehalfby](#BKMK_lk_applicationuser_modifiedonbehalfby)
- [lk_connector_createdby](#BKMK_lk_connector_createdby)
- [lk_connector_createdonbehalfby](#BKMK_lk_connector_createdonbehalfby)
- [lk_connector_modifiedby](#BKMK_lk_connector_modifiedby)
- [lk_connector_modifiedonbehalfby](#BKMK_lk_connector_modifiedonbehalfby)
- [user_connector](#BKMK_user_connector)
- [lk_environmentvariabledefinition_createdby](#BKMK_lk_environmentvariabledefinition_createdby)
- [lk_environmentvariabledefinition_createdonbehalfby](#BKMK_lk_environmentvariabledefinition_createdonbehalfby)
- [lk_environmentvariabledefinition_modifiedby](#BKMK_lk_environmentvariabledefinition_modifiedby)
- [lk_environmentvariabledefinition_modifiedonbehalfby](#BKMK_lk_environmentvariabledefinition_modifiedonbehalfby)
- [user_environmentvariabledefinition](#BKMK_user_environmentvariabledefinition)
- [lk_environmentvariablevalue_createdby](#BKMK_lk_environmentvariablevalue_createdby)
- [lk_environmentvariablevalue_createdonbehalfby](#BKMK_lk_environmentvariablevalue_createdonbehalfby)
- [lk_environmentvariablevalue_modifiedby](#BKMK_lk_environmentvariablevalue_modifiedby)
- [lk_environmentvariablevalue_modifiedonbehalfby](#BKMK_lk_environmentvariablevalue_modifiedonbehalfby)
- [user_environmentvariablevalue](#BKMK_user_environmentvariablevalue)
- [lk_flowmachine_createdby](#BKMK_lk_flowmachine_createdby)
- [lk_flowmachine_createdonbehalfby](#BKMK_lk_flowmachine_createdonbehalfby)
- [lk_flowmachine_modifiedby](#BKMK_lk_flowmachine_modifiedby)
- [lk_flowmachine_modifiedonbehalfby](#BKMK_lk_flowmachine_modifiedonbehalfby)
- [user_flowmachine](#BKMK_user_flowmachine)
- [lk_flowmachinegroup_createdby](#BKMK_lk_flowmachinegroup_createdby)
- [lk_flowmachinegroup_createdonbehalfby](#BKMK_lk_flowmachinegroup_createdonbehalfby)
- [lk_flowmachinegroup_modifiedby](#BKMK_lk_flowmachinegroup_modifiedby)
- [lk_flowmachinegroup_modifiedonbehalfby](#BKMK_lk_flowmachinegroup_modifiedonbehalfby)
- [user_flowmachinegroup](#BKMK_user_flowmachinegroup)
- [lk_processstageparameter_createdby](#BKMK_lk_processstageparameter_createdby)
- [lk_processstageparameter_createdonbehalfby](#BKMK_lk_processstageparameter_createdonbehalfby)
- [lk_processstageparameter_modifiedby](#BKMK_lk_processstageparameter_modifiedby)
- [lk_processstageparameter_modifiedonbehalfby](#BKMK_lk_processstageparameter_modifiedonbehalfby)
- [user_processstageparameter](#BKMK_user_processstageparameter)
- [lk_flowsession_createdby](#BKMK_lk_flowsession_createdby)
- [lk_flowsession_createdonbehalfby](#BKMK_lk_flowsession_createdonbehalfby)
- [lk_flowsession_modifiedby](#BKMK_lk_flowsession_modifiedby)
- [lk_flowsession_modifiedonbehalfby](#BKMK_lk_flowsession_modifiedonbehalfby)
- [user_flowsession](#BKMK_user_flowsession)
- [lk_workflowbinary_createdby](#BKMK_lk_workflowbinary_createdby)
- [lk_workflowbinary_createdonbehalfby](#BKMK_lk_workflowbinary_createdonbehalfby)
- [lk_workflowbinary_modifiedby](#BKMK_lk_workflowbinary_modifiedby)
- [lk_workflowbinary_modifiedonbehalfby](#BKMK_lk_workflowbinary_modifiedonbehalfby)
- [user_workflowbinary](#BKMK_user_workflowbinary)
- [lk_connectionreference_createdby](#BKMK_lk_connectionreference_createdby)
- [lk_connectionreference_createdonbehalfby](#BKMK_lk_connectionreference_createdonbehalfby)
- [lk_connectionreference_modifiedby](#BKMK_lk_connectionreference_modifiedby)
- [lk_connectionreference_modifiedonbehalfby](#BKMK_lk_connectionreference_modifiedonbehalfby)
- [user_connectionreference](#BKMK_user_connectionreference)
- [lk_msdyn_aiconfiguration_createdby](#BKMK_lk_msdyn_aiconfiguration_createdby)
- [lk_msdyn_aiconfiguration_createdonbehalfby](#BKMK_lk_msdyn_aiconfiguration_createdonbehalfby)
- [lk_msdyn_aiconfiguration_modifiedby](#BKMK_lk_msdyn_aiconfiguration_modifiedby)
- [lk_msdyn_aiconfiguration_modifiedonbehalfby](#BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby)
- [user_msdyn_aiconfiguration](#BKMK_user_msdyn_aiconfiguration)
- [lk_msdyn_aimodel_createdby](#BKMK_lk_msdyn_aimodel_createdby)
- [lk_msdyn_aimodel_createdonbehalfby](#BKMK_lk_msdyn_aimodel_createdonbehalfby)
- [lk_msdyn_aimodel_modifiedby](#BKMK_lk_msdyn_aimodel_modifiedby)
- [lk_msdyn_aimodel_modifiedonbehalfby](#BKMK_lk_msdyn_aimodel_modifiedonbehalfby)
- [user_msdyn_aimodel](#BKMK_user_msdyn_aimodel)
- [lk_msdyn_aitemplate_createdby](#BKMK_lk_msdyn_aitemplate_createdby)
- [lk_msdyn_aitemplate_createdonbehalfby](#BKMK_lk_msdyn_aitemplate_createdonbehalfby)
- [lk_msdyn_aitemplate_modifiedby](#BKMK_lk_msdyn_aitemplate_modifiedby)
- [lk_msdyn_aitemplate_modifiedonbehalfby](#BKMK_lk_msdyn_aitemplate_modifiedonbehalfby)
- [user_msdyn_aitemplate](#BKMK_user_msdyn_aitemplate)
- [lk_msdyn_aifptrainingdocument_createdby](#BKMK_lk_msdyn_aifptrainingdocument_createdby)
- [lk_msdyn_aifptrainingdocument_createdonbehalfby](#BKMK_lk_msdyn_aifptrainingdocument_createdonbehalfby)
- [lk_msdyn_aifptrainingdocument_modifiedby](#BKMK_lk_msdyn_aifptrainingdocument_modifiedby)
- [lk_msdyn_aifptrainingdocument_modifiedonbehalfby](#BKMK_lk_msdyn_aifptrainingdocument_modifiedonbehalfby)
- [user_msdyn_aifptrainingdocument](#BKMK_user_msdyn_aifptrainingdocument)
- [lk_msdyn_aiodimage_createdby](#BKMK_lk_msdyn_aiodimage_createdby)
- [lk_msdyn_aiodimage_createdonbehalfby](#BKMK_lk_msdyn_aiodimage_createdonbehalfby)
- [lk_msdyn_aiodimage_modifiedby](#BKMK_lk_msdyn_aiodimage_modifiedby)
- [lk_msdyn_aiodimage_modifiedonbehalfby](#BKMK_lk_msdyn_aiodimage_modifiedonbehalfby)
- [user_msdyn_aiodimage](#BKMK_user_msdyn_aiodimage)
- [lk_msdyn_aiodlabel_createdby](#BKMK_lk_msdyn_aiodlabel_createdby)
- [lk_msdyn_aiodlabel_createdonbehalfby](#BKMK_lk_msdyn_aiodlabel_createdonbehalfby)
- [lk_msdyn_aiodlabel_modifiedby](#BKMK_lk_msdyn_aiodlabel_modifiedby)
- [lk_msdyn_aiodlabel_modifiedonbehalfby](#BKMK_lk_msdyn_aiodlabel_modifiedonbehalfby)
- [user_msdyn_aiodlabel](#BKMK_user_msdyn_aiodlabel)
- [lk_msdyn_aiodtrainingboundingbox_createdby](#BKMK_lk_msdyn_aiodtrainingboundingbox_createdby)
- [lk_msdyn_aiodtrainingboundingbox_createdonbehalfby](#BKMK_lk_msdyn_aiodtrainingboundingbox_createdonbehalfby)
- [lk_msdyn_aiodtrainingboundingbox_modifiedby](#BKMK_lk_msdyn_aiodtrainingboundingbox_modifiedby)
- [lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby](#BKMK_lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby)
- [user_msdyn_aiodtrainingboundingbox](#BKMK_user_msdyn_aiodtrainingboundingbox)
- [lk_msdyn_aiodtrainingimage_createdby](#BKMK_lk_msdyn_aiodtrainingimage_createdby)
- [lk_msdyn_aiodtrainingimage_createdonbehalfby](#BKMK_lk_msdyn_aiodtrainingimage_createdonbehalfby)
- [lk_msdyn_aiodtrainingimage_modifiedby](#BKMK_lk_msdyn_aiodtrainingimage_modifiedby)
- [lk_msdyn_aiodtrainingimage_modifiedonbehalfby](#BKMK_lk_msdyn_aiodtrainingimage_modifiedonbehalfby)
- [user_msdyn_aiodtrainingimage](#BKMK_user_msdyn_aiodtrainingimage)
- [lk_msdyn_aibdataset_createdby](#BKMK_lk_msdyn_aibdataset_createdby)
- [lk_msdyn_aibdataset_createdonbehalfby](#BKMK_lk_msdyn_aibdataset_createdonbehalfby)
- [lk_msdyn_aibdataset_modifiedby](#BKMK_lk_msdyn_aibdataset_modifiedby)
- [lk_msdyn_aibdataset_modifiedonbehalfby](#BKMK_lk_msdyn_aibdataset_modifiedonbehalfby)
- [user_msdyn_aibdataset](#BKMK_user_msdyn_aibdataset)
- [lk_msdyn_aibdatasetfile_createdby](#BKMK_lk_msdyn_aibdatasetfile_createdby)
- [lk_msdyn_aibdatasetfile_createdonbehalfby](#BKMK_lk_msdyn_aibdatasetfile_createdonbehalfby)
- [lk_msdyn_aibdatasetfile_modifiedby](#BKMK_lk_msdyn_aibdatasetfile_modifiedby)
- [lk_msdyn_aibdatasetfile_modifiedonbehalfby](#BKMK_lk_msdyn_aibdatasetfile_modifiedonbehalfby)
- [user_msdyn_aibdatasetfile](#BKMK_user_msdyn_aibdatasetfile)
- [lk_msdyn_aibdatasetrecord_createdby](#BKMK_lk_msdyn_aibdatasetrecord_createdby)
- [lk_msdyn_aibdatasetrecord_createdonbehalfby](#BKMK_lk_msdyn_aibdatasetrecord_createdonbehalfby)
- [lk_msdyn_aibdatasetrecord_modifiedby](#BKMK_lk_msdyn_aibdatasetrecord_modifiedby)
- [lk_msdyn_aibdatasetrecord_modifiedonbehalfby](#BKMK_lk_msdyn_aibdatasetrecord_modifiedonbehalfby)
- [user_msdyn_aibdatasetrecord](#BKMK_user_msdyn_aibdatasetrecord)
- [lk_msdyn_aibdatasetscontainer_createdby](#BKMK_lk_msdyn_aibdatasetscontainer_createdby)
- [lk_msdyn_aibdatasetscontainer_createdonbehalfby](#BKMK_lk_msdyn_aibdatasetscontainer_createdonbehalfby)
- [lk_msdyn_aibdatasetscontainer_modifiedby](#BKMK_lk_msdyn_aibdatasetscontainer_modifiedby)
- [lk_msdyn_aibdatasetscontainer_modifiedonbehalfby](#BKMK_lk_msdyn_aibdatasetscontainer_modifiedonbehalfby)
- [user_msdyn_aibdatasetscontainer](#BKMK_user_msdyn_aibdatasetscontainer)
- [lk_msdyn_aibfile_createdby](#BKMK_lk_msdyn_aibfile_createdby)
- [lk_msdyn_aibfile_createdonbehalfby](#BKMK_lk_msdyn_aibfile_createdonbehalfby)
- [lk_msdyn_aibfile_modifiedby](#BKMK_lk_msdyn_aibfile_modifiedby)
- [lk_msdyn_aibfile_modifiedonbehalfby](#BKMK_lk_msdyn_aibfile_modifiedonbehalfby)
- [user_msdyn_aibfile](#BKMK_user_msdyn_aibfile)
- [lk_msdyn_aibfileattacheddata_createdby](#BKMK_lk_msdyn_aibfileattacheddata_createdby)
- [lk_msdyn_aibfileattacheddata_createdonbehalfby](#BKMK_lk_msdyn_aibfileattacheddata_createdonbehalfby)
- [lk_msdyn_aibfileattacheddata_modifiedby](#BKMK_lk_msdyn_aibfileattacheddata_modifiedby)
- [lk_msdyn_aibfileattacheddata_modifiedonbehalfby](#BKMK_lk_msdyn_aibfileattacheddata_modifiedonbehalfby)
- [user_msdyn_aibfileattacheddata](#BKMK_user_msdyn_aibfileattacheddata)
- [lk_msdyn_helppage_createdby](#BKMK_lk_msdyn_helppage_createdby)
- [lk_msdyn_helppage_createdonbehalfby](#BKMK_lk_msdyn_helppage_createdonbehalfby)
- [lk_msdyn_helppage_modifiedby](#BKMK_lk_msdyn_helppage_modifiedby)
- [lk_msdyn_helppage_modifiedonbehalfby](#BKMK_lk_msdyn_helppage_modifiedonbehalfby)
- [lk_msdyn_tour_createdby](#BKMK_lk_msdyn_tour_createdby)
- [lk_msdyn_tour_createdonbehalfby](#BKMK_lk_msdyn_tour_createdonbehalfby)
- [lk_msdyn_tour_modifiedby](#BKMK_lk_msdyn_tour_modifiedby)
- [lk_msdyn_tour_modifiedonbehalfby](#BKMK_lk_msdyn_tour_modifiedonbehalfby)
- [lk_msdynce_botcontent_createdby](#BKMK_lk_msdynce_botcontent_createdby)
- [lk_msdynce_botcontent_createdonbehalfby](#BKMK_lk_msdynce_botcontent_createdonbehalfby)
- [lk_msdynce_botcontent_modifiedby](#BKMK_lk_msdynce_botcontent_modifiedby)
- [lk_msdynce_botcontent_modifiedonbehalfby](#BKMK_lk_msdynce_botcontent_modifiedonbehalfby)
- [user_msdynce_botcontent](#BKMK_user_msdynce_botcontent)
- [lk_conversationtranscript_createdby](#BKMK_lk_conversationtranscript_createdby)
- [lk_conversationtranscript_createdonbehalfby](#BKMK_lk_conversationtranscript_createdonbehalfby)
- [lk_conversationtranscript_modifiedby](#BKMK_lk_conversationtranscript_modifiedby)
- [lk_conversationtranscript_modifiedonbehalfby](#BKMK_lk_conversationtranscript_modifiedonbehalfby)
- [user_conversationtranscript](#BKMK_user_conversationtranscript)
- [lk_bot_createdby](#BKMK_lk_bot_createdby)
- [lk_bot_createdonbehalfby](#BKMK_lk_bot_createdonbehalfby)
- [lk_bot_modifiedby](#BKMK_lk_bot_modifiedby)
- [lk_bot_modifiedonbehalfby](#BKMK_lk_bot_modifiedonbehalfby)
- [user_bot](#BKMK_user_bot)
- [lk_botcomponent_createdby](#BKMK_lk_botcomponent_createdby)
- [lk_botcomponent_createdonbehalfby](#BKMK_lk_botcomponent_createdonbehalfby)
- [lk_botcomponent_modifiedby](#BKMK_lk_botcomponent_modifiedby)
- [lk_botcomponent_modifiedonbehalfby](#BKMK_lk_botcomponent_modifiedonbehalfby)
- [user_botcomponent](#BKMK_user_botcomponent)
- [systemuser_bot_publishedby](#BKMK_systemuser_bot_publishedby)
- [lk_territorybase_createdby](#BKMK_lk_territorybase_createdby)
- [lk_territory_createdonbehalfby](#BKMK_lk_territory_createdonbehalfby)
- [lk_territorybase_modifiedby](#BKMK_lk_territorybase_modifiedby)
- [lk_territory_modifiedonbehalfby](#BKMK_lk_territory_modifiedonbehalfby)
- [system_user_territories](#BKMK_system_user_territories)
- [lk_activityfileattachment_createdby](#BKMK_lk_activityfileattachment_createdby)
- [lk_activityfileattachment_createdonbehalfby](#BKMK_lk_activityfileattachment_createdonbehalfby)
- [lk_activityfileattachment_modifiedby](#BKMK_lk_activityfileattachment_modifiedby)
- [lk_activityfileattachment_modifiedonbehalfby](#BKMK_lk_activityfileattachment_modifiedonbehalfby)
- [user_activityfileattachment](#BKMK_user_activityfileattachment)
- [lk_msdyn_serviceconfiguration_createdby](#BKMK_lk_msdyn_serviceconfiguration_createdby)
- [lk_msdyn_serviceconfiguration_createdonbehalfby](#BKMK_lk_msdyn_serviceconfiguration_createdonbehalfby)
- [lk_msdyn_serviceconfiguration_modifiedby](#BKMK_lk_msdyn_serviceconfiguration_modifiedby)
- [lk_msdyn_serviceconfiguration_modifiedonbehalfby](#BKMK_lk_msdyn_serviceconfiguration_modifiedonbehalfby)
- [user_msdyn_serviceconfiguration](#BKMK_user_msdyn_serviceconfiguration)
- [lk_msdyn_slakpi_createdby](#BKMK_lk_msdyn_slakpi_createdby)
- [lk_msdyn_slakpi_createdonbehalfby](#BKMK_lk_msdyn_slakpi_createdonbehalfby)
- [lk_msdyn_slakpi_modifiedby](#BKMK_lk_msdyn_slakpi_modifiedby)
- [lk_msdyn_slakpi_modifiedonbehalfby](#BKMK_lk_msdyn_slakpi_modifiedonbehalfby)
- [user_msdyn_slakpi](#BKMK_user_msdyn_slakpi)
- [lk_msdyn_federatedarticle_createdby](#BKMK_lk_msdyn_federatedarticle_createdby)
- [lk_msdyn_federatedarticle_createdonbehalfby](#BKMK_lk_msdyn_federatedarticle_createdonbehalfby)
- [lk_msdyn_federatedarticle_modifiedby](#BKMK_lk_msdyn_federatedarticle_modifiedby)
- [lk_msdyn_federatedarticle_modifiedonbehalfby](#BKMK_lk_msdyn_federatedarticle_modifiedonbehalfby)
- [user_msdyn_federatedarticle](#BKMK_user_msdyn_federatedarticle)
- [lk_msdyn_federatedarticleincident_createdby](#BKMK_lk_msdyn_federatedarticleincident_createdby)
- [lk_msdyn_federatedarticleincident_createdonbehalfby](#BKMK_lk_msdyn_federatedarticleincident_createdonbehalfby)
- [lk_msdyn_federatedarticleincident_modifiedby](#BKMK_lk_msdyn_federatedarticleincident_modifiedby)
- [lk_msdyn_federatedarticleincident_modifiedonbehalfby](#BKMK_lk_msdyn_federatedarticleincident_modifiedonbehalfby)
- [lk_msdyn_kmfederatedsearchconfig_createdby](#BKMK_lk_msdyn_kmfederatedsearchconfig_createdby)
- [lk_msdyn_kmfederatedsearchconfig_createdonbehalfby](#BKMK_lk_msdyn_kmfederatedsearchconfig_createdonbehalfby)
- [lk_msdyn_kmfederatedsearchconfig_modifiedby](#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedby)
- [lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby](#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby)
- [user_msdyn_kmfederatedsearchconfig](#BKMK_user_msdyn_kmfederatedsearchconfig)
- [lk_msdyn_knowledgearticleimage_createdby](#BKMK_lk_msdyn_knowledgearticleimage_createdby)
- [lk_msdyn_knowledgearticleimage_createdonbehalfby](#BKMK_lk_msdyn_knowledgearticleimage_createdonbehalfby)
- [lk_msdyn_knowledgearticleimage_modifiedby](#BKMK_lk_msdyn_knowledgearticleimage_modifiedby)
- [lk_msdyn_knowledgearticleimage_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgearticleimage_modifiedonbehalfby)
- [user_msdyn_knowledgearticleimage](#BKMK_user_msdyn_knowledgearticleimage)
- [lk_msdyn_knowledgeinteractioninsight_createdby](#BKMK_lk_msdyn_knowledgeinteractioninsight_createdby)
- [lk_msdyn_knowledgeinteractioninsight_createdonbehalfby](#BKMK_lk_msdyn_knowledgeinteractioninsight_createdonbehalfby)
- [lk_msdyn_knowledgeinteractioninsight_modifiedby](#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedby)
- [lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby)
- [user_msdyn_knowledgeinteractioninsight](#BKMK_user_msdyn_knowledgeinteractioninsight)
- [lk_msdyn_knowledgesearchinsight_createdby](#BKMK_lk_msdyn_knowledgesearchinsight_createdby)
- [lk_msdyn_knowledgesearchinsight_createdonbehalfby](#BKMK_lk_msdyn_knowledgesearchinsight_createdonbehalfby)
- [lk_msdyn_knowledgesearchinsight_modifiedby](#BKMK_lk_msdyn_knowledgesearchinsight_modifiedby)
- [lk_msdyn_knowledgesearchinsight_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgesearchinsight_modifiedonbehalfby)
- [user_msdyn_knowledgesearchinsight](#BKMK_user_msdyn_knowledgesearchinsight)
- [lk_msdyn_kalanguagesetting_createdby](#BKMK_lk_msdyn_kalanguagesetting_createdby)
- [lk_msdyn_kalanguagesetting_createdonbehalfby](#BKMK_lk_msdyn_kalanguagesetting_createdonbehalfby)
- [lk_msdyn_kalanguagesetting_modifiedby](#BKMK_lk_msdyn_kalanguagesetting_modifiedby)
- [lk_msdyn_kalanguagesetting_modifiedonbehalfby](#BKMK_lk_msdyn_kalanguagesetting_modifiedonbehalfby)
- [user_msdyn_kalanguagesetting](#BKMK_user_msdyn_kalanguagesetting)
- [lk_msdyn_kbattachment_createdby](#BKMK_lk_msdyn_kbattachment_createdby)
- [lk_msdyn_kbattachment_createdonbehalfby](#BKMK_lk_msdyn_kbattachment_createdonbehalfby)
- [lk_msdyn_kbattachment_modifiedby](#BKMK_lk_msdyn_kbattachment_modifiedby)
- [lk_msdyn_kbattachment_modifiedonbehalfby](#BKMK_lk_msdyn_kbattachment_modifiedonbehalfby)
- [user_msdyn_kbattachment](#BKMK_user_msdyn_kbattachment)
- [lk_msdyn_kmpersonalizationsetting_createdby](#BKMK_lk_msdyn_kmpersonalizationsetting_createdby)
- [lk_msdyn_kmpersonalizationsetting_createdonbehalfby](#BKMK_lk_msdyn_kmpersonalizationsetting_createdonbehalfby)
- [lk_msdyn_kmpersonalizationsetting_modifiedby](#BKMK_lk_msdyn_kmpersonalizationsetting_modifiedby)
- [lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby](#BKMK_lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby)
- [lk_msdyn_knowledgearticletemplate_createdby](#BKMK_lk_msdyn_knowledgearticletemplate_createdby)
- [lk_msdyn_knowledgearticletemplate_createdonbehalfby](#BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby)
- [lk_msdyn_knowledgearticletemplate_modifiedby](#BKMK_lk_msdyn_knowledgearticletemplate_modifiedby)
- [lk_msdyn_knowledgearticletemplate_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby)
- [user_msdyn_knowledgearticletemplate](#BKMK_user_msdyn_knowledgearticletemplate)
- [lk_msdyn_knowledgepersonalfilter_createdby](#BKMK_lk_msdyn_knowledgepersonalfilter_createdby)
- [lk_msdyn_knowledgepersonalfilter_createdonbehalfby](#BKMK_lk_msdyn_knowledgepersonalfilter_createdonbehalfby)
- [lk_msdyn_knowledgepersonalfilter_modifiedby](#BKMK_lk_msdyn_knowledgepersonalfilter_modifiedby)
- [lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby)
- [user_msdyn_knowledgepersonalfilter](#BKMK_user_msdyn_knowledgepersonalfilter)
- [lk_msdyn_knowledgesearchfilter_createdby](#BKMK_lk_msdyn_knowledgesearchfilter_createdby)
- [lk_msdyn_knowledgesearchfilter_createdonbehalfby](#BKMK_lk_msdyn_knowledgesearchfilter_createdonbehalfby)
- [lk_msdyn_knowledgesearchfilter_modifiedby](#BKMK_lk_msdyn_knowledgesearchfilter_modifiedby)
- [lk_msdyn_knowledgesearchfilter_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgesearchfilter_modifiedonbehalfby)
- [user_msdyn_knowledgesearchfilter](#BKMK_user_msdyn_knowledgesearchfilter)
- [lk_pluginpackage_createdby](#BKMK_lk_pluginpackage_createdby)
- [lk_pluginpackage_createdonbehalfby](#BKMK_lk_pluginpackage_createdonbehalfby)
- [lk_pluginpackage_modifiedby](#BKMK_lk_pluginpackage_modifiedby)
- [lk_pluginpackage_modifiedonbehalfby](#BKMK_lk_pluginpackage_modifiedonbehalfby)
- [lk_keyvaultreference_createdby](#BKMK_lk_keyvaultreference_createdby)
- [lk_keyvaultreference_createdonbehalfby](#BKMK_lk_keyvaultreference_createdonbehalfby)
- [lk_keyvaultreference_modifiedby](#BKMK_lk_keyvaultreference_modifiedby)
- [lk_keyvaultreference_modifiedonbehalfby](#BKMK_lk_keyvaultreference_modifiedonbehalfby)
- [user_keyvaultreference](#BKMK_user_keyvaultreference)
- [lk_managedidentity_createdby](#BKMK_lk_managedidentity_createdby)
- [lk_managedidentity_createdonbehalfby](#BKMK_lk_managedidentity_createdonbehalfby)
- [lk_managedidentity_modifiedby](#BKMK_lk_managedidentity_modifiedby)
- [lk_managedidentity_modifiedonbehalfby](#BKMK_lk_managedidentity_modifiedonbehalfby)
- [user_managedidentity](#BKMK_user_managedidentity)
- [email_acceptingentity_systemuser](#BKMK_email_acceptingentity_systemuser)
- [lk_virtualentitymetadata_createdby](#BKMK_lk_virtualentitymetadata_createdby)
- [lk_virtualentitymetadata_createdonbehalfby](#BKMK_lk_virtualentitymetadata_createdonbehalfby)
- [lk_virtualentitymetadata_modifiedby](#BKMK_lk_virtualentitymetadata_modifiedby)
- [lk_virtualentitymetadata_modifiedonbehalfby](#BKMK_lk_virtualentitymetadata_modifiedonbehalfby)
- [lk_organizationdatasyncsubscription_createdby](#BKMK_lk_organizationdatasyncsubscription_createdby)
- [lk_organizationdatasyncsubscription_createdonbehalfby](#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby)
- [lk_organizationdatasyncsubscription_modifiedby](#BKMK_lk_organizationdatasyncsubscription_modifiedby)
- [lk_organizationdatasyncsubscription_modifiedonbehalfby](#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby)
- [lk_organizationdatasyncsubscriptionentity_createdby](#BKMK_lk_organizationdatasyncsubscriptionentity_createdby)
- [lk_organizationdatasyncsubscriptionentity_createdonbehalfby](#BKMK_lk_organizationdatasyncsubscriptionentity_createdonbehalfby)
- [lk_organizationdatasyncsubscriptionentity_modifiedby](#BKMK_lk_organizationdatasyncsubscriptionentity_modifiedby)
- [lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby](#BKMK_lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby)
- [lk_appnotification_createdby](#BKMK_lk_appnotification_createdby)
- [lk_appnotification_createdonbehalfby](#BKMK_lk_appnotification_createdonbehalfby)
- [lk_appnotification_modifiedby](#BKMK_lk_appnotification_modifiedby)
- [lk_appnotification_modifiedonbehalfby](#BKMK_lk_appnotification_modifiedonbehalfby)
- [user_appnotification](#BKMK_user_appnotification)
- [lk_appaction_createdby](#BKMK_lk_appaction_createdby)
- [lk_appaction_createdonbehalfby](#BKMK_lk_appaction_createdonbehalfby)
- [lk_appaction_modifiedby](#BKMK_lk_appaction_modifiedby)
- [lk_appaction_modifiedonbehalfby](#BKMK_lk_appaction_modifiedonbehalfby)
- [lk_msdyn_richtextfile_createdby](#BKMK_lk_msdyn_richtextfile_createdby)
- [lk_msdyn_richtextfile_createdonbehalfby](#BKMK_lk_msdyn_richtextfile_createdonbehalfby)
- [lk_msdyn_richtextfile_modifiedby](#BKMK_lk_msdyn_richtextfile_modifiedby)
- [lk_msdyn_richtextfile_modifiedonbehalfby](#BKMK_lk_msdyn_richtextfile_modifiedonbehalfby)
- [user_msdyn_richtextfile](#BKMK_user_msdyn_richtextfile)
- [lk_msdyn_pminferredtask_createdby](#BKMK_lk_msdyn_pminferredtask_createdby)
- [lk_msdyn_pminferredtask_createdonbehalfby](#BKMK_lk_msdyn_pminferredtask_createdonbehalfby)
- [lk_msdyn_pminferredtask_modifiedby](#BKMK_lk_msdyn_pminferredtask_modifiedby)
- [lk_msdyn_pminferredtask_modifiedonbehalfby](#BKMK_lk_msdyn_pminferredtask_modifiedonbehalfby)
- [user_msdyn_pminferredtask](#BKMK_user_msdyn_pminferredtask)
- [lk_msdyn_pmrecording_createdby](#BKMK_lk_msdyn_pmrecording_createdby)
- [lk_msdyn_pmrecording_createdonbehalfby](#BKMK_lk_msdyn_pmrecording_createdonbehalfby)
- [lk_msdyn_pmrecording_modifiedby](#BKMK_lk_msdyn_pmrecording_modifiedby)
- [lk_msdyn_pmrecording_modifiedonbehalfby](#BKMK_lk_msdyn_pmrecording_modifiedonbehalfby)
- [user_msdyn_pmrecording](#BKMK_user_msdyn_pmrecording)
- [lk_msdyn_analysiscomponent_createdby](#BKMK_lk_msdyn_analysiscomponent_createdby)
- [lk_msdyn_analysiscomponent_createdonbehalfby](#BKMK_lk_msdyn_analysiscomponent_createdonbehalfby)
- [lk_msdyn_analysiscomponent_modifiedby](#BKMK_lk_msdyn_analysiscomponent_modifiedby)
- [lk_msdyn_analysiscomponent_modifiedonbehalfby](#BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby)
- [user_msdyn_analysiscomponent](#BKMK_user_msdyn_analysiscomponent)
- [lk_msdyn_analysisjob_createdby](#BKMK_lk_msdyn_analysisjob_createdby)
- [lk_msdyn_analysisjob_createdonbehalfby](#BKMK_lk_msdyn_analysisjob_createdonbehalfby)
- [lk_msdyn_analysisjob_modifiedby](#BKMK_lk_msdyn_analysisjob_modifiedby)
- [lk_msdyn_analysisjob_modifiedonbehalfby](#BKMK_lk_msdyn_analysisjob_modifiedonbehalfby)
- [user_msdyn_analysisjob](#BKMK_user_msdyn_analysisjob)
- [lk_msdyn_analysisresult_createdby](#BKMK_lk_msdyn_analysisresult_createdby)
- [lk_msdyn_analysisresult_createdonbehalfby](#BKMK_lk_msdyn_analysisresult_createdonbehalfby)
- [lk_msdyn_analysisresult_modifiedby](#BKMK_lk_msdyn_analysisresult_modifiedby)
- [lk_msdyn_analysisresult_modifiedonbehalfby](#BKMK_lk_msdyn_analysisresult_modifiedonbehalfby)
- [user_msdyn_analysisresult](#BKMK_user_msdyn_analysisresult)
- [lk_msdyn_analysisresultdetail_createdby](#BKMK_lk_msdyn_analysisresultdetail_createdby)
- [lk_msdyn_analysisresultdetail_createdonbehalfby](#BKMK_lk_msdyn_analysisresultdetail_createdonbehalfby)
- [lk_msdyn_analysisresultdetail_modifiedby](#BKMK_lk_msdyn_analysisresultdetail_modifiedby)
- [lk_msdyn_analysisresultdetail_modifiedonbehalfby](#BKMK_lk_msdyn_analysisresultdetail_modifiedonbehalfby)
- [user_msdyn_analysisresultdetail](#BKMK_user_msdyn_analysisresultdetail)
- [lk_msdyn_solutionhealthrule_createdby](#BKMK_lk_msdyn_solutionhealthrule_createdby)
- [lk_msdyn_solutionhealthrule_createdonbehalfby](#BKMK_lk_msdyn_solutionhealthrule_createdonbehalfby)
- [lk_msdyn_solutionhealthrule_modifiedby](#BKMK_lk_msdyn_solutionhealthrule_modifiedby)
- [lk_msdyn_solutionhealthrule_modifiedonbehalfby](#BKMK_lk_msdyn_solutionhealthrule_modifiedonbehalfby)
- [user_msdyn_solutionhealthrule](#BKMK_user_msdyn_solutionhealthrule)
- [lk_msdyn_solutionhealthruleargument_createdby](#BKMK_lk_msdyn_solutionhealthruleargument_createdby)
- [lk_msdyn_solutionhealthruleargument_createdonbehalfby](#BKMK_lk_msdyn_solutionhealthruleargument_createdonbehalfby)
- [lk_msdyn_solutionhealthruleargument_modifiedby](#BKMK_lk_msdyn_solutionhealthruleargument_modifiedby)
- [lk_msdyn_solutionhealthruleargument_modifiedonbehalfby](#BKMK_lk_msdyn_solutionhealthruleargument_modifiedonbehalfby)
- [user_msdyn_solutionhealthruleargument](#BKMK_user_msdyn_solutionhealthruleargument)
- [lk_msdyn_solutionhealthruleset_createdby](#BKMK_lk_msdyn_solutionhealthruleset_createdby)
- [lk_msdyn_solutionhealthruleset_createdonbehalfby](#BKMK_lk_msdyn_solutionhealthruleset_createdonbehalfby)
- [lk_msdyn_solutionhealthruleset_modifiedby](#BKMK_lk_msdyn_solutionhealthruleset_modifiedby)
- [lk_msdyn_solutionhealthruleset_modifiedonbehalfby](#BKMK_lk_msdyn_solutionhealthruleset_modifiedonbehalfby)


### <a name="BKMK_lk_appmodule_modifiedby"></a> lk_appmodule_modifiedby

Same as appmodule table [lk_appmodule_modifiedby](appmodule.md#BKMK_lk_appmodule_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodule|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appmodule_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuser_principalobjectattributeaccess_principalid"></a> systemuser_principalobjectattributeaccess_principalid

Same as principalobjectattributeaccess table [systemuser_principalobjectattributeaccess_principalid](principalobjectattributeaccess.md#BKMK_systemuser_principalobjectattributeaccess_principalid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|principalid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|systemuser_principalobjectattributeaccess_principalid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_exchangesyncidmapping"></a> user_exchangesyncidmapping

Same as exchangesyncidmapping table [user_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_user_exchangesyncidmapping) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exchangesyncidmapping|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_exchangesyncidmapping|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_theme_createdby"></a> lk_theme_createdby

Same as theme table [lk_theme_createdby](theme.md#BKMK_lk_theme_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|theme|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_theme_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_theme_createdonbehalfby"></a> lk_theme_createdonbehalfby

Same as theme table [lk_theme_createdonbehalfby](theme.md#BKMK_lk_theme_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|theme|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_theme_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_theme_modifiedby"></a> lk_theme_modifiedby

Same as theme table [lk_theme_modifiedby](theme.md#BKMK_lk_theme_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|theme|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_theme_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_theme_modifiedonbehalfby"></a> lk_theme_modifiedonbehalfby

Same as theme table [lk_theme_modifiedonbehalfby](theme.md#BKMK_lk_theme_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|theme|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_theme_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usermapping_createdby"></a> lk_usermapping_createdby

Same as usermapping table [lk_usermapping_createdby](usermapping.md#BKMK_lk_usermapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usermapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_usermapping_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usermapping_createdonbehalfby"></a> lk_usermapping_createdonbehalfby

Same as usermapping table [lk_usermapping_createdonbehalfby](usermapping.md#BKMK_lk_usermapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usermapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_usermapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usermapping_modifiedby"></a> lk_usermapping_modifiedby

Same as usermapping table [lk_usermapping_modifiedby](usermapping.md#BKMK_lk_usermapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usermapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_usermapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usermapping_modifiedonbehalfby"></a> lk_usermapping_modifiedonbehalfby

Same as usermapping table [lk_usermapping_modifiedonbehalfby](usermapping.md#BKMK_lk_usermapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usermapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_usermapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_interactionforemail_createdby"></a> lk_interactionforemail_createdby

Same as interactionforemail table [lk_interactionforemail_createdby](interactionforemail.md#BKMK_lk_interactionforemail_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_new_interactionforemail_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_interactionforemail_createdonbehalfby"></a> lk_interactionforemail_createdonbehalfby

Same as interactionforemail table [lk_interactionforemail_createdonbehalfby](interactionforemail.md#BKMK_lk_interactionforemail_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_new_interactionforemail_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_interactionforemail_modifiedby"></a> lk_interactionforemail_modifiedby

Same as interactionforemail table [lk_interactionforemail_modifiedby](interactionforemail.md#BKMK_lk_interactionforemail_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_new_interactionforemail_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_interactionforemail_modifiedonbehalfby"></a> lk_interactionforemail_modifiedonbehalfby

Same as interactionforemail table [lk_interactionforemail_modifiedonbehalfby](interactionforemail.md#BKMK_lk_interactionforemail_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_new_interactionforemail_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_interactionforemail"></a> user_interactionforemail

Same as interactionforemail table [user_interactionforemail](interactionforemail.md#BKMK_user_interactionforemail) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_new_interactionforemail|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticle_createdby"></a> lk_knowledgearticle_createdby

Same as knowledgearticle table [lk_knowledgearticle_createdby](knowledgearticle.md#BKMK_lk_knowledgearticle_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticle_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticle_createdonbehalfby"></a> lk_knowledgearticle_createdonbehalfby

Same as knowledgearticle table [lk_knowledgearticle_createdonbehalfby](knowledgearticle.md#BKMK_lk_knowledgearticle_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticle_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticle_modifiedby"></a> lk_knowledgearticle_modifiedby

Same as knowledgearticle table [lk_knowledgearticle_modifiedby](knowledgearticle.md#BKMK_lk_knowledgearticle_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticle_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticle_modifiedonbehalfby"></a> lk_knowledgearticle_modifiedonbehalfby

Same as knowledgearticle table [lk_knowledgearticle_modifiedonbehalfby](knowledgearticle.md#BKMK_lk_knowledgearticle_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticle_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_knowledgearticle"></a> user_knowledgearticle

Same as knowledgearticle table [user_knowledgearticle](knowledgearticle.md#BKMK_user_knowledgearticle) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_knowledgearticle|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_sharepointsite"></a> user_sharepointsite

Same as sharepointsite table [user_sharepointsite](sharepointsite.md#BKMK_user_sharepointsite) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_sharepointsite|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_sharepointdocumentlocation"></a> user_sharepointdocumentlocation

Same as sharepointdocumentlocation table [user_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_user_sharepointdocumentlocation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_sharepointdocumentlocation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goal_createdby"></a> lk_goal_createdby

Same as goal table [lk_goal_createdby](goal.md#BKMK_lk_goal_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_goal_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goal_createdonbehalfby"></a> lk_goal_createdonbehalfby

Same as goal table [lk_goal_createdonbehalfby](goal.md#BKMK_lk_goal_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_goal_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goal_modifiedby"></a> lk_goal_modifiedby

Same as goal table [lk_goal_modifiedby](goal.md#BKMK_lk_goal_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_goal_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goal_modifiedonbehalfby"></a> lk_goal_modifiedonbehalfby

Same as goal table [lk_goal_modifiedonbehalfby](goal.md#BKMK_lk_goal_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_goal_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_goal"></a> user_goal

Same as goal table [user_goal](goal.md#BKMK_user_goal) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_goal|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_goal_goalowner"></a> user_goal_goalowner

Same as goal table [user_goal_goalowner](goal.md#BKMK_user_goal_goalowner) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|goalownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_goal_goalowner|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_metric_createdby"></a> lk_metric_createdby

Same as metric table [lk_metric_createdby](metric.md#BKMK_lk_metric_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|metric|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_metric_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_metric_createdonbehalfby"></a> lk_metric_createdonbehalfby

Same as metric table [lk_metric_createdonbehalfby](metric.md#BKMK_lk_metric_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|metric|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_metric_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_metric_modifiedby"></a> lk_metric_modifiedby

Same as metric table [lk_metric_modifiedby](metric.md#BKMK_lk_metric_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|metric|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_metric_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_metric_modifiedonbehalfby"></a> lk_metric_modifiedonbehalfby

Same as metric table [lk_metric_modifiedonbehalfby](metric.md#BKMK_lk_metric_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|metric|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_metric_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_rollupfield_createdby"></a> lk_rollupfield_createdby

Same as rollupfield table [lk_rollupfield_createdby](rollupfield.md#BKMK_lk_rollupfield_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|rollupfield|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_rollupfield_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_rollupfield_createdonbehalfby"></a> lk_rollupfield_createdonbehalfby

Same as rollupfield table [lk_rollupfield_createdonbehalfby](rollupfield.md#BKMK_lk_rollupfield_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|rollupfield|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_rollupfield_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_rollupfield_modifiedby"></a> lk_rollupfield_modifiedby

Same as rollupfield table [lk_rollupfield_modifiedby](rollupfield.md#BKMK_lk_rollupfield_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|rollupfield|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_rollupfield_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_rollupfield_modifiedonbehalfby"></a> lk_rollupfield_modifiedonbehalfby

Same as rollupfield table [lk_rollupfield_modifiedonbehalfby](rollupfield.md#BKMK_lk_rollupfield_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|rollupfield|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_rollupfield_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goalrollupquery_createdby"></a> lk_goalrollupquery_createdby

Same as goalrollupquery table [lk_goalrollupquery_createdby](goalrollupquery.md#BKMK_lk_goalrollupquery_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_goalrollupquery_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goalrollupquery_createdonbehalfby"></a> lk_goalrollupquery_createdonbehalfby

Same as goalrollupquery table [lk_goalrollupquery_createdonbehalfby](goalrollupquery.md#BKMK_lk_goalrollupquery_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_goalrollupquery_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goalrollupquery_modifiedby"></a> lk_goalrollupquery_modifiedby

Same as goalrollupquery table [lk_goalrollupquery_modifiedby](goalrollupquery.md#BKMK_lk_goalrollupquery_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_goalrollupquery_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_goalrollupquery_modifiedonbehalfby"></a> lk_goalrollupquery_modifiedonbehalfby

Same as goalrollupquery table [lk_goalrollupquery_modifiedonbehalfby](goalrollupquery.md#BKMK_lk_goalrollupquery_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_goalrollupquery_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_emailserverprofile_createdonbehalfby"></a> lk_emailserverprofile_createdonbehalfby

Same as emailserverprofile table [lk_emailserverprofile_createdonbehalfby](emailserverprofile.md#BKMK_lk_emailserverprofile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_emailserverprofile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_emailserverprofile_modifiedonbehalfby"></a> lk_emailserverprofile_modifiedonbehalfby

Same as emailserverprofile table [lk_emailserverprofile_modifiedonbehalfby](emailserverprofile.md#BKMK_lk_emailserverprofile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_emailserverprofile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailbox_createdby"></a> lk_mailbox_createdby

Same as mailbox table [lk_mailbox_createdby](mailbox.md#BKMK_lk_mailbox_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailbox_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailbox_createdonbehalfby"></a> lk_mailbox_createdonbehalfby

Same as mailbox table [lk_mailbox_createdonbehalfby](mailbox.md#BKMK_lk_mailbox_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailbox_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailbox_modifiedby"></a> lk_mailbox_modifiedby

Same as mailbox table [lk_mailbox_modifiedby](mailbox.md#BKMK_lk_mailbox_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailbox_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailbox_modifiedonbehalfby"></a> lk_mailbox_modifiedonbehalfby

Same as mailbox table [lk_mailbox_modifiedonbehalfby](mailbox.md#BKMK_lk_mailbox_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailbox_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_mailbox"></a> user_mailbox

Same as mailbox table [user_mailbox](mailbox.md#BKMK_user_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mailbox_regarding_systemuser"></a> mailbox_regarding_systemuser

Same as mailbox table [mailbox_regarding_systemuser](mailbox.md#BKMK_mailbox_regarding_systemuser) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mailbox_regarding_systemuser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: NoCascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_post_modifiedonbehalfby"></a> lk_post_modifiedonbehalfby

Same as post table [lk_post_modifiedonbehalfby](post.md#BKMK_lk_post_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|post|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_post_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_position_createdby"></a> lk_position_createdby

Same as position table [lk_position_createdby](position.md#BKMK_lk_position_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|position|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_position_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_position_createdonbehalfby"></a> lk_position_createdonbehalfby

Same as position table [lk_position_createdonbehalfby](position.md#BKMK_lk_position_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|position|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_position_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_position_modifiedby"></a> lk_position_modifiedby

Same as position table [lk_position_modifiedby](position.md#BKMK_lk_position_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|position|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_position_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_position_modifiedonbehalfby"></a> lk_position_modifiedonbehalfby

Same as position table [lk_position_modifiedonbehalfby](position.md#BKMK_lk_position_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|position|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_position_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solution_createdby"></a> lk_solution_createdby

Same as solution table [lk_solution_createdby](solution.md#BKMK_lk_solution_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solution|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solution_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solution_modifiedby"></a> lk_solution_modifiedby

Same as solution table [lk_solution_modifiedby](solution.md#BKMK_lk_solution_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solution|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solution_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisher_createdby"></a> lk_publisher_createdby

Same as publisher table [lk_publisher_createdby](publisher.md#BKMK_lk_publisher_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisher|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisher_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisher_modifiedby"></a> lk_publisher_modifiedby

Same as publisher table [lk_publisher_modifiedby](publisher.md#BKMK_lk_publisher_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisher|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisher_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_officegraphdocument_createdonbehalfby"></a> lk_officegraphdocument_createdonbehalfby

Same as officegraphdocument table [lk_officegraphdocument_createdonbehalfby](officegraphdocument.md#BKMK_lk_officegraphdocument_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|officegraphdocument|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_officegraphdocument_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_officegraphdocument_modifiedonbehalfby"></a> lk_officegraphdocument_modifiedonbehalfby

Same as officegraphdocument table [lk_officegraphdocument_modifiedonbehalfby](officegraphdocument.md#BKMK_lk_officegraphdocument_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|officegraphdocument|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_officegraphdocument_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recommendeddocument_createdby"></a> lk_recommendeddocument_createdby

Same as recommendeddocument table [lk_recommendeddocument_createdby](recommendeddocument.md#BKMK_lk_recommendeddocument_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recommendeddocument|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recommendeddocument_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recommendeddocument_createdonbehalfby"></a> lk_recommendeddocument_createdonbehalfby

Same as recommendeddocument table [lk_recommendeddocument_createdonbehalfby](recommendeddocument.md#BKMK_lk_recommendeddocument_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recommendeddocument|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recommendeddocument_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recommendeddocument_modifiedby"></a> lk_recommendeddocument_modifiedby

Same as recommendeddocument table [lk_recommendeddocument_modifiedby](recommendeddocument.md#BKMK_lk_recommendeddocument_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recommendeddocument|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recommendeddocument_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recommendeddocument_modifiedonbehalfby"></a> lk_recommendeddocument_modifiedonbehalfby

Same as recommendeddocument table [lk_recommendeddocument_modifiedonbehalfby](recommendeddocument.md#BKMK_lk_recommendeddocument_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recommendeddocument|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recommendeddocument_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_KnowledgeBaseRecord_createdby"></a> lk_KnowledgeBaseRecord_createdby

Same as knowledgebaserecord table [lk_KnowledgeBaseRecord_createdby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgebaserecord|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_KnowledgeBaseRecord_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_KnowledgeBaseRecord_createdonbehalfby"></a> lk_KnowledgeBaseRecord_createdonbehalfby

Same as knowledgebaserecord table [lk_KnowledgeBaseRecord_createdonbehalfby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgebaserecord|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_KnowledgeBaseRecord_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedby"></a> lk_KnowledgeBaseRecord_modifiedby

Same as knowledgebaserecord table [lk_KnowledgeBaseRecord_modifiedby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgebaserecord|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_KnowledgeBaseRecord_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby"></a> lk_KnowledgeBaseRecord_modifiedonbehalfby

Same as knowledgebaserecord table [lk_KnowledgeBaseRecord_modifiedonbehalfby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgebaserecord|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_KnowledgeBaseRecord_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_lookupmapping_modifiedby"></a> lk_lookupmapping_modifiedby

Same as lookupmapping table [lk_lookupmapping_modifiedby](lookupmapping.md#BKMK_lk_lookupmapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|lookupmapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_lookupmapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usersettings_createdonbehalfby"></a> lk_usersettings_createdonbehalfby

Same as usersettings table [lk_usersettings_createdonbehalfby](usersettings.md#BKMK_lk_usersettings_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_usersettings_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticletemplatebase_modifiedby"></a> lk_kbarticletemplatebase_modifiedby

Same as kbarticletemplate table [lk_kbarticletemplatebase_modifiedby](kbarticletemplate.md#BKMK_lk_kbarticletemplatebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticletemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticletemplatebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fax_modifiedby"></a> lk_fax_modifiedby

Same as fax table [lk_fax_modifiedby](fax.md#BKMK_lk_fax_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_fax_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_completedby"></a> lk_processsession_completedby

Same as processsession table [lk_processsession_completedby](processsession.md#BKMK_lk_processsession_completedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|completedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_completedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_sdkmessageprocessingstepsecureconfig"></a> modifiedby_sdkmessageprocessingstepsecureconfig

Same as sdkmessageprocessingstepsecureconfig table [modifiedby_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepsecureconfig|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_sdkmessageprocessingstepsecureconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunit_createdonbehalfby"></a> lk_businessunit_createdonbehalfby

Same as businessunit table [lk_businessunit_createdonbehalfby](businessunit.md#BKMK_lk_businessunit_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_businessunit_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicaterule_createdonbehalfby"></a> lk_duplicaterule_createdonbehalfby

Same as duplicaterule table [lk_duplicaterule_createdonbehalfby](duplicaterule.md#BKMK_lk_duplicaterule_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicaterule_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessage_modifiedonbehalfby"></a> lk_sdkmessage_modifiedonbehalfby

Same as sdkmessage table [lk_sdkmessage_modifiedonbehalfby](sdkmessage.md#BKMK_lk_sdkmessage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_modifiedonbehalfby"></a> lk_translationprocess_modifiedonbehalfby

Same as translationprocess table [lk_translationprocess_modifiedonbehalfby](translationprocess.md#BKMK_lk_translationprocess_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_translationprocess_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_actioncardbase_createdonbehalfby"></a> lk_actioncardbase_createdonbehalfby

Same as actioncard table [lk_actioncardbase_createdonbehalfby](actioncard.md#BKMK_lk_actioncardbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_actioncardbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessagefilter_createdonbehalfby"></a> lk_sdkmessagefilter_createdonbehalfby

Same as sdkmessagefilter table [lk_sdkmessagefilter_createdonbehalfby](sdkmessagefilter.md#BKMK_lk_sdkmessagefilter_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessagefilter|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessagefilter_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slabase_modifiedonbehalfby"></a> lk_slabase_modifiedonbehalfby

Same as sla table [lk_slabase_modifiedonbehalfby](sla.md#BKMK_lk_slabase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slabase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_feedback_modifiedby"></a> lk_feedback_modifiedby

Same as feedback table [lk_feedback_modifiedby](feedback.md#BKMK_lk_feedback_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_feedback_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_templatebase_modifiedby"></a> lk_templatebase_modifiedby

Same as template table [lk_templatebase_modifiedby](template.md#BKMK_lk_templatebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_templatebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticletemplate_modifiedonbehalfby"></a> lk_kbarticletemplate_modifiedonbehalfby

Same as kbarticletemplate table [lk_kbarticletemplate_modifiedonbehalfby](kbarticletemplate.md#BKMK_lk_kbarticletemplate_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticletemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticletemplate_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slakpiinstancebase_createdby"></a> lk_slakpiinstancebase_createdby

Same as slakpiinstance table [lk_slakpiinstancebase_createdby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slakpiinstancebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ACIViewMapper_createdby"></a> lk_ACIViewMapper_createdby

Same as aciviewmapper table [lk_ACIViewMapper_createdby](aciviewmapper.md#BKMK_lk_ACIViewMapper_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|aciviewmapper|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ACIViewMapper_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userqueryvisualization_modifiedby"></a> lk_userqueryvisualization_modifiedby

Same as userqueryvisualization table [lk_userqueryvisualization_modifiedby](userqueryvisualization.md#BKMK_lk_userqueryvisualization_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userqueryvisualization_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurringappointmentmaster_createdonbehalfby"></a> lk_recurringappointmentmaster_createdonbehalfby

Same as recurringappointmentmaster table [lk_recurringappointmentmaster_createdonbehalfby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recurringappointmentmaster_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_lookupmapping_createdonbehalfby"></a> lk_lookupmapping_createdonbehalfby

Same as lookupmapping table [lk_lookupmapping_createdonbehalfby](lookupmapping.md#BKMK_lk_lookupmapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|lookupmapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_lookupmapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_MobileOfflineProfileItem_createdby"></a> lk_MobileOfflineProfileItem_createdby

Same as mobileofflineprofileitem table [lk_MobileOfflineProfileItem_createdby](mobileofflineprofileitem.md#BKMK_lk_MobileOfflineProfileItem_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitem|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_MobileOfflineProfileItem_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurringappointmentmaster_modifiedby"></a> lk_recurringappointmentmaster_modifiedby

Same as recurringappointmentmaster table [lk_recurringappointmentmaster_modifiedby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recurringappointmentmaster_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fax_createdby"></a> lk_fax_createdby

Same as fax table [lk_fax_createdby](fax.md#BKMK_lk_fax_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_fax_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_letter_modifiedonbehalfby"></a> lk_letter_modifiedonbehalfby

Same as letter table [lk_letter_modifiedonbehalfby](letter.md#BKMK_lk_letter_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_letter_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationmapping_createdby"></a> lk_transformationmapping_createdby

Same as transformationmapping table [lk_transformationmapping_createdby](transformationmapping.md#BKMK_lk_transformationmapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationmapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationmapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_reportcategorybase_createdby"></a> lk_reportcategorybase_createdby

Same as reportcategory table [lk_reportcategorybase_createdby](reportcategory.md#BKMK_lk_reportcategorybase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|reportcategory|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_reportcategorybase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_letter_createdby"></a> lk_letter_createdby

Same as letter table [lk_letter_createdby](letter.md#BKMK_lk_letter_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_letter_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrolresource_modifiedby"></a> lk_customcontrolresource_modifiedby

Same as customcontrolresource table [lk_customcontrolresource_modifiedby](customcontrolresource.md#BKMK_lk_customcontrolresource_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrolresource|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrolresource_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_expiredprocess_createdonbehalfby"></a> lk_expiredprocess_createdonbehalfby

Same as expiredprocess table [lk_expiredprocess_createdonbehalfby](expiredprocess.md#BKMK_lk_expiredprocess_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_expiredprocess_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodulecomponent_modifiedby"></a> lk_appmodulecomponent_modifiedby

Same as appmodulecomponent table [lk_appmodulecomponent_modifiedby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodulecomponent|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appmodulecomponent_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_calendar_modifiedby"></a> lk_calendar_modifiedby

Same as calendar table [lk_calendar_modifiedby](calendar.md#BKMK_lk_calendar_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|calendar|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_calendar_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_DuplicateRules"></a> SystemUser_DuplicateRules

Same as duplicaterule table [SystemUser_DuplicateRules](duplicaterule.md#BKMK_SystemUser_DuplicateRules) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_DuplicateRules|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_plugintype_createdonbehalfby"></a> lk_plugintype_createdonbehalfby

Same as plugintype table [lk_plugintype_createdonbehalfby](plugintype.md#BKMK_lk_plugintype_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintype|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_plugintype_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mobileofflineprofileitem_createdonbehalfby"></a> lk_mobileofflineprofileitem_createdonbehalfby

Same as mobileofflineprofileitem table [lk_mobileofflineprofileitem_createdonbehalfby](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitem|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mobileofflineprofileitem_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fax_createdonbehalfby"></a> lk_fax_createdonbehalfby

Same as fax table [lk_fax_createdonbehalfby](fax.md#BKMK_lk_fax_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_fax_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonedefinition_modifiedby"></a> lk_timezonedefinition_modifiedby

Same as timezonedefinition table [lk_timezonedefinition_modifiedby](timezonedefinition.md#BKMK_lk_timezonedefinition_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonedefinition|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonedefinition_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_columnmapping_createdby"></a> lk_columnmapping_createdby

Same as columnmapping table [lk_columnmapping_createdby](columnmapping.md#BKMK_lk_columnmapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|columnmapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_columnmapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_reportcategorybase_modifiedby"></a> lk_reportcategorybase_modifiedby

Same as reportcategory table [lk_reportcategorybase_modifiedby](reportcategory.md#BKMK_lk_reportcategorybase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|reportcategory|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_reportcategorybase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointsitebase_createdonbehalfby"></a> lk_sharepointsitebase_createdonbehalfby

Same as sharepointsite table [lk_sharepointsitebase_createdonbehalfby](sharepointsite.md#BKMK_lk_sharepointsitebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointsitebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowlog_modifiedby"></a> lk_workflowlog_modifiedby

Same as workflowlog table [lk_workflowlog_modifiedby](workflowlog.md#BKMK_lk_workflowlog_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_syncerrorbase_createdonbehalfby"></a> lk_syncerrorbase_createdonbehalfby

Same as syncerror table [lk_syncerrorbase_createdonbehalfby](syncerror.md#BKMK_lk_syncerrorbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_syncerrorbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bulkdeleteoperation_modifiedonbehalfby"></a> lk_bulkdeleteoperation_modifiedonbehalfby

Same as bulkdeleteoperation table [lk_bulkdeleteoperation_modifiedonbehalfby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeleteoperation|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_bulkdeleteoperation_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceendpointbase_createdonbehalfby"></a> lk_serviceendpointbase_createdonbehalfby

Same as serviceendpoint table [lk_serviceendpointbase_createdonbehalfby](serviceendpoint.md#BKMK_lk_serviceendpointbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceendpoint|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_serviceendpointbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentbase_createdonbehalfby"></a> lk_solutioncomponentbase_createdonbehalfby

Same as solutioncomponent table [lk_solutioncomponentbase_createdonbehalfby](solutioncomponent.md#BKMK_lk_solutioncomponentbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponent|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_plugintype_modifiedonbehalfby"></a> lk_plugintype_modifiedonbehalfby

Same as plugintype table [lk_plugintype_modifiedonbehalfby](plugintype.md#BKMK_lk_plugintype_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintype|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_plugintype_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_lookupmapping_modifiedonbehalfby"></a> lk_lookupmapping_modifiedonbehalfby

Same as lookupmapping table [lk_lookupmapping_modifiedonbehalfby](lookupmapping.md#BKMK_lk_lookupmapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|lookupmapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_lookupmapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_phonecall_modifiedby"></a> lk_phonecall_modifiedby

Same as phonecall table [lk_phonecall_modifiedby](phonecall.md#BKMK_lk_phonecall_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_phonecall_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slabase_modifiedby"></a> lk_slabase_modifiedby

Same as sla table [lk_slabase_modifiedby](sla.md#BKMK_lk_slabase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slabase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowlog_modifiedonbehalfby"></a> lk_workflowlog_modifiedonbehalfby

Same as workflowlog table [lk_workflowlog_modifiedonbehalfby](workflowlog.md#BKMK_lk_workflowlog_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importfilebase_createdonbehalfby"></a> lk_importfilebase_createdonbehalfby

Same as importfile table [lk_importfilebase_createdonbehalfby](importfile.md#BKMK_lk_importfilebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importfilebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fieldsecurityprofile_createdonbehalfby"></a> lk_fieldsecurityprofile_createdonbehalfby

Same as fieldsecurityprofile table [lk_fieldsecurityprofile_createdonbehalfby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fieldsecurityprofile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fieldsecurityprofile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importmapbase_createdby"></a> lk_importmapbase_createdby

Same as importmap table [lk_importmapbase_createdby](importmap.md#BKMK_lk_importmapbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importmapbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_PostFollow_createdby"></a> lk_PostFollow_createdby

Same as postfollow table [lk_PostFollow_createdby](postfollow.md#BKMK_lk_PostFollow_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_PostFollow_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuser_PostFollows"></a> systemuser_PostFollows

Same as postfollow table [systemuser_PostFollows](postfollow.md#BKMK_systemuser_PostFollows) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|systemuser_PostFollows|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_post_createdby"></a> lk_post_createdby

Same as post table [lk_post_createdby](post.md#BKMK_lk_post_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|post|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_post_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_post_createdonbehalfby"></a> lk_post_createdonbehalfby

Same as post table [lk_post_createdonbehalfby](post.md#BKMK_lk_post_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|post|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_post_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_post_modifiedby"></a> lk_post_modifiedby

Same as post table [lk_post_modifiedby](post.md#BKMK_lk_post_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|post|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_post_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_postcomment_createdby"></a> lk_postcomment_createdby

Same as postcomment table [lk_postcomment_createdby](postcomment.md#BKMK_lk_postcomment_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postcomment|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_postcomment_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_owner_postfollows"></a> user_owner_postfollows

Same as postfollow table [user_owner_postfollows](postfollow.md#BKMK_user_owner_postfollows) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_owner_postfollows|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_postfollow_createdonbehalfby"></a> lk_postfollow_createdonbehalfby

Same as postfollow table [lk_postfollow_createdonbehalfby](postfollow.md#BKMK_lk_postfollow_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_postfollow_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_postcomment_createdonbehalfby"></a> lk_postcomment_createdonbehalfby

Same as postcomment table [lk_postcomment_createdonbehalfby](postcomment.md#BKMK_lk_postcomment_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postcomment|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_postcomment_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_postlike_createdonbehalfby"></a> lk_postlike_createdonbehalfby

Same as postlike table [lk_postlike_createdonbehalfby](postlike.md#BKMK_lk_postlike_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postlike|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_postlike_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_postlike_createdby"></a> lk_postlike_createdby

Same as postlike table [lk_postlike_createdby](postlike.md#BKMK_lk_postlike_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postlike|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_postlike_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queueitem_modifiedonbehalfby"></a> lk_queueitem_modifiedonbehalfby

Same as queueitem table [lk_queueitem_modifiedonbehalfby](queueitem.md#BKMK_lk_queueitem_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queueitem_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_socialactivity"></a> user_socialactivity

Same as socialactivity table [user_socialactivity](socialactivity.md#BKMK_user_socialactivity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_socialactivity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_createdonbehalfby"></a> lk_translationprocess_createdonbehalfby

Same as translationprocess table [lk_translationprocess_createdonbehalfby](translationprocess.md#BKMK_lk_translationprocess_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_translationprocess_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby

Same as sdkmessageprocessingstepsecureconfig table [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](sdkmessageprocessingstepsecureconfig.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepsecureconfig|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_feedback_modifiedonbehalfby"></a> lk_feedback_modifiedonbehalfby

Same as feedback table [lk_feedback_modifiedonbehalfby](feedback.md#BKMK_lk_feedback_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_feedback_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowlog_createdonbehalfby"></a> lk_workflowlog_createdonbehalfby

Same as workflowlog table [lk_workflowlog_createdonbehalfby](workflowlog.md#BKMK_lk_workflowlog_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_role_createdonbehalfby"></a> lk_role_createdonbehalfby

Same as role table [lk_role_createdonbehalfby](role.md#BKMK_lk_role_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_role_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transactioncurrency_modifiedonbehalfby"></a> lk_transactioncurrency_modifiedonbehalfby

Same as transactioncurrency table [lk_transactioncurrency_modifiedonbehalfby](transactioncurrency.md#BKMK_lk_transactioncurrency_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transactioncurrency|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transactioncurrency_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_rolebase_modifiedby"></a> lk_rolebase_modifiedby

Same as role table [lk_rolebase_modifiedby](role.md#BKMK_lk_rolebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_rolebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_navigationsetting_createdby"></a> lk_navigationsetting_createdby

Same as navigationsetting table [lk_navigationsetting_createdby](navigationsetting.md#BKMK_lk_navigationsetting_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|navigationsetting|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_navigationsetting_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_subject_modifiedonbehalfby"></a> lk_subject_modifiedonbehalfby

Same as subject table [lk_subject_modifiedonbehalfby](subject.md#BKMK_lk_subject_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|subject|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_subject_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicaterule_modifiedonbehalfby"></a> lk_duplicaterule_modifiedonbehalfby

Same as duplicaterule table [lk_duplicaterule_modifiedonbehalfby](duplicaterule.md#BKMK_lk_duplicaterule_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicaterule_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_task_modifiedonbehalfby"></a> lk_task_modifiedonbehalfby

Same as task table [lk_task_modifiedonbehalfby](task.md#BKMK_lk_task_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_task_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_subjectbase_modifiedby"></a> lk_subjectbase_modifiedby

Same as subject table [lk_subjectbase_modifiedby](subject.md#BKMK_lk_subjectbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|subject|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_subjectbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailboxtrackingfolder_modifiedby"></a> lk_mailboxtrackingfolder_modifiedby

Same as mailboxtrackingfolder table [lk_mailboxtrackingfolder_modifiedby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailboxtrackingfolder_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_impersonatinguserid_sdkmessageprocessingstep"></a> impersonatinguserid_sdkmessageprocessingstep

Same as sdkmessageprocessingstep table [impersonatinguserid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_impersonatinguserid_sdkmessageprocessingstep) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|impersonatinguserid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|impersonatinguserid_sdkmessageprocessingstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticle_createdonbehalfby"></a> lk_kbarticle_createdonbehalfby

Same as kbarticle table [lk_kbarticle_createdonbehalfby](kbarticle.md#BKMK_lk_kbarticle_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticle|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_kbarticle_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_calendar_createdonbehalfby"></a> lk_calendar_createdonbehalfby

Same as calendar table [lk_calendar_createdonbehalfby](calendar.md#BKMK_lk_calendar_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|calendar|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_calendar_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunitnewsarticlebase_modifiedby"></a> lk_businessunitnewsarticlebase_modifiedby

Same as businessunitnewsarticle table [lk_businessunitnewsarticlebase_modifiedby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticlebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunitnewsarticle|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_businessunitnewsarticlebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_userqueryvisualizations"></a> user_userqueryvisualizations

Same as userqueryvisualization table [user_userqueryvisualizations](userqueryvisualization.md#BKMK_user_userqueryvisualizations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_userqueryvisualizations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_tracelog_createdonbehalfby"></a> lk_tracelog_createdonbehalfby

Same as tracelog table [lk_tracelog_createdonbehalfby](tracelog.md#BKMK_lk_tracelog_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|tracelog|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_tracelog_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queueitembase_workerid"></a> lk_queueitembase_workerid

Same as queueitem table [lk_queueitembase_workerid](queueitem.md#BKMK_lk_queueitembase_workerid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|workerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queueitembase_workerid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mobileofflineprofileitem_modifiedby"></a> lk_mobileofflineprofileitem_modifiedby

Same as mobileofflineprofileitem table [lk_mobileofflineprofileitem_modifiedby](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitem|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mobileofflineprofileitem_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customeraddressbase_modifiedby"></a> lk_customeraddressbase_modifiedby

Same as customeraddress table [lk_customeraddressbase_modifiedby](customeraddress.md#BKMK_lk_customeraddressbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customeraddress|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customeraddressbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activitypointer_modifiedby"></a> lk_activitypointer_modifiedby

Same as activitypointer table [lk_activitypointer_modifiedby](activitypointer.md#BKMK_lk_activitypointer_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_activitypointer_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customeraddressbase_createdby"></a> lk_customeraddressbase_createdby

Same as customeraddress table [lk_customeraddressbase_createdby](customeraddress.md#BKMK_lk_customeraddressbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customeraddress|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customeraddressbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_syncerrorbase_modifiedonbehalfby"></a> lk_syncerrorbase_modifiedonbehalfby

Same as syncerror table [lk_syncerrorbase_modifiedonbehalfby](syncerror.md#BKMK_lk_syncerrorbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_syncerrorbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_BulkDeleteFailures"></a> SystemUser_BulkDeleteFailures

Same as bulkdeletefailure table [SystemUser_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SystemUser_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teambase_modifiedby"></a> lk_teambase_modifiedby

Same as team table [lk_teambase_modifiedby](team.md#BKMK_lk_teambase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_teambase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_workflow_createdby"></a> workflow_createdby

Same as workflow table [workflow_createdby](workflow.md#BKMK_workflow_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queue_modifiedonbehalfby"></a> lk_queue_modifiedonbehalfby

Same as queue table [lk_queue_modifiedonbehalfby](queue.md#BKMK_lk_queue_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queue_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customeraddress_modifiedonbehalfby"></a> lk_customeraddress_modifiedonbehalfby

Same as customeraddress table [lk_customeraddress_modifiedonbehalfby](customeraddress.md#BKMK_lk_customeraddress_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customeraddress|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customeraddress_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_rolebase_createdby"></a> lk_rolebase_createdby

Same as role table [lk_rolebase_createdby](role.md#BKMK_lk_rolebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_rolebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_reportcategory_modifiedonbehalfby"></a> lk_reportcategory_modifiedonbehalfby

Same as reportcategory table [lk_reportcategory_modifiedonbehalfby](reportcategory.md#BKMK_lk_reportcategory_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|reportcategory|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_reportcategory_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationmapping_modifiedby"></a> lk_transformationmapping_modifiedby

Same as transformationmapping table [lk_transformationmapping_modifiedby](transformationmapping.md#BKMK_lk_transformationmapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationmapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationmapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicaterulecondition_modifiedonbehalfby"></a> lk_duplicaterulecondition_modifiedonbehalfby

Same as duplicaterulecondition table [lk_duplicaterulecondition_modifiedonbehalfby](duplicaterulecondition.md#BKMK_lk_duplicaterulecondition_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterulecondition|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicaterulecondition_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_picklistmapping_createdby"></a> lk_picklistmapping_createdby

Same as picklistmapping table [lk_picklistmapping_createdby](picklistmapping.md#BKMK_lk_picklistmapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|picklistmapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_picklistmapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedqueryvisualizationbase_modifiedby"></a> lk_savedqueryvisualizationbase_modifiedby

Same as savedqueryvisualization table [lk_savedqueryvisualizationbase_modifiedby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedqueryvisualization|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedqueryvisualizationbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticlecommentbase_modifiedby"></a> lk_kbarticlecommentbase_modifiedby

Same as kbarticlecomment table [lk_kbarticlecommentbase_modifiedby](kbarticlecomment.md#BKMK_lk_kbarticlecommentbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticlecomment|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticlecommentbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_email_modifiedonbehalfby"></a> lk_email_modifiedonbehalfby

Same as email table [lk_email_modifiedonbehalfby](email.md#BKMK_lk_email_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_email_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_asyncoperation_createdonbehalfby"></a> lk_asyncoperation_createdonbehalfby

Same as asyncoperation table [lk_asyncoperation_createdonbehalfby](asyncoperation.md#BKMK_lk_asyncoperation_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_asyncoperation_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_pluginassembly_modifiedonbehalfby"></a> lk_pluginassembly_modifiedonbehalfby

Same as pluginassembly table [lk_pluginassembly_modifiedonbehalfby](pluginassembly.md#BKMK_lk_pluginassembly_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginassembly|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_pluginassembly_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_team_createdonbehalfby"></a> lk_team_createdonbehalfby

Same as team table [lk_team_createdonbehalfby](team.md#BKMK_lk_team_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_team_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_connection"></a> createdby_connection

Same as connection table [createdby_connection](connection.md#BKMK_createdby_connection) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|createdby_connection|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_workflow_modifiedby"></a> workflow_modifiedby

Same as workflow table [workflow_modifiedby](workflow.md#BKMK_workflow_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunitnewsarticle_createdonbehalfby"></a> lk_businessunitnewsarticle_createdonbehalfby

Same as businessunitnewsarticle table [lk_businessunitnewsarticle_createdonbehalfby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticle_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunitnewsarticle|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_businessunitnewsarticle_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepimage_modifiedonbehalfby

Same as sdkmessageprocessingstepimage table [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](sdkmessageprocessingstepimage.md#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepimage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessageprocessingstepimage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsessionbase_createdonbehalfby"></a> lk_processsessionbase_createdonbehalfby

Same as processsession table [lk_processsessionbase_createdonbehalfby](processsession.md#BKMK_lk_processsessionbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsessionbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodule_modifiedonbehalfby"></a> lk_appmodule_modifiedonbehalfby

Same as appmodule table [lk_appmodule_modifiedonbehalfby](appmodule.md#BKMK_lk_appmodule_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodule|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appmodule_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontroldefaultconfig_modifiedonbehalfby"></a> lk_customcontroldefaultconfig_modifiedonbehalfby

Same as customcontroldefaultconfig table [lk_customcontroldefaultconfig_modifiedonbehalfby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontroldefaultconfig|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontroldefaultconfig_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_tracelog_modifiedby"></a> lk_tracelog_modifiedby

Same as tracelog table [lk_tracelog_modifiedby](tracelog.md#BKMK_lk_tracelog_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|tracelog|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_tracelog_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_appointment"></a> user_appointment

Same as appointment table [user_appointment](appointment.md#BKMK_user_appointment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_appointment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfig_createdonbehalfby"></a> lk_appconfig_createdonbehalfby

Same as appconfig table [lk_appconfig_createdonbehalfby](appconfig.md#BKMK_lk_appconfig_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfig|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfig_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfiginstance_createdonbehalfby"></a> lk_appconfiginstance_createdonbehalfby

Same as appconfiginstance table [lk_appconfiginstance_createdonbehalfby](appconfiginstance.md#BKMK_lk_appconfiginstance_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfiginstance|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfiginstance_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_DisplayStringbase_modifiedby"></a> lk_DisplayStringbase_modifiedby

Same as displaystring table [lk_DisplayStringbase_modifiedby](displaystring.md#BKMK_lk_DisplayStringbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|displaystring|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_DisplayStringbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importlog_modifiedonbehalfby"></a> lk_importlog_modifiedonbehalfby

Same as importlog table [lk_importlog_modifiedonbehalfby](importlog.md#BKMK_lk_importlog_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importlog_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_navigationsetting_modifiedby"></a> lk_navigationsetting_modifiedby

Same as navigationsetting table [lk_navigationsetting_modifiedby](navigationsetting.md#BKMK_lk_navigationsetting_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|navigationsetting|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_navigationsetting_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_Email_EmailSender"></a> SystemUser_Email_EmailSender

Same as email table [SystemUser_Email_EmailSender](email.md#BKMK_SystemUser_Email_EmailSender) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|emailsender|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_Email_EmailSender|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_activity"></a> user_activity

Same as activitypointer table [user_activity](activitypointer.md#BKMK_user_activity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_activity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_monthlyfiscalcalendar_salespersonid"></a> lk_monthlyfiscalcalendar_salespersonid

Same as monthlyfiscalcalendar table [lk_monthlyfiscalcalendar_salespersonid](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_salespersonid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|monthlyfiscalcalendar|
|ReferencingAttribute|salespersonid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_monthlyfiscalcalendar_salespersonid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunit_modifiedonbehalfby"></a> lk_businessunit_modifiedonbehalfby

Same as businessunit table [lk_businessunit_modifiedonbehalfby](businessunit.md#BKMK_lk_businessunit_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_businessunit_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_asyncoperation_modifiedonbehalfby"></a> lk_asyncoperation_modifiedonbehalfby

Same as asyncoperation table [lk_asyncoperation_modifiedonbehalfby](asyncoperation.md#BKMK_lk_asyncoperation_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_asyncoperation_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teambase_createdby"></a> lk_teambase_createdby

Same as team table [lk_teambase_createdby](team.md#BKMK_lk_teambase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_teambase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_emailserverprofile_modifiedby"></a> lk_emailserverprofile_modifiedby

Same as emailserverprofile table [lk_emailserverprofile_modifiedby](emailserverprofile.md#BKMK_lk_emailserverprofile_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_emailserverprofile_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processtriggerbase_modifiedonbehalfby"></a> lk_processtriggerbase_modifiedonbehalfby

Same as processtrigger table [lk_processtriggerbase_modifiedonbehalfby](processtrigger.md#BKMK_lk_processtriggerbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processtrigger|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processtriggerbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailmergetemplate_modifiedonbehalfby"></a> lk_mailmergetemplate_modifiedonbehalfby

Same as mailmergetemplate table [lk_mailmergetemplate_modifiedonbehalfby](mailmergetemplate.md#BKMK_lk_mailmergetemplate_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailmergetemplate_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionbase_modifiedonbehalfby"></a> lk_connectionbase_modifiedonbehalfby

Same as connection table [lk_connectionbase_modifiedonbehalfby](connection.md#BKMK_lk_connectionbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connectionbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queueitem_createdonbehalfby"></a> lk_queueitem_createdonbehalfby

Same as queueitem table [lk_queueitem_createdonbehalfby](queueitem.md#BKMK_lk_queueitem_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queueitem_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teamtemplate_modifiedonbehalfby"></a> lk_teamtemplate_modifiedonbehalfby

Same as teamtemplate table [lk_teamtemplate_modifiedonbehalfby](teamtemplate.md#BKMK_lk_teamtemplate_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|teamtemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_teamtemplate_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_documenttemplatebase_modifiedby"></a> lk_documenttemplatebase_modifiedby

Same as documenttemplate table [lk_documenttemplatebase_modifiedby](documenttemplate.md#BKMK_lk_documenttemplatebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|documenttemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_documenttemplatebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationparametermapping_createdonbehalfby"></a> lk_transformationparametermapping_createdonbehalfby

Same as transformationparametermapping table [lk_transformationparametermapping_createdonbehalfby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationparametermapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationparametermapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_userquery"></a> user_userquery

Same as userquery table [user_userquery](userquery.md#BKMK_user_userquery) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_userquery|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodule_createdby"></a> lk_appmodule_createdby

Same as appmodule table [lk_appmodule_createdby](appmodule.md#BKMK_lk_appmodule_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodule|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appmodule_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticlecommentbase_createdby"></a> lk_kbarticlecommentbase_createdby

Same as kbarticlecomment table [lk_kbarticlecommentbase_createdby](kbarticlecomment.md#BKMK_lk_kbarticlecommentbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticlecomment|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticlecommentbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_workflow_createdonbehalfby"></a> workflow_createdonbehalfby

Same as workflow table [workflow_createdonbehalfby](workflow.md#BKMK_workflow_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurrencerule_modifiedby"></a> lk_recurrencerule_modifiedby

Same as recurrencerule table [lk_recurrencerule_modifiedby](recurrencerule.md#BKMK_lk_recurrencerule_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurrencerule|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_recurrencerule_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_category_modifiedonbehalfby"></a> lk_category_modifiedonbehalfby

Same as category table [lk_category_modifiedonbehalfby](category.md#BKMK_lk_category_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_category_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfig_modifiedby"></a> lk_appconfig_modifiedby

Same as appconfig table [lk_appconfig_modifiedby](appconfig.md#BKMK_lk_appconfig_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfig|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfig_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bulkdeleteoperationbase_createdby"></a> lk_bulkdeleteoperationbase_createdby

Same as bulkdeleteoperation table [lk_bulkdeleteoperationbase_createdby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperationbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeleteoperation|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_bulkdeleteoperationbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_asyncoperation_createdby"></a> lk_asyncoperation_createdby

Same as asyncoperation table [lk_asyncoperation_createdby](asyncoperation.md#BKMK_lk_asyncoperation_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_asyncoperation_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessagefilter_modifiedonbehalfby"></a> lk_sdkmessagefilter_modifiedonbehalfby

Same as sdkmessagefilter table [lk_sdkmessagefilter_modifiedonbehalfby](sdkmessagefilter.md#BKMK_lk_sdkmessagefilter_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessagefilter|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessagefilter_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_recurringappointmentmaster"></a> user_recurringappointmentmaster

Same as recurringappointmentmaster table [user_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_user_recurringappointmentmaster) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_recurringappointmentmaster|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slaitembase_modifiedby"></a> lk_slaitembase_modifiedby

Same as slaitem table [lk_slaitembase_modifiedby](slaitem.md#BKMK_lk_slaitembase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slaitembase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisheraddressbase_modifiedonbehalfby"></a> lk_publisheraddressbase_modifiedonbehalfby

Same as publisheraddress table [lk_publisheraddressbase_modifiedonbehalfby](publisheraddress.md#BKMK_lk_publisheraddressbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisheraddress|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisheraddressbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_documenttemplatebase_createdby"></a> lk_documenttemplatebase_createdby

Same as documenttemplate table [lk_documenttemplatebase_createdby](documenttemplate.md#BKMK_lk_documenttemplatebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|documenttemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_documenttemplatebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationparametermapping_modifiedby"></a> lk_transformationparametermapping_modifiedby

Same as transformationparametermapping table [lk_transformationparametermapping_modifiedby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationparametermapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationparametermapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slabase_createdby"></a> lk_slabase_createdby

Same as sla table [lk_slabase_createdby](sla.md#BKMK_lk_slabase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slabase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationbase_createdby"></a> lk_organizationbase_createdby

Same as organization table [lk_organizationbase_createdby](organization.md#BKMK_lk_organizationbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organizationbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_report_modifiedonbehalfby"></a> lk_report_modifiedonbehalfby

Same as report table [lk_report_modifiedonbehalfby](report.md#BKMK_lk_report_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_report_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedby"></a> lk_quarterlyfiscalcalendar_modifiedby

Same as quarterlyfiscalcalendar table [lk_quarterlyfiscalcalendar_modifiedby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|quarterlyfiscalcalendar|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_quarterlyfiscalcalendar_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_serviceendpoint"></a> createdby_serviceendpoint

Same as serviceendpoint table [createdby_serviceendpoint](serviceendpoint.md#BKMK_createdby_serviceendpoint) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceendpoint|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_serviceendpoint|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicaterulecondition_createdonbehalfby"></a> lk_duplicaterulecondition_createdonbehalfby

Same as duplicaterulecondition table [lk_duplicaterulecondition_createdonbehalfby](duplicaterulecondition.md#BKMK_lk_duplicaterulecondition_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterulecondition|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicaterulecondition_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transactioncurrencybase_modifiedby"></a> lk_transactioncurrencybase_modifiedby

Same as transactioncurrency table [lk_transactioncurrencybase_modifiedby](transactioncurrency.md#BKMK_lk_transactioncurrencybase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transactioncurrency|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transactioncurrencybase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_DisplayStringbase_createdby"></a> lk_DisplayStringbase_createdby

Same as displaystring table [lk_DisplayStringbase_createdby](displaystring.md#BKMK_lk_DisplayStringbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|displaystring|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_DisplayStringbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slaitembase_modifiedonbehalfby"></a> lk_slaitembase_modifiedonbehalfby

Same as slaitem table [lk_slaitembase_modifiedonbehalfby](slaitem.md#BKMK_lk_slaitembase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slaitembase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_annotation_owning_user"></a> annotation_owning_user

Same as annotation table [annotation_owning_user](annotation.md#BKMK_annotation_owning_user) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|annotation_owning_user|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_contacts"></a> system_user_contacts

Same as contact table [system_user_contacts](contact.md#BKMK_system_user_contacts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|preferredsystemuserid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|system_user_contacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationparametermapping_createdby"></a> lk_transformationparametermapping_createdby

Same as transformationparametermapping table [lk_transformationparametermapping_createdby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationparametermapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationparametermapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_phonecall_createdonbehalfby"></a> lk_phonecall_createdonbehalfby

Same as phonecall table [lk_phonecall_createdonbehalfby](phonecall.md#BKMK_lk_phonecall_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_phonecall_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_email_modifiedby"></a> lk_email_modifiedby

Same as email table [lk_email_modifiedby](email.md#BKMK_lk_email_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_email_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usersettingsbase_createdby"></a> lk_usersettingsbase_createdby

Same as usersettings table [lk_usersettingsbase_createdby](usersettings.md#BKMK_lk_usersettingsbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_usersettingsbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teamtemplate_createdonbehalfby"></a> lk_teamtemplate_createdonbehalfby

Same as teamtemplate table [lk_teamtemplate_createdonbehalfby](teamtemplate.md#BKMK_lk_teamtemplate_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|teamtemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_teamtemplate_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodule_createdonbehalfby"></a> lk_appmodule_createdonbehalfby

Same as appmodule table [lk_appmodule_createdonbehalfby](appmodule.md#BKMK_lk_appmodule_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodule|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appmodule_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importlogbase_createdby"></a> lk_importlogbase_createdby

Same as importlog table [lk_importlogbase_createdby](importlog.md#BKMK_lk_importlogbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importlogbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointdocumentlocationbase_createdby"></a> lk_sharepointdocumentlocationbase_createdby

Same as sharepointdocumentlocation table [lk_sharepointdocumentlocationbase_createdby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointdocumentlocationbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_accounts"></a> user_accounts

Same as account table [user_accounts](account.md#BKMK_user_accounts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_accounts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_settings"></a> user_settings

Same as usersettings table [user_settings](usersettings.md#BKMK_user_settings) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|systemuserid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_settings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_plugintype"></a> modifiedby_plugintype

Same as plugintype table [modifiedby_plugintype](plugintype.md#BKMK_modifiedby_plugintype) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintype|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_plugintype|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importentitymapping_modifiedonbehalfby"></a> lk_importentitymapping_modifiedonbehalfby

Same as importentitymapping table [lk_importentitymapping_modifiedonbehalfby](importentitymapping.md#BKMK_lk_importentitymapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importentitymapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importentitymapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedquerybase_createdby"></a> lk_savedquerybase_createdby

Same as savedquery table [lk_savedquerybase_createdby](savedquery.md#BKMK_lk_savedquerybase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedquery|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedquerybase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activitypointer_createdby"></a> lk_activitypointer_createdby

Same as activitypointer table [lk_activitypointer_createdby](activitypointer.md#BKMK_lk_activitypointer_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_activitypointer_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_columnmapping_createdonbehalfby"></a> lk_columnmapping_createdonbehalfby

Same as columnmapping table [lk_columnmapping_createdonbehalfby](columnmapping.md#BKMK_lk_columnmapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|columnmapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_columnmapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby"></a> lk_mobileofflineprofileitemassociation_modifiedonbehalfby

Same as mobileofflineprofileitemassociation table [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](mobileofflineprofileitemassociation.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitemassociation|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mobileofflineprofileitemassocaition_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_subject_createdonbehalfby"></a> lk_subject_createdonbehalfby

Same as subject table [lk_subject_createdonbehalfby](subject.md#BKMK_lk_subject_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|subject|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_subject_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfigmaster_createdonbehalfby"></a> lk_appconfigmaster_createdonbehalfby

Same as appconfigmaster table [lk_appconfigmaster_createdonbehalfby](appconfigmaster.md#BKMK_lk_appconfigmaster_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfigmaster|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfigmaster_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticle_modifiedonbehalfby"></a> lk_kbarticle_modifiedonbehalfby

Same as kbarticle table [lk_kbarticle_modifiedonbehalfby](kbarticle.md#BKMK_lk_kbarticle_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticle|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_kbarticle_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_sdkmessageprocessingstepsecureconfig"></a> createdby_sdkmessageprocessingstepsecureconfig

Same as sdkmessageprocessingstepsecureconfig table [createdby_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_createdby_sdkmessageprocessingstepsecureconfig) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepsecureconfig|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_sdkmessageprocessingstepsecureconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_sdkmessageprocessingstep"></a> createdby_sdkmessageprocessingstep

Same as sdkmessageprocessingstep table [createdby_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_createdby_sdkmessageprocessingstep) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_sdkmessageprocessingstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfig_modifiedonbehalfby"></a> lk_appconfig_modifiedonbehalfby

Same as appconfig table [lk_appconfig_modifiedonbehalfby](appconfig.md#BKMK_lk_appconfig_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfig|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfig_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_quarterlyfiscalcalendar_salespersonid"></a> lk_quarterlyfiscalcalendar_salespersonid

Same as quarterlyfiscalcalendar table [lk_quarterlyfiscalcalendar_salespersonid](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_salespersonid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|quarterlyfiscalcalendar|
|ReferencingAttribute|salespersonid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_quarterlyfiscalcalendar_salespersonid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationparametermapping_modifiedonbehalfby"></a> lk_transformationparametermapping_modifiedonbehalfby

Same as transformationparametermapping table [lk_transformationparametermapping_modifiedonbehalfby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationparametermapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationparametermapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importentitymapping_createdonbehalfby"></a> lk_importentitymapping_createdonbehalfby

Same as importentitymapping table [lk_importentitymapping_createdonbehalfby](importentitymapping.md#BKMK_lk_importentitymapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importentitymapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importentitymapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_ProcessSessions"></a> SystemUser_ProcessSessions

Same as processsession table [SystemUser_ProcessSessions](processsession.md#BKMK_SystemUser_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_templatebase_createdonbehalfby"></a> lk_templatebase_createdonbehalfby

Same as template table [lk_templatebase_createdonbehalfby](template.md#BKMK_lk_templatebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_templatebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_lookupmapping_createdby"></a> lk_lookupmapping_createdby

Same as lookupmapping table [lk_lookupmapping_createdby](lookupmapping.md#BKMK_lk_lookupmapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|lookupmapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_lookupmapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby"></a> lk_mobileofflineprofileitem_modifiedonbehalfby

Same as mobileofflineprofileitem table [lk_mobileofflineprofileitem_modifiedonbehalfby](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitem|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mobileofflineprofileitem_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsessionbase_modifiedonbehalfby"></a> lk_processsessionbase_modifiedonbehalfby

Same as processsession table [lk_processsessionbase_modifiedonbehalfby](processsession.md#BKMK_lk_processsessionbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsessionbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_createdby"></a> lk_processsession_createdby

Same as processsession table [lk_processsession_createdby](processsession.md#BKMK_lk_processsession_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_personaldocumenttemplatebase_createdby"></a> lk_personaldocumenttemplatebase_createdby

Same as personaldocumenttemplate table [lk_personaldocumenttemplatebase_createdby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|personaldocumenttemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_personaldocumenttemplatebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisherbase_modifiedonbehalfby"></a> lk_publisherbase_modifiedonbehalfby

Same as publisher table [lk_publisherbase_modifiedonbehalfby](publisher.md#BKMK_lk_publisherbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisher|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisherbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_MobileOfflineProfile_createdonbehalfby"></a> lk_MobileOfflineProfile_createdonbehalfby

Same as mobileofflineprofile table [lk_MobileOfflineProfile_createdonbehalfby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_MobileOfflineProfile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonerule_createdby"></a> lk_timezonerule_createdby

Same as timezonerule table [lk_timezonerule_createdby](timezonerule.md#BKMK_lk_timezonerule_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonerule|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonerule_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_contactbase_createdby"></a> lk_contactbase_createdby

Same as contact table [lk_contactbase_createdby](contact.md#BKMK_lk_contactbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_contactbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slakpiinstancebase_createdonbehalfby"></a> lk_slakpiinstancebase_createdonbehalfby

Same as slakpiinstance table [lk_slakpiinstancebase_createdonbehalfby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slakpiinstancebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_workflow"></a> system_user_workflow

Same as workflow table [system_user_workflow](workflow.md#BKMK_system_user_workflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|system_user_workflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicaterulebase_createdby"></a> lk_duplicaterulebase_createdby

Same as duplicaterule table [lk_duplicaterulebase_createdby](duplicaterule.md#BKMK_lk_duplicaterulebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicaterulebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appointment_createdonbehalfby"></a> lk_appointment_createdonbehalfby

Same as appointment table [lk_appointment_createdonbehalfby](appointment.md#BKMK_lk_appointment_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appointment_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_connection_role"></a> createdby_connection_role

Same as connectionrole table [createdby_connection_role](connectionrole.md#BKMK_createdby_connection_role) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionrole|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_connection_role|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfigmaster_modifiedby"></a> lk_appconfigmaster_modifiedby

Same as appconfigmaster table [lk_appconfigmaster_modifiedby](appconfigmaster.md#BKMK_lk_appconfigmaster_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfigmaster|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfigmaster_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_newprocess_modifiedby"></a> lk_newprocess_modifiedby

Same as newprocess table [lk_newprocess_modifiedby](newprocess.md#BKMK_lk_newprocess_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_newprocess_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_columnmapping_modifiedonbehalfby"></a> lk_columnmapping_modifiedonbehalfby

Same as columnmapping table [lk_columnmapping_modifiedonbehalfby](columnmapping.md#BKMK_lk_columnmapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|columnmapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_columnmapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_createdby"></a> lk_translationprocess_createdby

Same as translationprocess table [lk_translationprocess_createdby](translationprocess.md#BKMK_lk_translationprocess_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_translationprocess_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedby"></a> lk_monthlyfiscalcalendar_modifiedby

Same as monthlyfiscalcalendar table [lk_monthlyfiscalcalendar_modifiedby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|monthlyfiscalcalendar|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_monthlyfiscalcalendar_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_systemuserbase_modifiedby"></a> lk_systemuserbase_modifiedby

Same as systemuser table [lk_systemuserbase_modifiedby](systemuser.md#BKMK_lk_systemuserbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_systemuserbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_expiredprocess_modifiedby"></a> lk_expiredprocess_modifiedby

Same as expiredprocess table [lk_expiredprocess_modifiedby](expiredprocess.md#BKMK_lk_expiredprocess_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_expiredprocess_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_SocialProfile_createdonbehalfby"></a> lk_SocialProfile_createdonbehalfby

Same as socialprofile table [lk_SocialProfile_createdonbehalfby](socialprofile.md#BKMK_lk_SocialProfile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_SocialProfile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importmap_createdonbehalfby"></a> lk_importmap_createdonbehalfby

Same as importmap table [lk_importmap_createdonbehalfby](importmap.md#BKMK_lk_importmap_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importmap_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_connection"></a> modifiedby_connection

Same as connection table [modifiedby_connection](connection.md#BKMK_modifiedby_connection) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|modifiedby_connection|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_import_createdonbehalfby"></a> lk_import_createdonbehalfby

Same as import table [lk_import_createdonbehalfby](import.md#BKMK_lk_import_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_import_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slaitembase_createdonbehalfby"></a> lk_slaitembase_createdonbehalfby

Same as slaitem table [lk_slaitembase_createdonbehalfby](slaitem.md#BKMK_lk_slaitembase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slaitembase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_navigationsetting_createdonbehalfby"></a> lk_navigationsetting_createdonbehalfby

Same as navigationsetting table [lk_navigationsetting_createdonbehalfby](navigationsetting.md#BKMK_lk_navigationsetting_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|navigationsetting|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_navigationsetting_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedquery_modifiedonbehalfby"></a> lk_savedquery_modifiedonbehalfby

Same as savedquery table [lk_savedquery_modifiedonbehalfby](savedquery.md#BKMK_lk_savedquery_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedquery|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedquery_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentbase_modifiedonbehalfby"></a> lk_solutioncomponentbase_modifiedonbehalfby

Same as solutioncomponent table [lk_solutioncomponentbase_modifiedonbehalfby](solutioncomponent.md#BKMK_lk_solutioncomponentbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponent|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionrolebase_createdonbehalfby"></a> lk_connectionrolebase_createdonbehalfby

Same as connectionrole table [lk_connectionrolebase_createdonbehalfby](connectionrole.md#BKMK_lk_connectionrolebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionrole|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_connectionrolebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_actioncardbase_createdby"></a> lk_actioncardbase_createdby

Same as actioncard table [lk_actioncardbase_createdby](actioncard.md#BKMK_lk_actioncardbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_actioncardbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby

Same as sdkmessageprocessingstepsecureconfig table [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](sdkmessageprocessingstepsecureconfig.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepsecureconfig|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_webresourcebase_modifiedonbehalfby"></a> lk_webresourcebase_modifiedonbehalfby

Same as webresource table [lk_webresourcebase_modifiedonbehalfby](webresource.md#BKMK_lk_webresourcebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|webresource|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_webresourcebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_letter"></a> user_letter

Same as letter table [user_letter](letter.md#BKMK_user_letter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_letter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_tracelog_modifiedonbehalfby"></a> lk_tracelog_modifiedonbehalfby

Same as tracelog table [lk_tracelog_modifiedonbehalfby](tracelog.md#BKMK_lk_tracelog_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|tracelog|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_tracelog_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonedefinition_createdby"></a> lk_timezonedefinition_createdby

Same as timezonedefinition table [lk_timezonedefinition_createdby](timezonedefinition.md#BKMK_lk_timezonedefinition_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonedefinition|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonedefinition_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_reportcategory_createdonbehalfby"></a> lk_reportcategory_createdonbehalfby

Same as reportcategory table [lk_reportcategory_createdonbehalfby](reportcategory.md#BKMK_lk_reportcategory_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|reportcategory|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_reportcategory_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_plugintype"></a> createdby_plugintype

Same as plugintype table [createdby_plugintype](plugintype.md#BKMK_createdby_plugintype) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintype|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_plugintype|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organization_createdonbehalfby"></a> lk_organization_createdonbehalfby

Same as organization table [lk_organization_createdonbehalfby](organization.md#BKMK_lk_organization_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organization_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_calendar_modifiedonbehalfby"></a> lk_calendar_modifiedonbehalfby

Same as calendar table [lk_calendar_modifiedonbehalfby](calendar.md#BKMK_lk_calendar_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|calendar|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_calendar_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slakpiinstancebase_modifiedby"></a> lk_slakpiinstancebase_modifiedby

Same as slakpiinstance table [lk_slakpiinstancebase_modifiedby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slakpiinstancebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_plugintracelog"></a> createdby_plugintracelog

Same as plugintracelog table [createdby_plugintracelog](plugintracelog.md#BKMK_createdby_plugintracelog) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintracelog|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_plugintracelog|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfiginstance_modifiedby"></a> lk_appconfiginstance_modifiedby

Same as appconfiginstance table [lk_appconfiginstance_modifiedby](appconfiginstance.md#BKMK_lk_appconfiginstance_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfiginstance|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfiginstance_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_picklistmapping_createdonbehalfby"></a> lk_picklistmapping_createdonbehalfby

Same as picklistmapping table [lk_picklistmapping_createdonbehalfby](picklistmapping.md#BKMK_lk_picklistmapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|picklistmapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_picklistmapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticleviews_createdby"></a> lk_knowledgearticleviews_createdby

Same as knowledgearticleviews table [lk_knowledgearticleviews_createdby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticleviews|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticleviews_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_Imports"></a> SystemUser_Imports

Same as import table [SystemUser_Imports](import.md#BKMK_SystemUser_Imports) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_Imports|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_sdkmessage"></a> modifiedby_sdkmessage

Same as sdkmessage table [modifiedby_sdkmessage](sdkmessage.md#BKMK_modifiedby_sdkmessage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_sdkmessage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ownermapping_createdonbehalfby"></a> lk_ownermapping_createdonbehalfby

Same as ownermapping table [lk_ownermapping_createdonbehalfby](ownermapping.md#BKMK_lk_ownermapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|ownermapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ownermapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticlecomment_createdonbehalfby"></a> lk_kbarticlecomment_createdonbehalfby

Same as kbarticlecomment table [lk_kbarticlecomment_createdonbehalfby](kbarticlecomment.md#BKMK_lk_kbarticlecomment_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticlecomment|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticlecomment_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_navigationsetting_modifiedonbehalfby"></a> lk_navigationsetting_modifiedonbehalfby

Same as navigationsetting table [lk_navigationsetting_modifiedonbehalfby](navigationsetting.md#BKMK_lk_navigationsetting_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|navigationsetting|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_navigationsetting_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonerule_createdonbehalfby"></a> lk_timezonerule_createdonbehalfby

Same as timezonerule table [lk_timezonerule_createdonbehalfby](timezonerule.md#BKMK_lk_timezonerule_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonerule|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonerule_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_templatebase_createdby"></a> lk_templatebase_createdby

Same as template table [lk_templatebase_createdby](template.md#BKMK_lk_templatebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_templatebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userformbase_modifiedonbehalfby"></a> lk_userformbase_modifiedonbehalfby

Same as userform table [lk_userformbase_modifiedonbehalfby](userform.md#BKMK_lk_userformbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userformbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby"></a> lk_mobileofflineprofileitemassociation_createdonbehalfby

Same as mobileofflineprofileitemassociation table [lk_mobileofflineprofileitemassociation_createdonbehalfby](mobileofflineprofileitemassociation.md#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitemassociation|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mobileofflineprofileitemassociation_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customeraddress_createdonbehalfby"></a> lk_customeraddress_createdonbehalfby

Same as customeraddress table [lk_customeraddress_createdonbehalfby](customeraddress.md#BKMK_lk_customeraddress_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customeraddress|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customeraddress_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importfilebase_modifiedby"></a> lk_importfilebase_modifiedby

Same as importfile table [lk_importfilebase_modifiedby](importfile.md#BKMK_lk_importfilebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importfilebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_accountbase_modifiedby"></a> lk_accountbase_modifiedby

Same as account table [lk_accountbase_modifiedby](account.md#BKMK_lk_accountbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_accountbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_personaldocumenttemplatebase_modifiedonbehalfby"></a> lk_personaldocumenttemplatebase_modifiedonbehalfby

Same as personaldocumenttemplate table [lk_personaldocumenttemplatebase_modifiedonbehalfby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|personaldocumenttemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_personaldocumenttemplatebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_category_createdby"></a> lk_category_createdby

Same as category table [lk_category_createdby](category.md#BKMK_lk_category_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_category_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontroldefaultconfig_modifiedby"></a> lk_customcontroldefaultconfig_modifiedby

Same as customcontroldefaultconfig table [lk_customcontroldefaultconfig_modifiedby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontroldefaultconfig|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontroldefaultconfig_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_SocialProfile_modifiedonbehalfby"></a> lk_SocialProfile_modifiedonbehalfby

Same as socialprofile table [lk_SocialProfile_modifiedonbehalfby](socialprofile.md#BKMK_lk_SocialProfile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_SocialProfile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_fax"></a> user_fax

Same as fax table [user_fax](fax.md#BKMK_user_fax) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_fax|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activitypointer_modifiedonbehalfby"></a> lk_activitypointer_modifiedonbehalfby

Same as activitypointer table [lk_activitypointer_modifiedonbehalfby](activitypointer.md#BKMK_lk_activitypointer_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_activitypointer_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_feedback_createdonbehalfby"></a> lk_feedback_createdonbehalfby

Same as feedback table [lk_feedback_createdonbehalfby](feedback.md#BKMK_lk_feedback_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_feedback_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodulecomponent_createdby"></a> lk_appmodulecomponent_createdby

Same as appmodulecomponent table [lk_appmodulecomponent_createdby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodulecomponent|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appmodulecomponent_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointsitebase_modifiedby"></a> lk_sharepointsitebase_modifiedby

Same as sharepointsite table [lk_sharepointsitebase_modifiedby](sharepointsite.md#BKMK_lk_sharepointsitebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointsitebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby"></a> lk_sdkmessageprocessingstepimage_createdonbehalfby

Same as sdkmessageprocessingstepimage table [lk_sdkmessageprocessingstepimage_createdonbehalfby](sdkmessageprocessingstepimage.md#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepimage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessageprocessingstepimage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importlog_createdonbehalfby"></a> lk_importlog_createdonbehalfby

Same as importlog table [lk_importlog_createdonbehalfby](importlog.md#BKMK_lk_importlog_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importlog_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_executedby"></a> lk_processsession_executedby

Same as processsession table [lk_processsession_executedby](processsession.md#BKMK_lk_processsession_executedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|executedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_executedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrol_modifiedby"></a> lk_customcontrol_modifiedby

Same as customcontrol table [lk_customcontrol_modifiedby](customcontrol.md#BKMK_lk_customcontrol_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrol|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrol_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrolresource_createdonbehalfby"></a> lk_customcontrolresource_createdonbehalfby

Same as customcontrolresource table [lk_customcontrolresource_createdonbehalfby](customcontrolresource.md#BKMK_lk_customcontrolresource_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrolresource|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrolresource_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_DuplicateMatchingRecord"></a> SystemUser_DuplicateMatchingRecord

Same as duplicaterecord table [SystemUser_DuplicateMatchingRecord](duplicaterecord.md#BKMK_SystemUser_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_sdkmessageprocessingstepimage"></a> createdby_sdkmessageprocessingstepimage

Same as sdkmessageprocessingstepimage table [createdby_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_createdby_sdkmessageprocessingstepimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepimage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_sdkmessageprocessingstepimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionbase_createdonbehalfby"></a> lk_connectionbase_createdonbehalfby

Same as connection table [lk_connectionbase_createdonbehalfby](connection.md#BKMK_lk_connectionbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connectionbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrol_createdby"></a> lk_customcontrol_createdby

Same as customcontrol table [lk_customcontrol_createdby](customcontrol.md#BKMK_lk_customcontrol_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrol|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrol_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrolresource_modifiedonbehalfby"></a> lk_customcontrolresource_modifiedonbehalfby

Same as customcontrolresource table [lk_customcontrolresource_modifiedonbehalfby](customcontrolresource.md#BKMK_lk_customcontrolresource_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrolresource|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrolresource_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonerule_modifiedby"></a> lk_timezonerule_modifiedby

Same as timezonerule table [lk_timezonerule_modifiedby](timezonerule.md#BKMK_lk_timezonerule_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonerule|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonerule_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ACIViewMapper_createdonbehalfby"></a> lk_ACIViewMapper_createdonbehalfby

Same as aciviewmapper table [lk_ACIViewMapper_createdonbehalfby](aciviewmapper.md#BKMK_lk_ACIViewMapper_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|aciviewmapper|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ACIViewMapper_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_audit_userid"></a> lk_audit_userid

Same as audit table [lk_audit_userid](audit.md#BKMK_lk_audit_userid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|audit|
|ReferencingAttribute|userid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_audit_userid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutionbase_createdonbehalfby"></a> lk_solutionbase_createdonbehalfby

Same as solution table [lk_solutionbase_createdonbehalfby](solution.md#BKMK_lk_solutionbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solution|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solutionbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby"></a> lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby

Same as fixedmonthlyfiscalcalendar table [lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fixedmonthlyfiscalcalendar|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_OwnerMapping_SystemUser"></a> OwnerMapping_SystemUser

Same as ownermapping table [OwnerMapping_SystemUser](ownermapping.md#BKMK_OwnerMapping_SystemUser) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|ownermapping|
|ReferencingAttribute|targetsystemuserid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|OwnerMapping_SystemUser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_columnmapping_modifiedby"></a> lk_columnmapping_modifiedby

Same as columnmapping table [lk_columnmapping_modifiedby](columnmapping.md#BKMK_lk_columnmapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|columnmapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_columnmapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisheraddressbase_modifiedby"></a> lk_publisheraddressbase_modifiedby

Same as publisheraddress table [lk_publisheraddressbase_modifiedby](publisheraddress.md#BKMK_lk_publisheraddressbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisheraddress|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisheraddressbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_accountbase_createdby"></a> lk_accountbase_createdby

Same as account table [lk_accountbase_createdby](account.md#BKMK_lk_accountbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_accountbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedquerybase_modifiedby"></a> lk_savedquerybase_modifiedby

Same as savedquery table [lk_savedquerybase_modifiedby](savedquery.md#BKMK_lk_savedquerybase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedquery|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedquerybase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_MobileOfflineProfile_modifiedby"></a> lk_MobileOfflineProfile_modifiedby

Same as mobileofflineprofile table [lk_MobileOfflineProfile_modifiedby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_MobileOfflineProfile_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_quarterlyfiscalcalendar_createdby"></a> lk_quarterlyfiscalcalendar_createdby

Same as quarterlyfiscalcalendar table [lk_quarterlyfiscalcalendar_createdby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|quarterlyfiscalcalendar|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_quarterlyfiscalcalendar_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonedefinition_modifiedonbehalfby"></a> lk_timezonedefinition_modifiedonbehalfby

Same as timezonedefinition table [lk_timezonedefinition_modifiedonbehalfby](timezonedefinition.md#BKMK_lk_timezonedefinition_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonedefinition|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonedefinition_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organization_modifiedonbehalfby"></a> lk_organization_modifiedonbehalfby

Same as organization table [lk_organization_modifiedonbehalfby](organization.md#BKMK_lk_organization_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organization_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuser_connections1"></a> systemuser_connections1

Same as connection table [systemuser_connections1](connection.md#BKMK_systemuser_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_SiteMap_modifiedby"></a> lk_SiteMap_modifiedby

Same as sitemap table [lk_SiteMap_modifiedby](sitemap.md#BKMK_lk_SiteMap_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sitemap|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_SiteMap_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_documenttemplatebase_createdonbehalfby"></a> lk_documenttemplatebase_createdonbehalfby

Same as documenttemplate table [lk_documenttemplatebase_createdonbehalfby](documenttemplate.md#BKMK_lk_documenttemplatebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|documenttemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_documenttemplatebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticlebase_createdby"></a> lk_kbarticlebase_createdby

Same as kbarticle table [lk_kbarticlebase_createdby](kbarticle.md#BKMK_lk_kbarticlebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticle|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_kbarticlebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_emailserverprofile_createdby"></a> lk_emailserverprofile_createdby

Same as emailserverprofile table [lk_emailserverprofile_createdby](emailserverprofile.md#BKMK_lk_emailserverprofile_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_emailserverprofile_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby"></a> lk_quarterlyfiscalcalendar_modifiedonbehalfby

Same as quarterlyfiscalcalendar table [lk_quarterlyfiscalcalendar_modifiedonbehalfby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|quarterlyfiscalcalendar|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_quarterlyfiscalcalendar_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userquery_modifiedby"></a> lk_userquery_modifiedby

Same as userquery table [lk_userquery_modifiedby](userquery.md#BKMK_lk_userquery_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userquery_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedby"></a> lk_mobileofflineprofileitemassociation_modifiedby

Same as mobileofflineprofileitemassociation table [lk_mobileofflineprofileitemassociation_modifiedby](mobileofflineprofileitemassociation.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitemassociation|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mobileofflineprofileitemassocaition_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticleviews_createdonbehalfby"></a> lk_knowledgearticleviews_createdonbehalfby

Same as knowledgearticleviews table [lk_knowledgearticleviews_createdonbehalfby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticleviews|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticleviews_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processtriggerbase_createdonbehalfby"></a> lk_processtriggerbase_createdonbehalfby

Same as processtrigger table [lk_processtriggerbase_createdonbehalfby](processtrigger.md#BKMK_lk_processtriggerbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processtrigger|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processtriggerbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_sdkmessageprocessingstepimage"></a> modifiedby_sdkmessageprocessingstepimage

Same as sdkmessageprocessingstepimage table [modifiedby_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_modifiedby_sdkmessageprocessingstepimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstepimage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_sdkmessageprocessingstepimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_phonecall_modifiedonbehalfby"></a> lk_phonecall_modifiedonbehalfby

Same as phonecall table [lk_phonecall_modifiedonbehalfby](phonecall.md#BKMK_lk_phonecall_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_phonecall_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowlog_createdby"></a> lk_workflowlog_createdby

Same as workflowlog table [lk_workflowlog_createdby](workflowlog.md#BKMK_lk_workflowlog_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_salespersonid"></a> lk_fixedmonthlyfiscalcalendar_salespersonid

Same as fixedmonthlyfiscalcalendar table [lk_fixedmonthlyfiscalcalendar_salespersonid](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_salespersonid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fixedmonthlyfiscalcalendar|
|ReferencingAttribute|salespersonid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fixedmonthlyfiscalcalendar_salespersonid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby"></a> lk_quarterlyfiscalcalendar_createdonbehalfby

Same as quarterlyfiscalcalendar table [lk_quarterlyfiscalcalendar_createdonbehalfby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|quarterlyfiscalcalendar|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_quarterlyfiscalcalendar_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teamtemplate_modifiedby"></a> lk_teamtemplate_modifiedby

Same as teamtemplate table [lk_teamtemplate_modifiedby](teamtemplate.md#BKMK_lk_teamtemplate_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|teamtemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_teamtemplate_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_userform"></a> user_userform

Same as userform table [user_userform](userform.md#BKMK_user_userform) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_userform|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_startedby"></a> lk_processsession_startedby

Same as processsession table [lk_processsession_startedby](processsession.md#BKMK_lk_processsession_startedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|startedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_startedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticleviews_modifiedonbehalfby"></a> lk_knowledgearticleviews_modifiedonbehalfby

Same as knowledgearticleviews table [lk_knowledgearticleviews_modifiedonbehalfby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticleviews|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticleviews_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_role_modifiedonbehalfby"></a> lk_role_modifiedonbehalfby

Same as role table [lk_role_modifiedonbehalfby](role.md#BKMK_lk_role_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_role_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_reportbase_modifiedby"></a> lk_reportbase_modifiedby

Same as report table [lk_reportbase_modifiedby](report.md#BKMK_lk_reportbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_reportbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_createdby"></a> lk_fixedmonthlyfiscalcalendar_createdby

Same as fixedmonthlyfiscalcalendar table [lk_fixedmonthlyfiscalcalendar_createdby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fixedmonthlyfiscalcalendar|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fixedmonthlyfiscalcalendar_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfigmaster_createdby"></a> lk_appconfigmaster_createdby

Same as appconfigmaster table [lk_appconfigmaster_createdby](appconfigmaster.md#BKMK_lk_appconfigmaster_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfigmaster|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfigmaster_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunitbase_modifiedby"></a> lk_businessunitbase_modifiedby

Same as businessunit table [lk_businessunitbase_modifiedby](businessunit.md#BKMK_lk_businessunitbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_businessunitbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_socialProfile_owning_user"></a> socialProfile_owning_user

Same as socialprofile table [socialProfile_owning_user](socialprofile.md#BKMK_socialProfile_owning_user) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|socialProfile_owning_user|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_task_modifiedby"></a> lk_task_modifiedby

Same as task table [lk_task_modifiedby](task.md#BKMK_lk_task_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_task_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slaitembase_createdby"></a> lk_slaitembase_createdby

Same as slaitem table [lk_slaitembase_createdby](slaitem.md#BKMK_lk_slaitembase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slaitembase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailboxtrackingfolder_createdonbehalfby"></a> lk_mailboxtrackingfolder_createdonbehalfby

Same as mailboxtrackingfolder table [lk_mailboxtrackingfolder_createdonbehalfby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailboxtrackingfolder_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_sdkmessageprocessingstep"></a> modifiedby_sdkmessageprocessingstep

Same as sdkmessageprocessingstep table [modifiedby_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_modifiedby_sdkmessageprocessingstep) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_sdkmessageprocessingstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicaterulebase_modifiedby"></a> lk_duplicaterulebase_modifiedby

Same as duplicaterule table [lk_duplicaterulebase_modifiedby](duplicaterule.md#BKMK_lk_duplicaterulebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicaterulebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurrencerulebase_createdonbehalfby"></a> lk_recurrencerulebase_createdonbehalfby

Same as recurrencerule table [lk_recurrencerulebase_createdonbehalfby](recurrencerule.md#BKMK_lk_recurrencerulebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurrencerule|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_recurrencerulebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationbase_modifiedby"></a> lk_organizationbase_modifiedby

Same as organization table [lk_organizationbase_modifiedby](organization.md#BKMK_lk_organizationbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organizationbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby"></a> lk_mailboxtrackingfolder_modifiedonbehalfby

Same as mailboxtrackingfolder table [lk_mailboxtrackingfolder_modifiedonbehalfby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailboxtrackingfolder_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_task_createdby"></a> lk_task_createdby

Same as task table [lk_task_createdby](task.md#BKMK_lk_task_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_task_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailboxtrackingfolder_createdby"></a> lk_mailboxtrackingfolder_createdby

Same as mailboxtrackingfolder table [lk_mailboxtrackingfolder_createdby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailboxtrackingfolder_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_personaldocumenttemplatebase_modifiedby"></a> lk_personaldocumenttemplatebase_modifiedby

Same as personaldocumenttemplate table [lk_personaldocumenttemplatebase_modifiedby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|personaldocumenttemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_personaldocumenttemplatebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processtriggerbase_modifiedby"></a> lk_processtriggerbase_modifiedby

Same as processtrigger table [lk_processtriggerbase_modifiedby](processtrigger.md#BKMK_lk_processtriggerbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processtrigger|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_processtriggerbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userquery_createdby"></a> lk_userquery_createdby

Same as userquery table [lk_userquery_createdby](userquery.md#BKMK_lk_userquery_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userquery_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_contact_owning_user"></a> contact_owning_user

Same as contact table [contact_owning_user](contact.md#BKMK_contact_owning_user) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|contact_owning_user|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailmergetemplate_createdonbehalfby"></a> lk_mailmergetemplate_createdonbehalfby

Same as mailmergetemplate table [lk_mailmergetemplate_createdonbehalfby](mailmergetemplate.md#BKMK_lk_mailmergetemplate_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailmergetemplate_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importjobbase_modifiedonbehalfby"></a> lk_importjobbase_modifiedonbehalfby

Same as importjob table [lk_importjobbase_modifiedonbehalfby](importjob.md#BKMK_lk_importjobbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importjob|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importjobbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontroldefaultconfig_createdby"></a> lk_customcontroldefaultconfig_createdby

Same as customcontroldefaultconfig table [lk_customcontroldefaultconfig_createdby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontroldefaultconfig|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontroldefaultconfig_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedquery_createdonbehalfby"></a> lk_savedquery_createdonbehalfby

Same as savedquery table [lk_savedquery_createdonbehalfby](savedquery.md#BKMK_lk_savedquery_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedquery|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedquery_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_accounts"></a> system_user_accounts

Same as account table [system_user_accounts](account.md#BKMK_system_user_accounts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|preferredsystemuserid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|system_user_accounts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_systemuser_createdonbehalfby"></a> lk_systemuser_createdonbehalfby

Same as systemuser table [lk_systemuser_createdonbehalfby](systemuser.md#BKMK_lk_systemuser_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_systemuser_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrol_modifiedonbehalfby"></a> lk_customcontrol_modifiedonbehalfby

Same as customcontrol table [lk_customcontrol_modifiedonbehalfby](customcontrol.md#BKMK_lk_customcontrol_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrol|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrol_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appointment_modifiedonbehalfby"></a> lk_appointment_modifiedonbehalfby

Same as appointment table [lk_appointment_modifiedonbehalfby](appointment.md#BKMK_lk_appointment_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appointment_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_knowledgearticleviews_modifiedby"></a> lk_knowledgearticleviews_modifiedby

Same as knowledgearticleviews table [lk_knowledgearticleviews_modifiedby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticleviews|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_knowledgearticleviews_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfigmaster_modifiedonbehalfby"></a> lk_appconfigmaster_modifiedonbehalfby

Same as appconfigmaster table [lk_appconfigmaster_modifiedonbehalfby](appconfigmaster.md#BKMK_lk_appconfigmaster_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfigmaster|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfigmaster_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importbase_createdby"></a> lk_importbase_createdby

Same as import table [lk_importbase_createdby](import.md#BKMK_lk_importbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ACIViewMapper_modifiedonbehalfby"></a> lk_ACIViewMapper_modifiedonbehalfby

Same as aciviewmapper table [lk_ACIViewMapper_modifiedonbehalfby](aciviewmapper.md#BKMK_lk_ACIViewMapper_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|aciviewmapper|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ACIViewMapper_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutionbase_modifiedonbehalfby"></a> lk_solutionbase_modifiedonbehalfby

Same as solution table [lk_solutionbase_modifiedonbehalfby](solution.md#BKMK_lk_solutionbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solution|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solutionbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_DisplayStringbase_modifiedonbehalfby"></a> lk_DisplayStringbase_modifiedonbehalfby

Same as displaystring table [lk_DisplayStringbase_modifiedonbehalfby](displaystring.md#BKMK_lk_DisplayStringbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|displaystring|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_DisplayStringbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annotationbase_modifiedby"></a> lk_annotationbase_modifiedby

Same as annotation table [lk_annotationbase_modifiedby](annotation.md#BKMK_lk_annotationbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annotationbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonerule_modifiedonbehalfby"></a> lk_timezonerule_modifiedonbehalfby

Same as timezonerule table [lk_timezonerule_modifiedonbehalfby](timezonerule.md#BKMK_lk_timezonerule_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonerule|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonerule_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importjobbase_createdby"></a> lk_importjobbase_createdby

Same as importjob table [lk_importjobbase_createdby](importjob.md#BKMK_lk_importjobbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importjob|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importjobbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_feedback_createdby"></a> lk_feedback_createdby

Same as feedback table [lk_feedback_createdby](feedback.md#BKMK_lk_feedback_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_feedback_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonelocalizedname_modifiedby"></a> lk_timezonelocalizedname_modifiedby

Same as timezonelocalizedname table [lk_timezonelocalizedname_modifiedby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonelocalizedname|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonelocalizedname_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailmergetemplatebase_createdby"></a> lk_mailmergetemplatebase_createdby

Same as mailmergetemplate table [lk_mailmergetemplatebase_createdby](mailmergetemplate.md#BKMK_lk_mailmergetemplatebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailmergetemplatebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_pluginassembly"></a> createdby_pluginassembly

Same as pluginassembly table [createdby_pluginassembly](pluginassembly.md#BKMK_createdby_pluginassembly) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginassembly|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_pluginassembly|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfiginstance_modifiedonbehalfby"></a> lk_appconfiginstance_modifiedonbehalfby

Same as appconfiginstance table [lk_appconfiginstance_modifiedonbehalfby](appconfiginstance.md#BKMK_lk_appconfiginstance_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfiginstance|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfiginstance_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userform_modifiedby"></a> lk_userform_modifiedby

Same as userform table [lk_userform_modifiedby](userform.md#BKMK_lk_userform_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userform_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisherbase_createdonbehalfby"></a> lk_publisherbase_createdonbehalfby

Same as publisher table [lk_publisherbase_createdonbehalfby](publisher.md#BKMK_lk_publisherbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisher|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisherbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurrencerule_createdby"></a> lk_recurrencerule_createdby

Same as recurrencerule table [lk_recurrencerule_createdby](recurrencerule.md#BKMK_lk_recurrencerule_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurrencerule|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_recurrencerule_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slakpiinstancebase_modifiedonbehalfby"></a> lk_slakpiinstancebase_modifiedonbehalfby

Same as slakpiinstance table [lk_slakpiinstancebase_modifiedonbehalfby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slakpiinstancebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_ImportFiles"></a> SystemUser_ImportFiles

Same as importfile table [SystemUser_ImportFiles](importfile.md#BKMK_SystemUser_ImportFiles) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_ImportFiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_modifiedby"></a> lk_processsession_modifiedby

Same as processsession table [lk_processsession_modifiedby](processsession.md#BKMK_lk_processsession_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_modifiedby"></a> lk_translationprocess_modifiedby

Same as translationprocess table [lk_translationprocess_modifiedby](translationprocess.md#BKMK_lk_translationprocess_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_translationprocess_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annualfiscalcalendar_modifiedby"></a> lk_annualfiscalcalendar_modifiedby

Same as annualfiscalcalendar table [lk_annualfiscalcalendar_modifiedby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annualfiscalcalendar|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annualfiscalcalendar_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_task"></a> user_task

Same as task table [user_task](task.md#BKMK_user_task) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_task|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurrencerulebase_modifiedonbehalfby"></a> lk_recurrencerulebase_modifiedonbehalfby

Same as recurrencerule table [lk_recurrencerulebase_modifiedonbehalfby](recurrencerule.md#BKMK_lk_recurrencerulebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurrencerule|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_recurrencerulebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_phonecall_createdby"></a> lk_phonecall_createdby

Same as phonecall table [lk_phonecall_createdby](phonecall.md#BKMK_lk_phonecall_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_phonecall_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_templatebase_modifiedonbehalfby"></a> lk_templatebase_modifiedonbehalfby

Same as template table [lk_templatebase_modifiedonbehalfby](template.md#BKMK_lk_templatebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_templatebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fax_modifiedonbehalfby"></a> lk_fax_modifiedonbehalfby

Same as fax table [lk_fax_modifiedonbehalfby](fax.md#BKMK_lk_fax_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_fax_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_contact_createdonbehalfby"></a> lk_contact_createdonbehalfby

Same as contact table [lk_contact_createdonbehalfby](contact.md#BKMK_lk_contact_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_contact_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontroldefaultconfig_createdonbehalfby"></a> lk_customcontroldefaultconfig_createdonbehalfby

Same as customcontroldefaultconfig table [lk_customcontroldefaultconfig_createdonbehalfby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontroldefaultconfig|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontroldefaultconfig_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisheraddressbase_createdonbehalfby"></a> lk_publisheraddressbase_createdonbehalfby

Same as publisheraddress table [lk_publisheraddressbase_createdonbehalfby](publisheraddress.md#BKMK_lk_publisheraddressbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisheraddress|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisheraddressbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annualfiscalcalendar_modifiedonbehalfby"></a> lk_annualfiscalcalendar_modifiedonbehalfby

Same as annualfiscalcalendar table [lk_annualfiscalcalendar_modifiedonbehalfby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annualfiscalcalendar|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annualfiscalcalendar_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_semiannualfiscalcalendar_modifiedby"></a> lk_semiannualfiscalcalendar_modifiedby

Same as semiannualfiscalcalendar table [lk_semiannualfiscalcalendar_modifiedby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|semiannualfiscalcalendar|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_semiannualfiscalcalendar_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_socialactivity_createdby"></a> lk_socialactivity_createdby

Same as socialactivity table [lk_socialactivity_createdby](socialactivity.md#BKMK_lk_socialactivity_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_socialactivity_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_SiteMap_createdby"></a> lk_SiteMap_createdby

Same as sitemap table [lk_SiteMap_createdby](sitemap.md#BKMK_lk_SiteMap_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sitemap|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_SiteMap_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_syncerrorbase_modifiedby"></a> lk_syncerrorbase_modifiedby

Same as syncerror table [lk_syncerrorbase_modifiedby](syncerror.md#BKMK_lk_syncerrorbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_syncerrorbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_calendar_createdby"></a> lk_calendar_createdby

Same as calendar table [lk_calendar_createdby](calendar.md#BKMK_lk_calendar_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|calendar|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_calendar_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby"></a> lk_semiannualfiscalcalendar_modifiedonbehalfby

Same as semiannualfiscalcalendar table [lk_semiannualfiscalcalendar_modifiedonbehalfby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|semiannualfiscalcalendar|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_semiannualfiscalcalendar_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_modifiedby"></a> lk_fixedmonthlyfiscalcalendar_modifiedby

Same as fixedmonthlyfiscalcalendar table [lk_fixedmonthlyfiscalcalendar_modifiedby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fixedmonthlyfiscalcalendar|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fixedmonthlyfiscalcalendar_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_DuplicateBaseRecord"></a> SystemUser_DuplicateBaseRecord

Same as duplicaterecord table [SystemUser_DuplicateBaseRecord](duplicaterecord.md#BKMK_SystemUser_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importentitymapping_createdby"></a> lk_importentitymapping_createdby

Same as importentitymapping table [lk_importentitymapping_createdby](importentitymapping.md#BKMK_lk_importentitymapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importentitymapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importentitymapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queueitembase_createdby"></a> lk_queueitembase_createdby

Same as queueitem table [lk_queueitembase_createdby](queueitem.md#BKMK_lk_queueitembase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queueitembase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessage_createdonbehalfby"></a> lk_sdkmessage_createdonbehalfby

Same as sdkmessage table [lk_sdkmessage_createdonbehalfby](sdkmessage.md#BKMK_lk_sdkmessage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_plugintypestatistic"></a> createdby_plugintypestatistic

Same as plugintypestatistic table [createdby_plugintypestatistic](plugintypestatistic.md#BKMK_createdby_plugintypestatistic) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintypestatistic|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_plugintypestatistic|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_picklistmapping_modifiedby"></a> lk_picklistmapping_modifiedby

Same as picklistmapping table [lk_picklistmapping_modifiedby](picklistmapping.md#BKMK_lk_picklistmapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|picklistmapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_picklistmapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_team_modifiedonbehalfby"></a> lk_team_modifiedonbehalfby

Same as team table [lk_team_modifiedonbehalfby](team.md#BKMK_lk_team_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_team_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunitnewsarticle_modifiedonbehalfby"></a> lk_businessunitnewsarticle_modifiedonbehalfby

Same as businessunitnewsarticle table [lk_businessunitnewsarticle_modifiedonbehalfby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticle_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunitnewsarticle|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_businessunitnewsarticle_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_ImportLogs"></a> SystemUser_ImportLogs

Same as importlog table [SystemUser_ImportLogs](importlog.md#BKMK_SystemUser_ImportLogs) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_ImportLogs|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_plugintypestatisticbase_modifiedonbehalfby"></a> lk_plugintypestatisticbase_modifiedonbehalfby

Same as plugintypestatistic table [lk_plugintypestatisticbase_modifiedonbehalfby](plugintypestatistic.md#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintypestatistic|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_plugintypestatisticbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_tracelog_createdby"></a> lk_tracelog_createdby

Same as tracelog table [lk_tracelog_createdby](tracelog.md#BKMK_lk_tracelog_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|tracelog|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_tracelog_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teambase_administratorid"></a> lk_teambase_administratorid

Same as team table [lk_teambase_administratorid](team.md#BKMK_lk_teambase_administratorid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|administratorid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_teambase_administratorid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedqueryvisualizationbase_createdby"></a> lk_savedqueryvisualizationbase_createdby

Same as savedqueryvisualization table [lk_savedqueryvisualizationbase_createdby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedqueryvisualization|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedqueryvisualizationbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_primaryauthorid"></a> knowledgearticle_primaryauthorid

Same as knowledgearticle table [knowledgearticle_primaryauthorid](knowledgearticle.md#BKMK_knowledgearticle_primaryauthorid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|primaryauthorid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_primaryauthorid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_createdonbehalfby"></a> lk_fixedmonthlyfiscalcalendar_createdonbehalfby

Same as fixedmonthlyfiscalcalendar table [lk_fixedmonthlyfiscalcalendar_createdonbehalfby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fixedmonthlyfiscalcalendar|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fixedmonthlyfiscalcalendar_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_email_createdby"></a> lk_email_createdby

Same as email table [lk_email_createdby](email.md#BKMK_lk_email_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_email_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_monthlyfiscalcalendar_createdby"></a> lk_monthlyfiscalcalendar_createdby

Same as monthlyfiscalcalendar table [lk_monthlyfiscalcalendar_createdby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|monthlyfiscalcalendar|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_monthlyfiscalcalendar_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queuebase_createdby"></a> lk_queuebase_createdby

Same as queue table [lk_queuebase_createdby](queue.md#BKMK_lk_queuebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queuebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodulecomponent_createdonbehalfby"></a> lk_appmodulecomponent_createdonbehalfby

Same as appmodulecomponent table [lk_appmodulecomponent_createdonbehalfby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodulecomponent|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_appmodulecomponent_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_personaldocumenttemplatebase_createdonbehalfby"></a> lk_personaldocumenttemplatebase_createdonbehalfby

Same as personaldocumenttemplate table [lk_personaldocumenttemplatebase_createdonbehalfby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|personaldocumenttemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_personaldocumenttemplatebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedqueryvisualizationbase_createdonbehalfby"></a> lk_savedqueryvisualizationbase_createdonbehalfby

Same as savedqueryvisualization table [lk_savedqueryvisualizationbase_createdonbehalfby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedqueryvisualization|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedqueryvisualizationbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_newprocess_createdby"></a> lk_newprocess_createdby

Same as newprocess table [lk_newprocess_createdby](newprocess.md#BKMK_lk_newprocess_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_newprocess_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_category_createdonbehalfby"></a> lk_category_createdonbehalfby

Same as category table [lk_category_createdonbehalfby](category.md#BKMK_lk_category_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_category_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_newprocess_modifiedonbehalfby"></a> lk_newprocess_modifiedonbehalfby

Same as newprocess table [lk_newprocess_modifiedonbehalfby](newprocess.md#BKMK_lk_newprocess_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_newprocess_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_feedback_closedby"></a> lk_feedback_closedby

Same as feedback table [lk_feedback_closedby](feedback.md#BKMK_lk_feedback_closedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|closedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_feedback_closedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_semiannualfiscalcalendar_createdby"></a> lk_semiannualfiscalcalendar_createdby

Same as semiannualfiscalcalendar table [lk_semiannualfiscalcalendar_createdby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|semiannualfiscalcalendar|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_semiannualfiscalcalendar_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_duplicateruleconditionbase_modifiedby"></a> lk_duplicateruleconditionbase_modifiedby

Same as duplicaterulecondition table [lk_duplicateruleconditionbase_modifiedby](duplicaterulecondition.md#BKMK_lk_duplicateruleconditionbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterulecondition|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicateruleconditionbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_primary_user"></a> queue_primary_user

Same as queue table [queue_primary_user](queue.md#BKMK_queue_primary_user) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|primaryuserid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|queue_primary_user|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_email"></a> user_email

Same as email table [user_email](email.md#BKMK_user_email) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_email|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_reportbase_createdby"></a> lk_reportbase_createdby

Same as report table [lk_reportbase_createdby](report.md#BKMK_lk_reportbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_reportbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appointment_createdby"></a> lk_appointment_createdby

Same as appointment table [lk_appointment_createdby](appointment.md#BKMK_lk_appointment_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appointment_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_letter_modifiedby"></a> lk_letter_modifiedby

Same as letter table [lk_letter_modifiedby](letter.md#BKMK_lk_letter_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_letter_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrol_createdonbehalfby"></a> lk_customcontrol_createdonbehalfby

Same as customcontrol table [lk_customcontrol_createdonbehalfby](customcontrol.md#BKMK_lk_customcontrol_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrol|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrol_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usersettingsbase_modifiedby"></a> lk_usersettingsbase_modifiedby

Same as usersettings table [lk_usersettingsbase_modifiedby](usersettings.md#BKMK_lk_usersettingsbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_usersettingsbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queueitembase_modifiedby"></a> lk_queueitembase_modifiedby

Same as queueitem table [lk_queueitembase_modifiedby](queueitem.md#BKMK_lk_queueitembase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queueitembase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby"></a> lk_sdkmessageprocessingstep_modifiedonbehalfby

Same as sdkmessageprocessingstep table [lk_sdkmessageprocessingstep_modifiedonbehalfby](sdkmessageprocessingstep.md#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessageprocessingstep_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_pluginassembly"></a> modifiedby_pluginassembly

Same as pluginassembly table [modifiedby_pluginassembly](pluginassembly.md#BKMK_modifiedby_pluginassembly) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginassembly|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_pluginassembly|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedby"></a> lk_sharepointdocumentlocationbase_modifiedby

Same as sharepointdocumentlocation table [lk_sharepointdocumentlocationbase_modifiedby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointdocumentlocationbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_activity_parties"></a> system_user_activity_parties

Same as activityparty table [system_user_activity_parties](activityparty.md#BKMK_system_user_activity_parties) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|partyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|system_user_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annualfiscalcalendar_salespersonid"></a> lk_annualfiscalcalendar_salespersonid

Same as annualfiscalcalendar table [lk_annualfiscalcalendar_salespersonid](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_salespersonid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annualfiscalcalendar|
|ReferencingAttribute|salespersonid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annualfiscalcalendar_salespersonid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_AsyncOperations"></a> SystemUser_AsyncOperations

Same as asyncoperation table [SystemUser_AsyncOperations](asyncoperation.md#BKMK_SystemUser_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_publisheraddressbase_createdby"></a> lk_publisheraddressbase_createdby

Same as publisheraddress table [lk_publisheraddressbase_createdby](publisheraddress.md#BKMK_lk_publisheraddressbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|publisheraddress|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_publisheraddressbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_import_modifiedonbehalfby"></a> lk_import_modifiedonbehalfby

Same as import table [lk_import_modifiedonbehalfby](import.md#BKMK_lk_import_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_import_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queuebase_modifiedby"></a> lk_queuebase_modifiedby

Same as queue table [lk_queuebase_modifiedby](queue.md#BKMK_lk_queuebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queuebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_ImportMaps"></a> SystemUser_ImportMaps

Same as importmap table [SystemUser_ImportMaps](importmap.md#BKMK_SystemUser_ImportMaps) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_ImportMaps|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_workflow_modifiedonbehalfby"></a> workflow_modifiedonbehalfby

Same as workflow table [workflow_modifiedonbehalfby](workflow.md#BKMK_workflow_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_category_modifiedby"></a> lk_category_modifiedby

Same as category table [lk_category_modifiedby](category.md#BKMK_lk_category_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_category_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_SiteMap_createdonbehalfby"></a> lk_SiteMap_createdonbehalfby

Same as sitemap table [lk_SiteMap_createdonbehalfby](sitemap.md#BKMK_lk_SiteMap_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sitemap|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_SiteMap_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_webresource_modifiedby"></a> webresource_modifiedby

Same as webresource table [webresource_modifiedby](webresource.md#BKMK_webresource_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|webresource|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|webresource_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_sdkmessage"></a> createdby_sdkmessage

Same as sdkmessage table [createdby_sdkmessage](sdkmessage.md#BKMK_createdby_sdkmessage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_sdkmessage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importlogbase_modifiedby"></a> lk_importlogbase_modifiedby

Same as importlog table [lk_importlogbase_modifiedby](importlog.md#BKMK_lk_importlogbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importlogbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importjobbase_createdonbehalfby"></a> lk_importjobbase_createdonbehalfby

Same as importjob table [lk_importjobbase_createdonbehalfby](importjob.md#BKMK_lk_importjobbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importjob|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importjobbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby"></a> lk_monthlyfiscalcalendar_modifiedonbehalfby

Same as monthlyfiscalcalendar table [lk_monthlyfiscalcalendar_modifiedonbehalfby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|monthlyfiscalcalendar|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_monthlyfiscalcalendar_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transactioncurrency_createdonbehalfby"></a> lk_transactioncurrency_createdonbehalfby

Same as transactioncurrency table [lk_transactioncurrency_createdonbehalfby](transactioncurrency.md#BKMK_lk_transactioncurrency_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transactioncurrency|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transactioncurrency_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bulkdeleteoperation_createdonbehalfby"></a> lk_bulkdeleteoperation_createdonbehalfby

Same as bulkdeleteoperation table [lk_bulkdeleteoperation_createdonbehalfby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperation_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeleteoperation|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_bulkdeleteoperation_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_plugintypestatistic"></a> modifiedby_plugintypestatistic

Same as plugintypestatistic table [modifiedby_plugintypestatistic](plugintypestatistic.md#BKMK_modifiedby_plugintypestatistic) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintypestatistic|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_plugintypestatistic|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_actioncardbase_modifiedonbehalfby"></a> lk_actioncardbase_modifiedonbehalfby

Same as actioncard table [lk_actioncardbase_modifiedonbehalfby](actioncard.md#BKMK_lk_actioncardbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_actioncardbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurringappointmentmaster_createdby"></a> lk_recurringappointmentmaster_createdby

Same as recurringappointmentmaster table [lk_recurringappointmentmaster_createdby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recurringappointmentmaster_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_DisplayStringbase_createdonbehalfby"></a> lk_DisplayStringbase_createdonbehalfby

Same as displaystring table [lk_DisplayStringbase_createdonbehalfby](displaystring.md#BKMK_lk_DisplayStringbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|displaystring|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_DisplayStringbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_audit_callinguserid"></a> lk_audit_callinguserid

Same as audit table [lk_audit_callinguserid](audit.md#BKMK_lk_audit_callinguserid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|audit|
|ReferencingAttribute|callinguserid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_audit_callinguserid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importfilebase_createdby"></a> lk_importfilebase_createdby

Same as importfile table [lk_importfilebase_createdby](importfile.md#BKMK_lk_importfilebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importfilebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importmap_modifiedonbehalfby"></a> lk_importmap_modifiedonbehalfby

Same as importmap table [lk_importmap_modifiedonbehalfby](importmap.md#BKMK_lk_importmap_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importmap_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_expiredprocess_modifiedonbehalfby"></a> lk_expiredprocess_modifiedonbehalfby

Same as expiredprocess table [lk_expiredprocess_modifiedonbehalfby](expiredprocess.md#BKMK_lk_expiredprocess_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_expiredprocess_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userqueryvisualizationbase_modifiedonbehalfby"></a> lk_userqueryvisualizationbase_modifiedonbehalfby

Same as userqueryvisualization table [lk_userqueryvisualizationbase_modifiedonbehalfby](userqueryvisualization.md#BKMK_lk_userqueryvisualizationbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userqueryvisualizationbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_semiannualfiscalcalendar_salespersonid"></a> lk_semiannualfiscalcalendar_salespersonid

Same as semiannualfiscalcalendar table [lk_semiannualfiscalcalendar_salespersonid](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_salespersonid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|semiannualfiscalcalendar|
|ReferencingAttribute|salespersonid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_semiannualfiscalcalendar_salespersonid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_report_createdonbehalfby"></a> lk_report_createdonbehalfby

Same as report table [lk_report_createdonbehalfby](report.md#BKMK_lk_report_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_report_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_canceledby"></a> lk_processsession_canceledby

Same as processsession table [lk_processsession_canceledby](processsession.md#BKMK_lk_processsession_canceledby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|canceledby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_canceledby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_SiteMap_modifiedonbehalfby"></a> lk_SiteMap_modifiedonbehalfby

Same as sitemap table [lk_SiteMap_modifiedonbehalfby](sitemap.md#BKMK_lk_SiteMap_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sitemap|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_SiteMap_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_SyncError"></a> SystemUser_SyncError

Same as syncerror table [SystemUser_SyncError](syncerror.md#BKMK_SystemUser_SyncError) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemUser_SyncError|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_socialactivity_modifiedby"></a> lk_socialactivity_modifiedby

Same as socialactivity table [lk_socialactivity_modifiedby](socialactivity.md#BKMK_lk_socialactivity_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_socialactivity_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_accountbase_modifiedonbehalfby"></a> lk_accountbase_modifiedonbehalfby

Same as account table [lk_accountbase_modifiedonbehalfby](account.md#BKMK_lk_accountbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_accountbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_subjectbase_createdby"></a> lk_subjectbase_createdby

Same as subject table [lk_subjectbase_createdby](subject.md#BKMK_lk_subjectbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|subject|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_subjectbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_MobileOfflineProfile_modifiedonbehalfby"></a> lk_MobileOfflineProfile_modifiedonbehalfby

Same as mobileofflineprofile table [lk_MobileOfflineProfile_modifiedonbehalfby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_MobileOfflineProfile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annotationbase_modifiedonbehalfby"></a> lk_annotationbase_modifiedonbehalfby

Same as annotation table [lk_annotationbase_modifiedonbehalfby](annotation.md#BKMK_lk_annotationbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annotationbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticletemplatebase_createdby"></a> lk_kbarticletemplatebase_createdby

Same as kbarticletemplate table [lk_kbarticletemplatebase_createdby](kbarticletemplate.md#BKMK_lk_kbarticletemplatebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticletemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticletemplatebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importbase_modifiedby"></a> lk_importbase_modifiedby

Same as import table [lk_importbase_modifiedby](import.md#BKMK_lk_importbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_connection_role"></a> modifiedby_connection_role

Same as connectionrole table [modifiedby_connection_role](connectionrole.md#BKMK_modifiedby_connection_role) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionrole|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_connection_role|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby"></a> lk_sharepointdocumentlocationbase_createdonbehalfby

Same as sharepointdocumentlocation table [lk_sharepointdocumentlocationbase_createdonbehalfby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointdocumentlocationbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_mailmergetemplatebase_modifiedby"></a> lk_mailmergetemplatebase_modifiedby

Same as mailmergetemplate table [lk_mailmergetemplatebase_modifiedby](mailmergetemplate.md#BKMK_lk_mailmergetemplatebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_mailmergetemplatebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userquery_createdonbehalfby"></a> lk_userquery_createdonbehalfby

Same as userquery table [lk_userquery_createdonbehalfby](userquery.md#BKMK_lk_userquery_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userquery_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transactioncurrencybase_createdby"></a> lk_transactioncurrencybase_createdby

Same as transactioncurrency table [lk_transactioncurrencybase_createdby](transactioncurrency.md#BKMK_lk_transactioncurrencybase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transactioncurrency|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transactioncurrencybase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_queue_createdonbehalfby"></a> lk_queue_createdonbehalfby

Same as queue table [lk_queue_createdonbehalfby](queue.md#BKMK_lk_queue_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_queue_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_MobileOfflineProfile_createdby"></a> lk_MobileOfflineProfile_createdby

Same as mobileofflineprofile table [lk_MobileOfflineProfile_createdby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_MobileOfflineProfile_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_serviceendpoint"></a> modifiedby_serviceendpoint

Same as serviceendpoint table [modifiedby_serviceendpoint](serviceendpoint.md#BKMK_modifiedby_serviceendpoint) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceendpoint|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_serviceendpoint|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appointment_modifiedby"></a> lk_appointment_modifiedby

Same as appointment table [lk_appointment_modifiedby](appointment.md#BKMK_lk_appointment_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appointment_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_picklistmapping_modifiedonbehalfby"></a> lk_picklistmapping_modifiedonbehalfby

Same as picklistmapping table [lk_picklistmapping_modifiedonbehalfby](picklistmapping.md#BKMK_lk_picklistmapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|picklistmapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_picklistmapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationmapping_createdonbehalfby"></a> lk_transformationmapping_createdonbehalfby

Same as transformationmapping table [lk_transformationmapping_createdonbehalfby](transformationmapping.md#BKMK_lk_transformationmapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationmapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationmapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_plugintypestatisticbase_createdonbehalfby"></a> lk_plugintypestatisticbase_createdonbehalfby

Same as plugintypestatistic table [lk_plugintypestatisticbase_createdonbehalfby](plugintypestatistic.md#BKMK_lk_plugintypestatisticbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintypestatistic|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_plugintypestatisticbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticletemplate_createdonbehalfby"></a> lk_kbarticletemplate_createdonbehalfby

Same as kbarticletemplate table [lk_kbarticletemplate_createdonbehalfby](kbarticletemplate.md#BKMK_lk_kbarticletemplate_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticletemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticletemplate_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ImportFile_SystemUser"></a> ImportFile_SystemUser

Same as importfile table [ImportFile_SystemUser](importfile.md#BKMK_ImportFile_SystemUser) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|recordsownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportFile_SystemUser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importmapbase_modifiedby"></a> lk_importmapbase_modifiedby

Same as importmap table [lk_importmapbase_modifiedby](importmap.md#BKMK_lk_importmapbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importmapbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userform_createdby"></a> lk_userform_createdby

Same as userform table [lk_userform_createdby](userform.md#BKMK_lk_userform_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userform_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_expiredprocess_createdby"></a> lk_expiredprocess_createdby

Same as expiredprocess table [lk_expiredprocess_createdby](expiredprocess.md#BKMK_lk_expiredprocess_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_expiredprocess_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userqueryvisualization_createdby"></a> lk_userqueryvisualization_createdby

Same as userqueryvisualization table [lk_userqueryvisualization_createdby](userqueryvisualization.md#BKMK_lk_userqueryvisualization_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userqueryvisualization_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ACIViewMapper_modifiedby"></a> lk_ACIViewMapper_modifiedby

Same as aciviewmapper table [lk_ACIViewMapper_modifiedby](aciviewmapper.md#BKMK_lk_ACIViewMapper_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|aciviewmapper|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ACIViewMapper_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_slabase"></a> user_slabase

Same as sla table [user_slabase](sla.md#BKMK_user_slabase) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_slabase|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annotationbase_createdby"></a> lk_annotationbase_createdby

Same as annotation table [lk_annotationbase_createdby](annotation.md#BKMK_lk_annotationbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annotationbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_webresource_createdby"></a> webresource_createdby

Same as webresource table [webresource_createdby](webresource.md#BKMK_webresource_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|webresource|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|webresource_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userqueryvisualizationbase_createdonbehalfby"></a> lk_userqueryvisualizationbase_createdonbehalfby

Same as userqueryvisualization table [lk_userqueryvisualizationbase_createdonbehalfby](userqueryvisualization.md#BKMK_lk_userqueryvisualizationbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userqueryvisualizationbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_usersettings_modifiedonbehalfby"></a> lk_usersettings_modifiedonbehalfby

Same as usersettings table [lk_usersettings_modifiedonbehalfby](usersettings.md#BKMK_lk_usersettings_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_usersettings_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_parent_user"></a> user_parent_user

Same as systemuser table [user_parent_user](systemuser.md#BKMK_user_parent_user) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|parentsystemuserid|
|IsHierarchical|True|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_parent_user|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfiginstance_createdby"></a> lk_appconfiginstance_createdby

Same as appconfiginstance table [lk_appconfiginstance_createdby](appconfiginstance.md#BKMK_lk_appconfiginstance_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfiginstance|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfiginstance_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annualfiscalcalendar_createdonbehalfby"></a> lk_annualfiscalcalendar_createdonbehalfby

Same as annualfiscalcalendar table [lk_annualfiscalcalendar_createdonbehalfby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annualfiscalcalendar|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annualfiscalcalendar_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userformbase_createdonbehalfby"></a> lk_userformbase_createdonbehalfby

Same as userform table [lk_userformbase_createdonbehalfby](userform.md#BKMK_lk_userformbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userformbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fieldsecurityprofile_createdby"></a> lk_fieldsecurityprofile_createdby

Same as fieldsecurityprofile table [lk_fieldsecurityprofile_createdby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fieldsecurityprofile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fieldsecurityprofile_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_asyncoperation_modifiedby"></a> lk_asyncoperation_modifiedby

Same as asyncoperation table [lk_asyncoperation_modifiedby](asyncoperation.md#BKMK_lk_asyncoperation_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_asyncoperation_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_pluginassembly_createdonbehalfby"></a> lk_pluginassembly_createdonbehalfby

Same as pluginassembly table [lk_pluginassembly_createdonbehalfby](pluginassembly.md#BKMK_lk_pluginassembly_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginassembly|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_pluginassembly_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importentitymapping_modifiedby"></a> lk_importentitymapping_modifiedby

Same as importentitymapping table [lk_importentitymapping_modifiedby](importentitymapping.md#BKMK_lk_importentitymapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importentitymapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importentitymapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sdkmessageprocessingstep_createdonbehalfby"></a> lk_sdkmessageprocessingstep_createdonbehalfby

Same as sdkmessageprocessingstep table [lk_sdkmessageprocessingstep_createdonbehalfby](sdkmessageprocessingstep.md#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_sdkmessageprocessingstep_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activitypointer_createdonbehalfby"></a> lk_activitypointer_createdonbehalfby

Same as activitypointer table [lk_activitypointer_createdonbehalfby](activitypointer.md#BKMK_lk_activitypointer_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_activitypointer_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_contact_modifiedonbehalfby"></a> lk_contact_modifiedonbehalfby

Same as contact table [lk_contact_modifiedonbehalfby](contact.md#BKMK_lk_contact_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_contact_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby"></a> lk_savedqueryvisualizationbase_modifiedonbehalfby

Same as savedqueryvisualization table [lk_savedqueryvisualizationbase_modifiedonbehalfby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedqueryvisualization|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_savedqueryvisualizationbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_accountbase_createdonbehalfby"></a> lk_accountbase_createdonbehalfby

Same as account table [lk_accountbase_createdonbehalfby](account.md#BKMK_lk_accountbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_accountbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_modifiedby_sdkmessagefilter"></a> modifiedby_sdkmessagefilter

Same as sdkmessagefilter table [modifiedby_sdkmessagefilter](sdkmessagefilter.md#BKMK_modifiedby_sdkmessagefilter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessagefilter|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|modifiedby_sdkmessagefilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_email_templates"></a> system_user_email_templates

Same as template table [system_user_email_templates](template.md#BKMK_system_user_email_templates) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|system_user_email_templates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ownermapping_modifiedonbehalfby"></a> lk_ownermapping_modifiedonbehalfby

Same as ownermapping table [lk_ownermapping_modifiedonbehalfby](ownermapping.md#BKMK_lk_ownermapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|ownermapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ownermapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_systemuser_modifiedonbehalfby"></a> lk_systemuser_modifiedonbehalfby

Same as systemuser table [lk_systemuser_modifiedonbehalfby](systemuser.md#BKMK_lk_systemuser_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_systemuser_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annualfiscalcalendar_createdby"></a> lk_annualfiscalcalendar_createdby

Same as annualfiscalcalendar table [lk_annualfiscalcalendar_createdby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annualfiscalcalendar|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annualfiscalcalendar_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_email_createdonbehalfby"></a> lk_email_createdonbehalfby

Same as email table [lk_email_createdonbehalfby](email.md#BKMK_lk_email_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_email_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_recurringappointmentmaster_modifiedonbehalfby"></a> lk_recurringappointmentmaster_modifiedonbehalfby

Same as recurringappointmentmaster table [lk_recurringappointmentmaster_modifiedonbehalfby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_recurringappointmentmaster_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonelocalizedname_createdby"></a> lk_timezonelocalizedname_createdby

Same as timezonelocalizedname table [lk_timezonelocalizedname_createdby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonelocalizedname|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonelocalizedname_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bulkdeleteoperationbase_modifiedby"></a> lk_bulkdeleteoperationbase_modifiedby

Same as bulkdeleteoperation table [lk_bulkdeleteoperationbase_modifiedby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperationbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeleteoperation|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_bulkdeleteoperationbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointsitebase_modifiedonbehalfby"></a> lk_sharepointsitebase_modifiedonbehalfby

Same as sharepointsite table [lk_sharepointsitebase_modifiedonbehalfby](sharepointsite.md#BKMK_lk_sharepointsitebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointsitebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ownermapping_modifiedby"></a> lk_ownermapping_modifiedby

Same as ownermapping table [lk_ownermapping_modifiedby](ownermapping.md#BKMK_lk_ownermapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|ownermapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ownermapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointsitebase_createdby"></a> lk_sharepointsitebase_createdby

Same as sharepointsite table [lk_sharepointsitebase_createdby](sharepointsite.md#BKMK_lk_sharepointsitebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointsitebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_actioncardbase_modifiedby"></a> lk_actioncardbase_modifiedby

Same as actioncard table [lk_actioncardbase_modifiedby](actioncard.md#BKMK_lk_actioncardbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_actioncardbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_webresourcebase_createdonbehalfby"></a> lk_webresourcebase_createdonbehalfby

Same as webresource table [lk_webresourcebase_createdonbehalfby](webresource.md#BKMK_lk_webresourcebase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|webresource|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_webresourcebase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionrolebase_modifiedonbehalfby"></a> lk_connectionrolebase_modifiedonbehalfby

Same as connectionrole table [lk_connectionrolebase_modifiedonbehalfby](connectionrole.md#BKMK_lk_connectionrolebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionrole|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_connectionrolebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonelocalizedname_modifiedonbehalfby"></a> lk_timezonelocalizedname_modifiedonbehalfby

Same as timezonelocalizedname table [lk_timezonelocalizedname_modifiedonbehalfby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonelocalizedname|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonelocalizedname_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_transformationmapping_modifiedonbehalfby"></a> lk_transformationmapping_modifiedonbehalfby

Same as transformationmapping table [lk_transformationmapping_modifiedonbehalfby](transformationmapping.md#BKMK_lk_transformationmapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|transformationmapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_transformationmapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_documenttemplatebase_modifiedonbehalfby"></a> lk_documenttemplatebase_modifiedonbehalfby

Same as documenttemplate table [lk_documenttemplatebase_modifiedonbehalfby](documenttemplate.md#BKMK_lk_documenttemplatebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|documenttemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_documenttemplatebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_phonecall"></a> user_phonecall

Same as phonecall table [user_phonecall](phonecall.md#BKMK_user_phonecall) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_phonecall|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceendpointbase_modifiedonbehalfby"></a> lk_serviceendpointbase_modifiedonbehalfby

Same as serviceendpoint table [lk_serviceendpointbase_modifiedonbehalfby](serviceendpoint.md#BKMK_lk_serviceendpointbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceendpoint|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_serviceendpointbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_slabase_createdonbehalfby"></a> lk_slabase_createdonbehalfby

Same as sla table [lk_slabase_createdonbehalfby](sla.md#BKMK_lk_slabase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_slabase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importjobbase_modifiedby"></a> lk_importjobbase_modifiedby

Same as importjob table [lk_importjobbase_modifiedby](importjob.md#BKMK_lk_importjobbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importjob|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importjobbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_MobileOfflineProfileItemAssociation_createdby"></a> lk_MobileOfflineProfileItemAssociation_createdby

Same as mobileofflineprofileitemassociation table [lk_MobileOfflineProfileItemAssociation_createdby](mobileofflineprofileitemassociation.md#BKMK_lk_MobileOfflineProfileItemAssociation_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitemassociation|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_MobileOfflineProfileItemAssociation_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processtriggerbase_createdby"></a> lk_processtriggerbase_createdby

Same as processtrigger table [lk_processtriggerbase_createdby](processtrigger.md#BKMK_lk_processtriggerbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processtrigger|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processtriggerbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonedefinition_createdonbehalfby"></a> lk_timezonedefinition_createdonbehalfby

Same as timezonedefinition table [lk_timezonedefinition_createdonbehalfby](timezonedefinition.md#BKMK_lk_timezonedefinition_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonedefinition|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonedefinition_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticlecomment_modifiedonbehalfby"></a> lk_kbarticlecomment_modifiedonbehalfby

Same as kbarticlecomment table [lk_kbarticlecomment_modifiedonbehalfby](kbarticlecomment.md#BKMK_lk_kbarticlecomment_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticlecomment|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_kbarticlecomment_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonelocalizedname_createdonbehalfby"></a> lk_timezonelocalizedname_createdonbehalfby

Same as timezonelocalizedname table [lk_timezonelocalizedname_createdonbehalfby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonelocalizedname|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonelocalizedname_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_systemuserbase_createdby"></a> lk_systemuserbase_createdby

Same as systemuser table [lk_systemuserbase_createdby](systemuser.md#BKMK_lk_systemuserbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_systemuserbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuser_principalobjectattributeaccess"></a> systemuser_principalobjectattributeaccess

Same as principalobjectattributeaccess table [systemuser_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_systemuser_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|systemuser_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_asyncoperation"></a> system_user_asyncoperation

Same as asyncoperation table [system_user_asyncoperation](asyncoperation.md#BKMK_system_user_asyncoperation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|system_user_asyncoperation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_plugintracelogbase_createdonbehalfby"></a> lk_plugintracelogbase_createdonbehalfby

Same as plugintracelog table [lk_plugintracelogbase_createdonbehalfby](plugintracelog.md#BKMK_lk_plugintracelogbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintracelog|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_plugintracelogbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_teamtemplate_createdby"></a> lk_teamtemplate_createdby

Same as teamtemplate table [lk_teamtemplate_createdby](teamtemplate.md#BKMK_lk_teamtemplate_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|teamtemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_teamtemplate_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_annotationbase_createdonbehalfby"></a> lk_annotationbase_createdonbehalfby

Same as annotation table [lk_annotationbase_createdonbehalfby](annotation.md#BKMK_lk_annotationbase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_annotationbase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fieldsecurityprofile_modifiedonbehalfby"></a> lk_fieldsecurityprofile_modifiedonbehalfby

Same as fieldsecurityprofile table [lk_fieldsecurityprofile_modifiedonbehalfby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fieldsecurityprofile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fieldsecurityprofile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appmodulecomponent_modifiedonbehalfby"></a> lk_appmodulecomponent_modifiedonbehalfby

Same as appmodulecomponent table [lk_appmodulecomponent_modifiedonbehalfby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodulecomponent|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_appmodulecomponent_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_semiannualfiscalcalendar_createdonbehalfby"></a> lk_semiannualfiscalcalendar_createdonbehalfby

Same as semiannualfiscalcalendar table [lk_semiannualfiscalcalendar_createdonbehalfby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|semiannualfiscalcalendar|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_semiannualfiscalcalendar_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_userquery_modifiedonbehalfby"></a> lk_userquery_modifiedonbehalfby

Same as userquery table [lk_userquery_modifiedonbehalfby](userquery.md#BKMK_lk_userquery_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_userquery_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunitnewsarticlebase_createdby"></a> lk_businessunitnewsarticlebase_createdby

Same as businessunitnewsarticle table [lk_businessunitnewsarticlebase_createdby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticlebase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunitnewsarticle|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_businessunitnewsarticlebase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuser_connections2"></a> systemuser_connections2

Same as connection table [systemuser_connections2](connection.md#BKMK_systemuser_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_task_createdonbehalfby"></a> lk_task_createdonbehalfby

Same as task table [lk_task_createdonbehalfby](task.md#BKMK_lk_task_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_task_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_contactbase_modifiedby"></a> lk_contactbase_modifiedby

Same as contact table [lk_contactbase_modifiedby](contact.md#BKMK_lk_contactbase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_contactbase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_letter_createdonbehalfby"></a> lk_letter_createdonbehalfby

Same as letter table [lk_letter_createdonbehalfby](letter.md#BKMK_lk_letter_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_letter_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customcontrolresource_createdby"></a> lk_customcontrolresource_createdby

Same as customcontrolresource table [lk_customcontrolresource_createdby](customcontrolresource.md#BKMK_lk_customcontrolresource_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customcontrolresource|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customcontrolresource_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_socialactivitybase_modifiedonbehalfby"></a> lk_socialactivitybase_modifiedonbehalfby

Same as socialactivity table [lk_socialactivitybase_modifiedonbehalfby](socialactivity.md#BKMK_lk_socialactivitybase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_socialactivitybase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_socialactivitybase_createdonbehalfby"></a> lk_socialactivitybase_createdonbehalfby

Same as socialactivity table [lk_socialactivitybase_createdonbehalfby](socialactivity.md#BKMK_lk_socialactivitybase_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_socialactivitybase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_importfilebase_modifiedonbehalfby"></a> lk_importfilebase_modifiedonbehalfby

Same as importfile table [lk_importfilebase_modifiedonbehalfby](importfile.md#BKMK_lk_importfilebase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_importfilebase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_fieldsecurityprofile_modifiedby"></a> lk_fieldsecurityprofile_modifiedby

Same as fieldsecurityprofile table [lk_fieldsecurityprofile_modifiedby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fieldsecurityprofile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_fieldsecurityprofile_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_newprocess_createdonbehalfby"></a> lk_newprocess_createdonbehalfby

Same as newprocess table [lk_newprocess_createdonbehalfby](newprocess.md#BKMK_lk_newprocess_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_newprocess_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appconfig_createdby"></a> lk_appconfig_createdby

Same as appconfig table [lk_appconfig_createdby](appconfig.md#BKMK_lk_appconfig_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfig|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_appconfig_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_businessunitbase_createdby"></a> lk_businessunitbase_createdby

Same as businessunit table [lk_businessunitbase_createdby](businessunit.md#BKMK_lk_businessunitbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_businessunitbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_monthlyfiscalcalendar_createdonbehalfby"></a> lk_monthlyfiscalcalendar_createdonbehalfby

Same as monthlyfiscalcalendar table [lk_monthlyfiscalcalendar_createdonbehalfby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|monthlyfiscalcalendar|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_monthlyfiscalcalendar_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby"></a> lk_sharepointdocumentlocationbase_modifiedonbehalfby

Same as sharepointdocumentlocation table [lk_sharepointdocumentlocationbase_modifiedonbehalfby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_sharepointdocumentlocationbase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_syncerrorbase_createdby"></a> lk_syncerrorbase_createdby

Same as syncerror table [lk_syncerrorbase_createdby](syncerror.md#BKMK_lk_syncerrorbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_syncerrorbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_createdby_sdkmessagefilter"></a> createdby_sdkmessagefilter

Same as sdkmessagefilter table [createdby_sdkmessagefilter](sdkmessagefilter.md#BKMK_createdby_sdkmessagefilter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessagefilter|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|createdby_sdkmessagefilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_kbarticlebase_modifiedby"></a> lk_kbarticlebase_modifiedby

Same as kbarticle table [lk_kbarticlebase_modifiedby](kbarticle.md#BKMK_lk_kbarticlebase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticle|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_kbarticlebase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_ownermapping_createdby"></a> lk_ownermapping_createdby

Same as ownermapping table [lk_ownermapping_createdby](ownermapping.md#BKMK_lk_ownermapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|ownermapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_ownermapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemUser_SyncErrors"></a> SystemUser_SyncErrors

Same as syncerror table [SystemUser_SyncErrors](syncerror.md#BKMK_SystemUser_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SystemUser_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_lk_duplicateruleconditionbase_createdby"></a> lk_duplicateruleconditionbase_createdby

Same as duplicaterulecondition table [lk_duplicateruleconditionbase_createdby](duplicaterulecondition.md#BKMK_lk_duplicateruleconditionbase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterulecondition|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_duplicateruleconditionbase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_callbackregistration_modifiedonbehalfby"></a> lk_callbackregistration_modifiedonbehalfby

Same as callbackregistration table [lk_callbackregistration_modifiedonbehalfby](callbackregistration.md#BKMK_lk_callbackregistration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|callbackregistration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_callbackregistration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_callbackregistration_modifiedby"></a> lk_callbackregistration_modifiedby

Same as callbackregistration table [lk_callbackregistration_modifiedby](callbackregistration.md#BKMK_lk_callbackregistration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|callbackregistration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_callbackregistration_modifiedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_callbackregistration_createdonbehalfby"></a> lk_callbackregistration_createdonbehalfby

Same as callbackregistration table [lk_callbackregistration_createdonbehalfby](callbackregistration.md#BKMK_lk_callbackregistration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|callbackregistration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_callbackregistration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_callbackregistration_createdby"></a> lk_callbackregistration_createdby

Same as callbackregistration table [lk_callbackregistration_createdby](callbackregistration.md#BKMK_lk_callbackregistration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|callbackregistration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_callbackregistration_createdby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentattributeconfiguration_createdby"></a> lk_solutioncomponentattributeconfiguration_createdby

**Added by**: Active Solution Solution

Same as solutioncomponentattributeconfiguration table [lk_solutioncomponentattributeconfiguration_createdby](solutioncomponentattributeconfiguration.md#BKMK_lk_solutioncomponentattributeconfiguration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentattributeconfiguration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentattributeconfiguration_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentattributeconfiguration_createdonbehalfby"></a> lk_solutioncomponentattributeconfiguration_createdonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentattributeconfiguration table [lk_solutioncomponentattributeconfiguration_createdonbehalfby](solutioncomponentattributeconfiguration.md#BKMK_lk_solutioncomponentattributeconfiguration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentattributeconfiguration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentattributeconfiguration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentattributeconfiguration_modifiedby"></a> lk_solutioncomponentattributeconfiguration_modifiedby

**Added by**: Active Solution Solution

Same as solutioncomponentattributeconfiguration table [lk_solutioncomponentattributeconfiguration_modifiedby](solutioncomponentattributeconfiguration.md#BKMK_lk_solutioncomponentattributeconfiguration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentattributeconfiguration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentattributeconfiguration_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentattributeconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentattributeconfiguration_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentattributeconfiguration table [lk_solutioncomponentattributeconfiguration_modifiedonbehalfby](solutioncomponentattributeconfiguration.md#BKMK_lk_solutioncomponentattributeconfiguration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentattributeconfiguration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentattributeconfiguration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentbatchconfiguration_createdby"></a> lk_solutioncomponentbatchconfiguration_createdby

**Added by**: Active Solution Solution

Same as solutioncomponentbatchconfiguration table [lk_solutioncomponentbatchconfiguration_createdby](solutioncomponentbatchconfiguration.md#BKMK_lk_solutioncomponentbatchconfiguration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentbatchconfiguration_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentbatchconfiguration_createdonbehalfby"></a> lk_solutioncomponentbatchconfiguration_createdonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentbatchconfiguration table [lk_solutioncomponentbatchconfiguration_createdonbehalfby](solutioncomponentbatchconfiguration.md#BKMK_lk_solutioncomponentbatchconfiguration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentbatchconfiguration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentbatchconfiguration_modifiedby"></a> lk_solutioncomponentbatchconfiguration_modifiedby

**Added by**: Active Solution Solution

Same as solutioncomponentbatchconfiguration table [lk_solutioncomponentbatchconfiguration_modifiedby](solutioncomponentbatchconfiguration.md#BKMK_lk_solutioncomponentbatchconfiguration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentbatchconfiguration_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentbatchconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentbatchconfiguration_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentbatchconfiguration table [lk_solutioncomponentbatchconfiguration_modifiedonbehalfby](solutioncomponentbatchconfiguration.md#BKMK_lk_solutioncomponentbatchconfiguration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentbatchconfiguration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_solutioncomponentbatchconfiguration"></a> user_solutioncomponentbatchconfiguration

**Added by**: Active Solution Solution

Same as solutioncomponentbatchconfiguration table [user_solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md#BKMK_user_solutioncomponentbatchconfiguration) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_solutioncomponentbatchconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentconfiguration_createdby"></a> lk_solutioncomponentconfiguration_createdby

**Added by**: Active Solution Solution

Same as solutioncomponentconfiguration table [lk_solutioncomponentconfiguration_createdby](solutioncomponentconfiguration.md#BKMK_lk_solutioncomponentconfiguration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentconfiguration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentconfiguration_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentconfiguration_createdonbehalfby"></a> lk_solutioncomponentconfiguration_createdonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentconfiguration table [lk_solutioncomponentconfiguration_createdonbehalfby](solutioncomponentconfiguration.md#BKMK_lk_solutioncomponentconfiguration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentconfiguration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentconfiguration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentconfiguration_modifiedby"></a> lk_solutioncomponentconfiguration_modifiedby

**Added by**: Active Solution Solution

Same as solutioncomponentconfiguration table [lk_solutioncomponentconfiguration_modifiedby](solutioncomponentconfiguration.md#BKMK_lk_solutioncomponentconfiguration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentconfiguration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentconfiguration_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentconfiguration_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentconfiguration table [lk_solutioncomponentconfiguration_modifiedonbehalfby](solutioncomponentconfiguration.md#BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentconfiguration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentconfiguration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_createdby"></a> lk_solutioncomponentrelationshipconfiguration_createdby

**Added by**: Active Solution Solution

Same as solutioncomponentrelationshipconfiguration table [lk_solutioncomponentrelationshipconfiguration_createdby](solutioncomponentrelationshipconfiguration.md#BKMK_lk_solutioncomponentrelationshipconfiguration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentrelationshipconfiguration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentrelationshipconfiguration_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby"></a> lk_solutioncomponentrelationshipconfiguration_createdonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentrelationshipconfiguration table [lk_solutioncomponentrelationshipconfiguration_createdonbehalfby](solutioncomponentrelationshipconfiguration.md#BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentrelationshipconfiguration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentrelationshipconfiguration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby"></a> lk_solutioncomponentrelationshipconfiguration_modifiedby

**Added by**: Active Solution Solution

Same as solutioncomponentrelationshipconfiguration table [lk_solutioncomponentrelationshipconfiguration_modifiedby](solutioncomponentrelationshipconfiguration.md#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentrelationshipconfiguration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentrelationshipconfiguration_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as solutioncomponentrelationshipconfiguration table [lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby](solutioncomponentrelationshipconfiguration.md#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentrelationshipconfiguration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_package_createdby"></a> lk_package_createdby

**Added by**: Active Solution Solution

Same as package table [lk_package_createdby](package.md#BKMK_lk_package_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|package|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_package_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_package_createdonbehalfby"></a> lk_package_createdonbehalfby

**Added by**: Active Solution Solution

Same as package table [lk_package_createdonbehalfby](package.md#BKMK_lk_package_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|package|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_package_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_package_modifiedby"></a> lk_package_modifiedby

**Added by**: Active Solution Solution

Same as package table [lk_package_modifiedby](package.md#BKMK_lk_package_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|package|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_package_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_package_modifiedonbehalfby"></a> lk_package_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as package table [lk_package_modifiedonbehalfby](package.md#BKMK_lk_package_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|package|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_package_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_stagesolutionupload_createdby"></a> lk_stagesolutionupload_createdby

**Added by**: Active Solution Solution

Same as stagesolutionupload table [lk_stagesolutionupload_createdby](stagesolutionupload.md#BKMK_lk_stagesolutionupload_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_stagesolutionupload_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_stagesolutionupload_createdonbehalfby"></a> lk_stagesolutionupload_createdonbehalfby

**Added by**: Active Solution Solution

Same as stagesolutionupload table [lk_stagesolutionupload_createdonbehalfby](stagesolutionupload.md#BKMK_lk_stagesolutionupload_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_stagesolutionupload_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_stagesolutionupload_modifiedby"></a> lk_stagesolutionupload_modifiedby

**Added by**: Active Solution Solution

Same as stagesolutionupload table [lk_stagesolutionupload_modifiedby](stagesolutionupload.md#BKMK_lk_stagesolutionupload_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_stagesolutionupload_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_stagesolutionupload_modifiedonbehalfby"></a> lk_stagesolutionupload_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as stagesolutionupload table [lk_stagesolutionupload_modifiedonbehalfby](stagesolutionupload.md#BKMK_lk_stagesolutionupload_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_stagesolutionupload_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_stagesolutionupload"></a> user_stagesolutionupload

**Added by**: Active Solution Solution

Same as stagesolutionupload table [user_stagesolutionupload](stagesolutionupload.md#BKMK_user_stagesolutionupload) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_stagesolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_exportsolutionupload_createdby"></a> lk_exportsolutionupload_createdby

**Added by**: Active Solution Solution

Same as exportsolutionupload table [lk_exportsolutionupload_createdby](exportsolutionupload.md#BKMK_lk_exportsolutionupload_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_exportsolutionupload_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_exportsolutionupload_createdonbehalfby"></a> lk_exportsolutionupload_createdonbehalfby

**Added by**: Active Solution Solution

Same as exportsolutionupload table [lk_exportsolutionupload_createdonbehalfby](exportsolutionupload.md#BKMK_lk_exportsolutionupload_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_exportsolutionupload_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_exportsolutionupload_modifiedby"></a> lk_exportsolutionupload_modifiedby

**Added by**: Active Solution Solution

Same as exportsolutionupload table [lk_exportsolutionupload_modifiedby](exportsolutionupload.md#BKMK_lk_exportsolutionupload_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_exportsolutionupload_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_exportsolutionupload_modifiedonbehalfby"></a> lk_exportsolutionupload_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as exportsolutionupload table [lk_exportsolutionupload_modifiedonbehalfby](exportsolutionupload.md#BKMK_lk_exportsolutionupload_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_exportsolutionupload_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_exportsolutionupload"></a> user_exportsolutionupload

**Added by**: Active Solution Solution

Same as exportsolutionupload table [user_exportsolutionupload](exportsolutionupload.md#BKMK_user_exportsolutionupload) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_exportsolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_featurecontrolsetting_createdby"></a> lk_featurecontrolsetting_createdby

**Added by**: Active Solution Solution

Same as featurecontrolsetting table [lk_featurecontrolsetting_createdby](featurecontrolsetting.md#BKMK_lk_featurecontrolsetting_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_featurecontrolsetting_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_featurecontrolsetting_createdonbehalfby"></a> lk_featurecontrolsetting_createdonbehalfby

**Added by**: Active Solution Solution

Same as featurecontrolsetting table [lk_featurecontrolsetting_createdonbehalfby](featurecontrolsetting.md#BKMK_lk_featurecontrolsetting_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_featurecontrolsetting_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_featurecontrolsetting_modifiedby"></a> lk_featurecontrolsetting_modifiedby

**Added by**: Active Solution Solution

Same as featurecontrolsetting table [lk_featurecontrolsetting_modifiedby](featurecontrolsetting.md#BKMK_lk_featurecontrolsetting_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_featurecontrolsetting_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_featurecontrolsetting_modifiedonbehalfby"></a> lk_featurecontrolsetting_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as featurecontrolsetting table [lk_featurecontrolsetting_modifiedonbehalfby](featurecontrolsetting.md#BKMK_lk_featurecontrolsetting_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_featurecontrolsetting_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_featurecontrolsetting"></a> user_featurecontrolsetting

**Added by**: Active Solution Solution

Same as featurecontrolsetting table [user_featurecontrolsetting](featurecontrolsetting.md#BKMK_user_featurecontrolsetting) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_featurecontrolsetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalog_createdby"></a> lk_catalog_createdby

**Added by**: Active Solution Solution

Same as catalog table [lk_catalog_createdby](catalog.md#BKMK_lk_catalog_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalog|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_catalog_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalog_createdonbehalfby"></a> lk_catalog_createdonbehalfby

**Added by**: Active Solution Solution

Same as catalog table [lk_catalog_createdonbehalfby](catalog.md#BKMK_lk_catalog_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalog|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_catalog_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalog_modifiedby"></a> lk_catalog_modifiedby

**Added by**: Active Solution Solution

Same as catalog table [lk_catalog_modifiedby](catalog.md#BKMK_lk_catalog_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalog|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_catalog_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalog_modifiedonbehalfby"></a> lk_catalog_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as catalog table [lk_catalog_modifiedonbehalfby](catalog.md#BKMK_lk_catalog_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalog|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_catalog_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalogassignment_createdby"></a> lk_catalogassignment_createdby

**Added by**: Active Solution Solution

Same as catalogassignment table [lk_catalogassignment_createdby](catalogassignment.md#BKMK_lk_catalogassignment_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalogassignment|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_catalogassignment_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalogassignment_createdonbehalfby"></a> lk_catalogassignment_createdonbehalfby

**Added by**: Active Solution Solution

Same as catalogassignment table [lk_catalogassignment_createdonbehalfby](catalogassignment.md#BKMK_lk_catalogassignment_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalogassignment|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_catalogassignment_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalogassignment_modifiedby"></a> lk_catalogassignment_modifiedby

**Added by**: Active Solution Solution

Same as catalogassignment table [lk_catalogassignment_modifiedby](catalogassignment.md#BKMK_lk_catalogassignment_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalogassignment|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_catalogassignment_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_catalogassignment_modifiedonbehalfby"></a> lk_catalogassignment_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as catalogassignment table [lk_catalogassignment_modifiedonbehalfby](catalogassignment.md#BKMK_lk_catalogassignment_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalogassignment|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_catalogassignment_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapi_createdby"></a> lk_customapi_createdby

**Added by**: Active Solution Solution

Same as customapi table [lk_customapi_createdby](customapi.md#BKMK_lk_customapi_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customapi_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapi_createdonbehalfby"></a> lk_customapi_createdonbehalfby

**Added by**: Active Solution Solution

Same as customapi table [lk_customapi_createdonbehalfby](customapi.md#BKMK_lk_customapi_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customapi_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapi_modifiedby"></a> lk_customapi_modifiedby

**Added by**: Active Solution Solution

Same as customapi table [lk_customapi_modifiedby](customapi.md#BKMK_lk_customapi_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customapi_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapi_modifiedonbehalfby"></a> lk_customapi_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as customapi table [lk_customapi_modifiedonbehalfby](customapi.md#BKMK_lk_customapi_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customapi_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_customapi"></a> user_customapi

**Added by**: Active Solution Solution

Same as customapi table [user_customapi](customapi.md#BKMK_user_customapi) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_customapi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapirequestparameter_createdby"></a> lk_customapirequestparameter_createdby

**Added by**: Active Solution Solution

Same as customapirequestparameter table [lk_customapirequestparameter_createdby](customapirequestparameter.md#BKMK_lk_customapirequestparameter_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customapirequestparameter_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapirequestparameter_createdonbehalfby"></a> lk_customapirequestparameter_createdonbehalfby

**Added by**: Active Solution Solution

Same as customapirequestparameter table [lk_customapirequestparameter_createdonbehalfby](customapirequestparameter.md#BKMK_lk_customapirequestparameter_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customapirequestparameter_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapirequestparameter_modifiedby"></a> lk_customapirequestparameter_modifiedby

**Added by**: Active Solution Solution

Same as customapirequestparameter table [lk_customapirequestparameter_modifiedby](customapirequestparameter.md#BKMK_lk_customapirequestparameter_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customapirequestparameter_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapirequestparameter_modifiedonbehalfby"></a> lk_customapirequestparameter_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as customapirequestparameter table [lk_customapirequestparameter_modifiedonbehalfby](customapirequestparameter.md#BKMK_lk_customapirequestparameter_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customapirequestparameter_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_customapirequestparameter"></a> user_customapirequestparameter

**Added by**: Active Solution Solution

Same as customapirequestparameter table [user_customapirequestparameter](customapirequestparameter.md#BKMK_user_customapirequestparameter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_customapirequestparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapiresponseproperty_createdby"></a> lk_customapiresponseproperty_createdby

**Added by**: Active Solution Solution

Same as customapiresponseproperty table [lk_customapiresponseproperty_createdby](customapiresponseproperty.md#BKMK_lk_customapiresponseproperty_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customapiresponseproperty_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapiresponseproperty_createdonbehalfby"></a> lk_customapiresponseproperty_createdonbehalfby

**Added by**: Active Solution Solution

Same as customapiresponseproperty table [lk_customapiresponseproperty_createdonbehalfby](customapiresponseproperty.md#BKMK_lk_customapiresponseproperty_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customapiresponseproperty_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapiresponseproperty_modifiedby"></a> lk_customapiresponseproperty_modifiedby

**Added by**: Active Solution Solution

Same as customapiresponseproperty table [lk_customapiresponseproperty_modifiedby](customapiresponseproperty.md#BKMK_lk_customapiresponseproperty_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_customapiresponseproperty_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_customapiresponseproperty_modifiedonbehalfby"></a> lk_customapiresponseproperty_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as customapiresponseproperty table [lk_customapiresponseproperty_modifiedonbehalfby](customapiresponseproperty.md#BKMK_lk_customapiresponseproperty_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_customapiresponseproperty_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_customapiresponseproperty"></a> user_customapiresponseproperty

**Added by**: Active Solution Solution

Same as customapiresponseproperty table [user_customapiresponseproperty](customapiresponseproperty.md#BKMK_user_customapiresponseproperty) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_customapiresponseproperty|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolder_createdby"></a> lk_datalakefolder_createdby

**Added by**: Active Solution Solution

Same as datalakefolder table [lk_datalakefolder_createdby](datalakefolder.md#BKMK_lk_datalakefolder_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolder_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolder_createdonbehalfby"></a> lk_datalakefolder_createdonbehalfby

**Added by**: Active Solution Solution

Same as datalakefolder table [lk_datalakefolder_createdonbehalfby](datalakefolder.md#BKMK_lk_datalakefolder_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolder_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolder_modifiedby"></a> lk_datalakefolder_modifiedby

**Added by**: Active Solution Solution

Same as datalakefolder table [lk_datalakefolder_modifiedby](datalakefolder.md#BKMK_lk_datalakefolder_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolder_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolder_modifiedonbehalfby"></a> lk_datalakefolder_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as datalakefolder table [lk_datalakefolder_modifiedonbehalfby](datalakefolder.md#BKMK_lk_datalakefolder_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolder_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_datalakefolder"></a> user_datalakefolder

**Added by**: Active Solution Solution

Same as datalakefolder table [user_datalakefolder](datalakefolder.md#BKMK_user_datalakefolder) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_datalakefolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolderpermission_createdby"></a> lk_datalakefolderpermission_createdby

**Added by**: Active Solution Solution

Same as datalakefolderpermission table [lk_datalakefolderpermission_createdby](datalakefolderpermission.md#BKMK_lk_datalakefolderpermission_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolderpermission_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolderpermission_createdonbehalfby"></a> lk_datalakefolderpermission_createdonbehalfby

**Added by**: Active Solution Solution

Same as datalakefolderpermission table [lk_datalakefolderpermission_createdonbehalfby](datalakefolderpermission.md#BKMK_lk_datalakefolderpermission_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolderpermission_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolderpermission_modifiedby"></a> lk_datalakefolderpermission_modifiedby

**Added by**: Active Solution Solution

Same as datalakefolderpermission table [lk_datalakefolderpermission_modifiedby](datalakefolderpermission.md#BKMK_lk_datalakefolderpermission_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolderpermission_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakefolderpermission_modifiedonbehalfby"></a> lk_datalakefolderpermission_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as datalakefolderpermission table [lk_datalakefolderpermission_modifiedonbehalfby](datalakefolderpermission.md#BKMK_lk_datalakefolderpermission_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakefolderpermission_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_datalakefolderpermission"></a> user_datalakefolderpermission

**Added by**: Active Solution Solution

Same as datalakefolderpermission table [user_datalakefolderpermission](datalakefolderpermission.md#BKMK_user_datalakefolderpermission) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_datalakefolderpermission|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspace_createdby"></a> lk_datalakeworkspace_createdby

**Added by**: Active Solution Solution

Same as datalakeworkspace table [lk_datalakeworkspace_createdby](datalakeworkspace.md#BKMK_lk_datalakeworkspace_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspace|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspace_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspace_createdonbehalfby"></a> lk_datalakeworkspace_createdonbehalfby

**Added by**: Active Solution Solution

Same as datalakeworkspace table [lk_datalakeworkspace_createdonbehalfby](datalakeworkspace.md#BKMK_lk_datalakeworkspace_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspace|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspace_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspace_modifiedby"></a> lk_datalakeworkspace_modifiedby

**Added by**: Active Solution Solution

Same as datalakeworkspace table [lk_datalakeworkspace_modifiedby](datalakeworkspace.md#BKMK_lk_datalakeworkspace_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspace|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspace_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspace_modifiedonbehalfby"></a> lk_datalakeworkspace_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as datalakeworkspace table [lk_datalakeworkspace_modifiedonbehalfby](datalakeworkspace.md#BKMK_lk_datalakeworkspace_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspace|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspace_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspacepermission_createdby"></a> lk_datalakeworkspacepermission_createdby

**Added by**: Active Solution Solution

Same as datalakeworkspacepermission table [lk_datalakeworkspacepermission_createdby](datalakeworkspacepermission.md#BKMK_lk_datalakeworkspacepermission_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspacepermission|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspacepermission_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspacepermission_createdonbehalfby"></a> lk_datalakeworkspacepermission_createdonbehalfby

**Added by**: Active Solution Solution

Same as datalakeworkspacepermission table [lk_datalakeworkspacepermission_createdonbehalfby](datalakeworkspacepermission.md#BKMK_lk_datalakeworkspacepermission_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspacepermission|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspacepermission_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspacepermission_modifiedby"></a> lk_datalakeworkspacepermission_modifiedby

**Added by**: Active Solution Solution

Same as datalakeworkspacepermission table [lk_datalakeworkspacepermission_modifiedby](datalakeworkspacepermission.md#BKMK_lk_datalakeworkspacepermission_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspacepermission|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspacepermission_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_datalakeworkspacepermission_modifiedonbehalfby"></a> lk_datalakeworkspacepermission_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as datalakeworkspacepermission table [lk_datalakeworkspacepermission_modifiedonbehalfby](datalakeworkspacepermission.md#BKMK_lk_datalakeworkspacepermission_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakeworkspacepermission|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_datalakeworkspacepermission_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_dataflow_createdby"></a> lk_msdyn_dataflow_createdby

**Added by**: Active Solution Solution

Same as msdyn_dataflow table [lk_msdyn_dataflow_createdby](msdyn_dataflow.md#BKMK_lk_msdyn_dataflow_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_dataflow_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_dataflow_createdonbehalfby"></a> lk_msdyn_dataflow_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_dataflow table [lk_msdyn_dataflow_createdonbehalfby](msdyn_dataflow.md#BKMK_lk_msdyn_dataflow_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_dataflow_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_dataflow_modifiedby"></a> lk_msdyn_dataflow_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_dataflow table [lk_msdyn_dataflow_modifiedby](msdyn_dataflow.md#BKMK_lk_msdyn_dataflow_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_dataflow_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_dataflow_modifiedonbehalfby"></a> lk_msdyn_dataflow_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_dataflow table [lk_msdyn_dataflow_modifiedonbehalfby](msdyn_dataflow.md#BKMK_lk_msdyn_dataflow_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_dataflow_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_dataflow"></a> user_msdyn_dataflow

**Added by**: Active Solution Solution

Same as msdyn_dataflow table [user_msdyn_dataflow](msdyn_dataflow.md#BKMK_user_msdyn_dataflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_dataflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplan_createdby"></a> lk_serviceplan_createdby

**Added by**: Active Solution Solution

Same as serviceplan table [lk_serviceplan_createdby](serviceplan.md#BKMK_lk_serviceplan_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplan|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplan_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplan_createdonbehalfby"></a> lk_serviceplan_createdonbehalfby

**Added by**: Active Solution Solution

Same as serviceplan table [lk_serviceplan_createdonbehalfby](serviceplan.md#BKMK_lk_serviceplan_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplan|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplan_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplan_modifiedby"></a> lk_serviceplan_modifiedby

**Added by**: Active Solution Solution

Same as serviceplan table [lk_serviceplan_modifiedby](serviceplan.md#BKMK_lk_serviceplan_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplan|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplan_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplan_modifiedonbehalfby"></a> lk_serviceplan_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as serviceplan table [lk_serviceplan_modifiedonbehalfby](serviceplan.md#BKMK_lk_serviceplan_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplan|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplan_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplanmapping_createdby"></a> lk_serviceplanmapping_createdby

**Added by**: Active Solution Solution

Same as serviceplanmapping table [lk_serviceplanmapping_createdby](serviceplanmapping.md#BKMK_lk_serviceplanmapping_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplanmapping|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplanmapping_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplanmapping_createdonbehalfby"></a> lk_serviceplanmapping_createdonbehalfby

**Added by**: Active Solution Solution

Same as serviceplanmapping table [lk_serviceplanmapping_createdonbehalfby](serviceplanmapping.md#BKMK_lk_serviceplanmapping_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplanmapping|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplanmapping_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplanmapping_modifiedby"></a> lk_serviceplanmapping_modifiedby

**Added by**: Active Solution Solution

Same as serviceplanmapping table [lk_serviceplanmapping_modifiedby](serviceplanmapping.md#BKMK_lk_serviceplanmapping_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplanmapping|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplanmapping_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_serviceplanmapping_modifiedonbehalfby"></a> lk_serviceplanmapping_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as serviceplanmapping table [lk_serviceplanmapping_modifiedonbehalfby](serviceplanmapping.md#BKMK_lk_serviceplanmapping_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|serviceplanmapping|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_serviceplanmapping_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_applicationuser_createdby"></a> lk_applicationuser_createdby

**Added by**: Active Solution Solution

Same as applicationuser table [lk_applicationuser_createdby](applicationuser.md#BKMK_lk_applicationuser_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|applicationuser|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_applicationuser_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_applicationuser_createdonbehalfby"></a> lk_applicationuser_createdonbehalfby

**Added by**: Active Solution Solution

Same as applicationuser table [lk_applicationuser_createdonbehalfby](applicationuser.md#BKMK_lk_applicationuser_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|applicationuser|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_applicationuser_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_applicationuser_modifiedby"></a> lk_applicationuser_modifiedby

**Added by**: Active Solution Solution

Same as applicationuser table [lk_applicationuser_modifiedby](applicationuser.md#BKMK_lk_applicationuser_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|applicationuser|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_applicationuser_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_applicationuser_modifiedonbehalfby"></a> lk_applicationuser_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as applicationuser table [lk_applicationuser_modifiedonbehalfby](applicationuser.md#BKMK_lk_applicationuser_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|applicationuser|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_applicationuser_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connector_createdby"></a> lk_connector_createdby

**Added by**: Active Solution Solution

Same as connector table [lk_connector_createdby](connector.md#BKMK_lk_connector_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connector_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connector_createdonbehalfby"></a> lk_connector_createdonbehalfby

**Added by**: Active Solution Solution

Same as connector table [lk_connector_createdonbehalfby](connector.md#BKMK_lk_connector_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connector_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connector_modifiedby"></a> lk_connector_modifiedby

**Added by**: Active Solution Solution

Same as connector table [lk_connector_modifiedby](connector.md#BKMK_lk_connector_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connector_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connector_modifiedonbehalfby"></a> lk_connector_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as connector table [lk_connector_modifiedonbehalfby](connector.md#BKMK_lk_connector_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connector_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_connector"></a> user_connector

**Added by**: Active Solution Solution

Same as connector table [user_connector](connector.md#BKMK_user_connector) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_connector|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariabledefinition_createdby"></a> lk_environmentvariabledefinition_createdby

**Added by**: Active Solution Solution

Same as environmentvariabledefinition table [lk_environmentvariabledefinition_createdby](environmentvariabledefinition.md#BKMK_lk_environmentvariabledefinition_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_environmentvariabledefinition_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariabledefinition_createdonbehalfby"></a> lk_environmentvariabledefinition_createdonbehalfby

**Added by**: Active Solution Solution

Same as environmentvariabledefinition table [lk_environmentvariabledefinition_createdonbehalfby](environmentvariabledefinition.md#BKMK_lk_environmentvariabledefinition_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_environmentvariabledefinition_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariabledefinition_modifiedby"></a> lk_environmentvariabledefinition_modifiedby

**Added by**: Active Solution Solution

Same as environmentvariabledefinition table [lk_environmentvariabledefinition_modifiedby](environmentvariabledefinition.md#BKMK_lk_environmentvariabledefinition_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_environmentvariabledefinition_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariabledefinition_modifiedonbehalfby"></a> lk_environmentvariabledefinition_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as environmentvariabledefinition table [lk_environmentvariabledefinition_modifiedonbehalfby](environmentvariabledefinition.md#BKMK_lk_environmentvariabledefinition_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_environmentvariabledefinition_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_environmentvariabledefinition"></a> user_environmentvariabledefinition

**Added by**: Active Solution Solution

Same as environmentvariabledefinition table [user_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_user_environmentvariabledefinition) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_environmentvariabledefinition|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariablevalue_createdby"></a> lk_environmentvariablevalue_createdby

**Added by**: Active Solution Solution

Same as environmentvariablevalue table [lk_environmentvariablevalue_createdby](environmentvariablevalue.md#BKMK_lk_environmentvariablevalue_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_environmentvariablevalue_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariablevalue_createdonbehalfby"></a> lk_environmentvariablevalue_createdonbehalfby

**Added by**: Active Solution Solution

Same as environmentvariablevalue table [lk_environmentvariablevalue_createdonbehalfby](environmentvariablevalue.md#BKMK_lk_environmentvariablevalue_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_environmentvariablevalue_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariablevalue_modifiedby"></a> lk_environmentvariablevalue_modifiedby

**Added by**: Active Solution Solution

Same as environmentvariablevalue table [lk_environmentvariablevalue_modifiedby](environmentvariablevalue.md#BKMK_lk_environmentvariablevalue_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_environmentvariablevalue_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_environmentvariablevalue_modifiedonbehalfby"></a> lk_environmentvariablevalue_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as environmentvariablevalue table [lk_environmentvariablevalue_modifiedonbehalfby](environmentvariablevalue.md#BKMK_lk_environmentvariablevalue_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_environmentvariablevalue_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_environmentvariablevalue"></a> user_environmentvariablevalue

**Added by**: Active Solution Solution

Same as environmentvariablevalue table [user_environmentvariablevalue](environmentvariablevalue.md#BKMK_user_environmentvariablevalue) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_environmentvariablevalue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachine_createdby"></a> lk_flowmachine_createdby

**Added by**: Active Solution Solution

Same as flowmachine table [lk_flowmachine_createdby](flowmachine.md#BKMK_lk_flowmachine_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_flowmachine_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachine_createdonbehalfby"></a> lk_flowmachine_createdonbehalfby

**Added by**: Active Solution Solution

Same as flowmachine table [lk_flowmachine_createdonbehalfby](flowmachine.md#BKMK_lk_flowmachine_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_flowmachine_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachine_modifiedby"></a> lk_flowmachine_modifiedby

**Added by**: Active Solution Solution

Same as flowmachine table [lk_flowmachine_modifiedby](flowmachine.md#BKMK_lk_flowmachine_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_flowmachine_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachine_modifiedonbehalfby"></a> lk_flowmachine_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as flowmachine table [lk_flowmachine_modifiedonbehalfby](flowmachine.md#BKMK_lk_flowmachine_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_flowmachine_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_flowmachine"></a> user_flowmachine

**Added by**: Active Solution Solution

Same as flowmachine table [user_flowmachine](flowmachine.md#BKMK_user_flowmachine) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_flowmachine|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachinegroup_createdby"></a> lk_flowmachinegroup_createdby

**Added by**: Active Solution Solution

Same as flowmachinegroup table [lk_flowmachinegroup_createdby](flowmachinegroup.md#BKMK_lk_flowmachinegroup_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_flowmachinegroup_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachinegroup_createdonbehalfby"></a> lk_flowmachinegroup_createdonbehalfby

**Added by**: Active Solution Solution

Same as flowmachinegroup table [lk_flowmachinegroup_createdonbehalfby](flowmachinegroup.md#BKMK_lk_flowmachinegroup_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_flowmachinegroup_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachinegroup_modifiedby"></a> lk_flowmachinegroup_modifiedby

**Added by**: Active Solution Solution

Same as flowmachinegroup table [lk_flowmachinegroup_modifiedby](flowmachinegroup.md#BKMK_lk_flowmachinegroup_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_flowmachinegroup_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowmachinegroup_modifiedonbehalfby"></a> lk_flowmachinegroup_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as flowmachinegroup table [lk_flowmachinegroup_modifiedonbehalfby](flowmachinegroup.md#BKMK_lk_flowmachinegroup_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_flowmachinegroup_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_flowmachinegroup"></a> user_flowmachinegroup

**Added by**: Active Solution Solution

Same as flowmachinegroup table [user_flowmachinegroup](flowmachinegroup.md#BKMK_user_flowmachinegroup) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_flowmachinegroup|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processstageparameter_createdby"></a> lk_processstageparameter_createdby

**Added by**: Active Solution Solution

Same as processstageparameter table [lk_processstageparameter_createdby](processstageparameter.md#BKMK_lk_processstageparameter_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_processstageparameter_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processstageparameter_createdonbehalfby"></a> lk_processstageparameter_createdonbehalfby

**Added by**: Active Solution Solution

Same as processstageparameter table [lk_processstageparameter_createdonbehalfby](processstageparameter.md#BKMK_lk_processstageparameter_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_processstageparameter_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processstageparameter_modifiedby"></a> lk_processstageparameter_modifiedby

**Added by**: Active Solution Solution

Same as processstageparameter table [lk_processstageparameter_modifiedby](processstageparameter.md#BKMK_lk_processstageparameter_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_processstageparameter_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processstageparameter_modifiedonbehalfby"></a> lk_processstageparameter_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as processstageparameter table [lk_processstageparameter_modifiedonbehalfby](processstageparameter.md#BKMK_lk_processstageparameter_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_processstageparameter_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_processstageparameter"></a> user_processstageparameter

**Added by**: Active Solution Solution

Same as processstageparameter table [user_processstageparameter](processstageparameter.md#BKMK_user_processstageparameter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_processstageparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowsession_createdby"></a> lk_flowsession_createdby

**Added by**: Active Solution Solution

Same as flowsession table [lk_flowsession_createdby](flowsession.md#BKMK_lk_flowsession_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_flowsession_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowsession_createdonbehalfby"></a> lk_flowsession_createdonbehalfby

**Added by**: Active Solution Solution

Same as flowsession table [lk_flowsession_createdonbehalfby](flowsession.md#BKMK_lk_flowsession_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_flowsession_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowsession_modifiedby"></a> lk_flowsession_modifiedby

**Added by**: Active Solution Solution

Same as flowsession table [lk_flowsession_modifiedby](flowsession.md#BKMK_lk_flowsession_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_flowsession_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_flowsession_modifiedonbehalfby"></a> lk_flowsession_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as flowsession table [lk_flowsession_modifiedonbehalfby](flowsession.md#BKMK_lk_flowsession_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_flowsession_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_flowsession"></a> user_flowsession

**Added by**: Active Solution Solution

Same as flowsession table [user_flowsession](flowsession.md#BKMK_user_flowsession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_flowsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowbinary_createdby"></a> lk_workflowbinary_createdby

**Added by**: Active Solution Solution

Same as workflowbinary table [lk_workflowbinary_createdby](workflowbinary.md#BKMK_lk_workflowbinary_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowbinary_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowbinary_createdonbehalfby"></a> lk_workflowbinary_createdonbehalfby

**Added by**: Active Solution Solution

Same as workflowbinary table [lk_workflowbinary_createdonbehalfby](workflowbinary.md#BKMK_lk_workflowbinary_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_workflowbinary_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowbinary_modifiedby"></a> lk_workflowbinary_modifiedby

**Added by**: Active Solution Solution

Same as workflowbinary table [lk_workflowbinary_modifiedby](workflowbinary.md#BKMK_lk_workflowbinary_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowbinary_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowbinary_modifiedonbehalfby"></a> lk_workflowbinary_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as workflowbinary table [lk_workflowbinary_modifiedonbehalfby](workflowbinary.md#BKMK_lk_workflowbinary_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_workflowbinary_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_workflowbinary"></a> user_workflowbinary

**Added by**: Active Solution Solution

Same as workflowbinary table [user_workflowbinary](workflowbinary.md#BKMK_user_workflowbinary) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_workflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionreference_createdby"></a> lk_connectionreference_createdby

**Added by**: Active Solution Solution

Same as connectionreference table [lk_connectionreference_createdby](connectionreference.md#BKMK_lk_connectionreference_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_connectionreference_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionreference_createdonbehalfby"></a> lk_connectionreference_createdonbehalfby

**Added by**: Active Solution Solution

Same as connectionreference table [lk_connectionreference_createdonbehalfby](connectionreference.md#BKMK_lk_connectionreference_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connectionreference_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionreference_modifiedby"></a> lk_connectionreference_modifiedby

**Added by**: Active Solution Solution

Same as connectionreference table [lk_connectionreference_modifiedby](connectionreference.md#BKMK_lk_connectionreference_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connectionreference_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_connectionreference_modifiedonbehalfby"></a> lk_connectionreference_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as connectionreference table [lk_connectionreference_modifiedonbehalfby](connectionreference.md#BKMK_lk_connectionreference_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_connectionreference_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_connectionreference"></a> user_connectionreference

**Added by**: Active Solution Solution

Same as connectionreference table [user_connectionreference](connectionreference.md#BKMK_user_connectionreference) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_connectionreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiconfiguration_createdby"></a> lk_msdyn_aiconfiguration_createdby

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration table [lk_msdyn_aiconfiguration_createdby](msdyn_aiconfiguration.md#BKMK_lk_msdyn_aiconfiguration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiconfiguration_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiconfiguration_createdonbehalfby"></a> lk_msdyn_aiconfiguration_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration table [lk_msdyn_aiconfiguration_createdonbehalfby](msdyn_aiconfiguration.md#BKMK_lk_msdyn_aiconfiguration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiconfiguration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiconfiguration_modifiedby"></a> lk_msdyn_aiconfiguration_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration table [lk_msdyn_aiconfiguration_modifiedby](msdyn_aiconfiguration.md#BKMK_lk_msdyn_aiconfiguration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiconfiguration_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby"></a> lk_msdyn_aiconfiguration_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration table [lk_msdyn_aiconfiguration_modifiedonbehalfby](msdyn_aiconfiguration.md#BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiconfiguration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aiconfiguration"></a> user_msdyn_aiconfiguration

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration table [user_msdyn_aiconfiguration](msdyn_aiconfiguration.md#BKMK_user_msdyn_aiconfiguration) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aiconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aimodel_createdby"></a> lk_msdyn_aimodel_createdby

**Added by**: Active Solution Solution

Same as msdyn_aimodel table [lk_msdyn_aimodel_createdby](msdyn_aimodel.md#BKMK_lk_msdyn_aimodel_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aimodel_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aimodel_createdonbehalfby"></a> lk_msdyn_aimodel_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aimodel table [lk_msdyn_aimodel_createdonbehalfby](msdyn_aimodel.md#BKMK_lk_msdyn_aimodel_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aimodel_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aimodel_modifiedby"></a> lk_msdyn_aimodel_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aimodel table [lk_msdyn_aimodel_modifiedby](msdyn_aimodel.md#BKMK_lk_msdyn_aimodel_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aimodel_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aimodel_modifiedonbehalfby"></a> lk_msdyn_aimodel_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aimodel table [lk_msdyn_aimodel_modifiedonbehalfby](msdyn_aimodel.md#BKMK_lk_msdyn_aimodel_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aimodel_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aimodel"></a> user_msdyn_aimodel

**Added by**: Active Solution Solution

Same as msdyn_aimodel table [user_msdyn_aimodel](msdyn_aimodel.md#BKMK_user_msdyn_aimodel) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aimodel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aitemplate_createdby"></a> lk_msdyn_aitemplate_createdby

**Added by**: Active Solution Solution

Same as msdyn_aitemplate table [lk_msdyn_aitemplate_createdby](msdyn_aitemplate.md#BKMK_lk_msdyn_aitemplate_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aitemplate_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aitemplate_createdonbehalfby"></a> lk_msdyn_aitemplate_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aitemplate table [lk_msdyn_aitemplate_createdonbehalfby](msdyn_aitemplate.md#BKMK_lk_msdyn_aitemplate_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aitemplate_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aitemplate_modifiedby"></a> lk_msdyn_aitemplate_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aitemplate table [lk_msdyn_aitemplate_modifiedby](msdyn_aitemplate.md#BKMK_lk_msdyn_aitemplate_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aitemplate_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aitemplate_modifiedonbehalfby"></a> lk_msdyn_aitemplate_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aitemplate table [lk_msdyn_aitemplate_modifiedonbehalfby](msdyn_aitemplate.md#BKMK_lk_msdyn_aitemplate_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aitemplate_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aitemplate"></a> user_msdyn_aitemplate

**Added by**: Active Solution Solution

Same as msdyn_aitemplate table [user_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_user_msdyn_aitemplate) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aitemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aifptrainingdocument_createdby"></a> lk_msdyn_aifptrainingdocument_createdby

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument table [lk_msdyn_aifptrainingdocument_createdby](msdyn_aifptrainingdocument.md#BKMK_lk_msdyn_aifptrainingdocument_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aifptrainingdocument_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aifptrainingdocument_createdonbehalfby"></a> lk_msdyn_aifptrainingdocument_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument table [lk_msdyn_aifptrainingdocument_createdonbehalfby](msdyn_aifptrainingdocument.md#BKMK_lk_msdyn_aifptrainingdocument_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aifptrainingdocument_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aifptrainingdocument_modifiedby"></a> lk_msdyn_aifptrainingdocument_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument table [lk_msdyn_aifptrainingdocument_modifiedby](msdyn_aifptrainingdocument.md#BKMK_lk_msdyn_aifptrainingdocument_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aifptrainingdocument_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aifptrainingdocument_modifiedonbehalfby"></a> lk_msdyn_aifptrainingdocument_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument table [lk_msdyn_aifptrainingdocument_modifiedonbehalfby](msdyn_aifptrainingdocument.md#BKMK_lk_msdyn_aifptrainingdocument_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aifptrainingdocument_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aifptrainingdocument"></a> user_msdyn_aifptrainingdocument

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument table [user_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_user_msdyn_aifptrainingdocument) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aifptrainingdocument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodimage_createdby"></a> lk_msdyn_aiodimage_createdby

**Added by**: Active Solution Solution

Same as msdyn_aiodimage table [lk_msdyn_aiodimage_createdby](msdyn_aiodimage.md#BKMK_lk_msdyn_aiodimage_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodimage_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodimage_createdonbehalfby"></a> lk_msdyn_aiodimage_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodimage table [lk_msdyn_aiodimage_createdonbehalfby](msdyn_aiodimage.md#BKMK_lk_msdyn_aiodimage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodimage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodimage_modifiedby"></a> lk_msdyn_aiodimage_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aiodimage table [lk_msdyn_aiodimage_modifiedby](msdyn_aiodimage.md#BKMK_lk_msdyn_aiodimage_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodimage_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodimage_modifiedonbehalfby"></a> lk_msdyn_aiodimage_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodimage table [lk_msdyn_aiodimage_modifiedonbehalfby](msdyn_aiodimage.md#BKMK_lk_msdyn_aiodimage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodimage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aiodimage"></a> user_msdyn_aiodimage

**Added by**: Active Solution Solution

Same as msdyn_aiodimage table [user_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_user_msdyn_aiodimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aiodimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodlabel_createdby"></a> lk_msdyn_aiodlabel_createdby

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel table [lk_msdyn_aiodlabel_createdby](msdyn_aiodlabel.md#BKMK_lk_msdyn_aiodlabel_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodlabel_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodlabel_createdonbehalfby"></a> lk_msdyn_aiodlabel_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel table [lk_msdyn_aiodlabel_createdonbehalfby](msdyn_aiodlabel.md#BKMK_lk_msdyn_aiodlabel_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodlabel_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodlabel_modifiedby"></a> lk_msdyn_aiodlabel_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel table [lk_msdyn_aiodlabel_modifiedby](msdyn_aiodlabel.md#BKMK_lk_msdyn_aiodlabel_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodlabel_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodlabel_modifiedonbehalfby"></a> lk_msdyn_aiodlabel_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel table [lk_msdyn_aiodlabel_modifiedonbehalfby](msdyn_aiodlabel.md#BKMK_lk_msdyn_aiodlabel_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodlabel_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aiodlabel"></a> user_msdyn_aiodlabel

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel table [user_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_user_msdyn_aiodlabel) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aiodlabel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingboundingbox_createdby"></a> lk_msdyn_aiodtrainingboundingbox_createdby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox table [lk_msdyn_aiodtrainingboundingbox_createdby](msdyn_aiodtrainingboundingbox.md#BKMK_lk_msdyn_aiodtrainingboundingbox_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingboundingbox_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingboundingbox_createdonbehalfby"></a> lk_msdyn_aiodtrainingboundingbox_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox table [lk_msdyn_aiodtrainingboundingbox_createdonbehalfby](msdyn_aiodtrainingboundingbox.md#BKMK_lk_msdyn_aiodtrainingboundingbox_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingboundingbox_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingboundingbox_modifiedby"></a> lk_msdyn_aiodtrainingboundingbox_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox table [lk_msdyn_aiodtrainingboundingbox_modifiedby](msdyn_aiodtrainingboundingbox.md#BKMK_lk_msdyn_aiodtrainingboundingbox_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingboundingbox_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby"></a> lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox table [lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby](msdyn_aiodtrainingboundingbox.md#BKMK_lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingboundingbox_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aiodtrainingboundingbox"></a> user_msdyn_aiodtrainingboundingbox

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox table [user_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_user_msdyn_aiodtrainingboundingbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aiodtrainingboundingbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingimage_createdby"></a> lk_msdyn_aiodtrainingimage_createdby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage table [lk_msdyn_aiodtrainingimage_createdby](msdyn_aiodtrainingimage.md#BKMK_lk_msdyn_aiodtrainingimage_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingimage_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingimage_createdonbehalfby"></a> lk_msdyn_aiodtrainingimage_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage table [lk_msdyn_aiodtrainingimage_createdonbehalfby](msdyn_aiodtrainingimage.md#BKMK_lk_msdyn_aiodtrainingimage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingimage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingimage_modifiedby"></a> lk_msdyn_aiodtrainingimage_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage table [lk_msdyn_aiodtrainingimage_modifiedby](msdyn_aiodtrainingimage.md#BKMK_lk_msdyn_aiodtrainingimage_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingimage_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aiodtrainingimage_modifiedonbehalfby"></a> lk_msdyn_aiodtrainingimage_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage table [lk_msdyn_aiodtrainingimage_modifiedonbehalfby](msdyn_aiodtrainingimage.md#BKMK_lk_msdyn_aiodtrainingimage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aiodtrainingimage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aiodtrainingimage"></a> user_msdyn_aiodtrainingimage

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage table [user_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_user_msdyn_aiodtrainingimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aiodtrainingimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdataset_createdby"></a> lk_msdyn_aibdataset_createdby

**Added by**: Active Solution Solution

Same as msdyn_aibdataset table [lk_msdyn_aibdataset_createdby](msdyn_aibdataset.md#BKMK_lk_msdyn_aibdataset_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdataset_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdataset_createdonbehalfby"></a> lk_msdyn_aibdataset_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdataset table [lk_msdyn_aibdataset_createdonbehalfby](msdyn_aibdataset.md#BKMK_lk_msdyn_aibdataset_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdataset_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdataset_modifiedby"></a> lk_msdyn_aibdataset_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aibdataset table [lk_msdyn_aibdataset_modifiedby](msdyn_aibdataset.md#BKMK_lk_msdyn_aibdataset_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdataset_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdataset_modifiedonbehalfby"></a> lk_msdyn_aibdataset_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdataset table [lk_msdyn_aibdataset_modifiedonbehalfby](msdyn_aibdataset.md#BKMK_lk_msdyn_aibdataset_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdataset_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aibdataset"></a> user_msdyn_aibdataset

**Added by**: Active Solution Solution

Same as msdyn_aibdataset table [user_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_user_msdyn_aibdataset) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aibdataset|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetfile_createdby"></a> lk_msdyn_aibdatasetfile_createdby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile table [lk_msdyn_aibdatasetfile_createdby](msdyn_aibdatasetfile.md#BKMK_lk_msdyn_aibdatasetfile_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetfile_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetfile_createdonbehalfby"></a> lk_msdyn_aibdatasetfile_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile table [lk_msdyn_aibdatasetfile_createdonbehalfby](msdyn_aibdatasetfile.md#BKMK_lk_msdyn_aibdatasetfile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetfile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetfile_modifiedby"></a> lk_msdyn_aibdatasetfile_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile table [lk_msdyn_aibdatasetfile_modifiedby](msdyn_aibdatasetfile.md#BKMK_lk_msdyn_aibdatasetfile_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetfile_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetfile_modifiedonbehalfby"></a> lk_msdyn_aibdatasetfile_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile table [lk_msdyn_aibdatasetfile_modifiedonbehalfby](msdyn_aibdatasetfile.md#BKMK_lk_msdyn_aibdatasetfile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetfile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aibdatasetfile"></a> user_msdyn_aibdatasetfile

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile table [user_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_user_msdyn_aibdatasetfile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aibdatasetfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetrecord_createdby"></a> lk_msdyn_aibdatasetrecord_createdby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord table [lk_msdyn_aibdatasetrecord_createdby](msdyn_aibdatasetrecord.md#BKMK_lk_msdyn_aibdatasetrecord_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetrecord_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetrecord_createdonbehalfby"></a> lk_msdyn_aibdatasetrecord_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord table [lk_msdyn_aibdatasetrecord_createdonbehalfby](msdyn_aibdatasetrecord.md#BKMK_lk_msdyn_aibdatasetrecord_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetrecord_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetrecord_modifiedby"></a> lk_msdyn_aibdatasetrecord_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord table [lk_msdyn_aibdatasetrecord_modifiedby](msdyn_aibdatasetrecord.md#BKMK_lk_msdyn_aibdatasetrecord_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetrecord_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetrecord_modifiedonbehalfby"></a> lk_msdyn_aibdatasetrecord_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord table [lk_msdyn_aibdatasetrecord_modifiedonbehalfby](msdyn_aibdatasetrecord.md#BKMK_lk_msdyn_aibdatasetrecord_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetrecord_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aibdatasetrecord"></a> user_msdyn_aibdatasetrecord

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord table [user_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_user_msdyn_aibdatasetrecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aibdatasetrecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetscontainer_createdby"></a> lk_msdyn_aibdatasetscontainer_createdby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer table [lk_msdyn_aibdatasetscontainer_createdby](msdyn_aibdatasetscontainer.md#BKMK_lk_msdyn_aibdatasetscontainer_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetscontainer_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetscontainer_createdonbehalfby"></a> lk_msdyn_aibdatasetscontainer_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer table [lk_msdyn_aibdatasetscontainer_createdonbehalfby](msdyn_aibdatasetscontainer.md#BKMK_lk_msdyn_aibdatasetscontainer_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetscontainer_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetscontainer_modifiedby"></a> lk_msdyn_aibdatasetscontainer_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer table [lk_msdyn_aibdatasetscontainer_modifiedby](msdyn_aibdatasetscontainer.md#BKMK_lk_msdyn_aibdatasetscontainer_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetscontainer_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibdatasetscontainer_modifiedonbehalfby"></a> lk_msdyn_aibdatasetscontainer_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer table [lk_msdyn_aibdatasetscontainer_modifiedonbehalfby](msdyn_aibdatasetscontainer.md#BKMK_lk_msdyn_aibdatasetscontainer_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibdatasetscontainer_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aibdatasetscontainer"></a> user_msdyn_aibdatasetscontainer

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer table [user_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_user_msdyn_aibdatasetscontainer) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aibdatasetscontainer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfile_createdby"></a> lk_msdyn_aibfile_createdby

**Added by**: Active Solution Solution

Same as msdyn_aibfile table [lk_msdyn_aibfile_createdby](msdyn_aibfile.md#BKMK_lk_msdyn_aibfile_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfile_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfile_createdonbehalfby"></a> lk_msdyn_aibfile_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibfile table [lk_msdyn_aibfile_createdonbehalfby](msdyn_aibfile.md#BKMK_lk_msdyn_aibfile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfile_modifiedby"></a> lk_msdyn_aibfile_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aibfile table [lk_msdyn_aibfile_modifiedby](msdyn_aibfile.md#BKMK_lk_msdyn_aibfile_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfile_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfile_modifiedonbehalfby"></a> lk_msdyn_aibfile_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibfile table [lk_msdyn_aibfile_modifiedonbehalfby](msdyn_aibfile.md#BKMK_lk_msdyn_aibfile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aibfile"></a> user_msdyn_aibfile

**Added by**: Active Solution Solution

Same as msdyn_aibfile table [user_msdyn_aibfile](msdyn_aibfile.md#BKMK_user_msdyn_aibfile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aibfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfileattacheddata_createdby"></a> lk_msdyn_aibfileattacheddata_createdby

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata table [lk_msdyn_aibfileattacheddata_createdby](msdyn_aibfileattacheddata.md#BKMK_lk_msdyn_aibfileattacheddata_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfileattacheddata_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfileattacheddata_createdonbehalfby"></a> lk_msdyn_aibfileattacheddata_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata table [lk_msdyn_aibfileattacheddata_createdonbehalfby](msdyn_aibfileattacheddata.md#BKMK_lk_msdyn_aibfileattacheddata_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfileattacheddata_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfileattacheddata_modifiedby"></a> lk_msdyn_aibfileattacheddata_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata table [lk_msdyn_aibfileattacheddata_modifiedby](msdyn_aibfileattacheddata.md#BKMK_lk_msdyn_aibfileattacheddata_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfileattacheddata_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_aibfileattacheddata_modifiedonbehalfby"></a> lk_msdyn_aibfileattacheddata_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata table [lk_msdyn_aibfileattacheddata_modifiedonbehalfby](msdyn_aibfileattacheddata.md#BKMK_lk_msdyn_aibfileattacheddata_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_aibfileattacheddata_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_aibfileattacheddata"></a> user_msdyn_aibfileattacheddata

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata table [user_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_user_msdyn_aibfileattacheddata) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_aibfileattacheddata|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_helppage_createdby"></a> lk_msdyn_helppage_createdby

**Added by**: Active Solution Solution

Same as msdyn_helppage table [lk_msdyn_helppage_createdby](msdyn_helppage.md#BKMK_lk_msdyn_helppage_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_helppage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_helppage_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_helppage_createdonbehalfby"></a> lk_msdyn_helppage_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_helppage table [lk_msdyn_helppage_createdonbehalfby](msdyn_helppage.md#BKMK_lk_msdyn_helppage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_helppage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_helppage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_helppage_modifiedby"></a> lk_msdyn_helppage_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_helppage table [lk_msdyn_helppage_modifiedby](msdyn_helppage.md#BKMK_lk_msdyn_helppage_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_helppage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_helppage_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_helppage_modifiedonbehalfby"></a> lk_msdyn_helppage_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_helppage table [lk_msdyn_helppage_modifiedonbehalfby](msdyn_helppage.md#BKMK_lk_msdyn_helppage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_helppage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_helppage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_tour_createdby"></a> lk_msdyn_tour_createdby

**Added by**: Active Solution Solution

Same as msdyn_tour table [lk_msdyn_tour_createdby](msdyn_tour.md#BKMK_lk_msdyn_tour_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_tour|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_tour_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_tour_createdonbehalfby"></a> lk_msdyn_tour_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_tour table [lk_msdyn_tour_createdonbehalfby](msdyn_tour.md#BKMK_lk_msdyn_tour_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_tour|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_tour_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_tour_modifiedby"></a> lk_msdyn_tour_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_tour table [lk_msdyn_tour_modifiedby](msdyn_tour.md#BKMK_lk_msdyn_tour_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_tour|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_tour_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_tour_modifiedonbehalfby"></a> lk_msdyn_tour_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_tour table [lk_msdyn_tour_modifiedonbehalfby](msdyn_tour.md#BKMK_lk_msdyn_tour_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_tour|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_tour_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdynce_botcontent_createdby"></a> lk_msdynce_botcontent_createdby

**Added by**: Active Solution Solution

Same as msdynce_botcontent table [lk_msdynce_botcontent_createdby](msdynce_botcontent.md#BKMK_lk_msdynce_botcontent_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdynce_botcontent_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdynce_botcontent_createdonbehalfby"></a> lk_msdynce_botcontent_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdynce_botcontent table [lk_msdynce_botcontent_createdonbehalfby](msdynce_botcontent.md#BKMK_lk_msdynce_botcontent_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdynce_botcontent_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdynce_botcontent_modifiedby"></a> lk_msdynce_botcontent_modifiedby

**Added by**: Active Solution Solution

Same as msdynce_botcontent table [lk_msdynce_botcontent_modifiedby](msdynce_botcontent.md#BKMK_lk_msdynce_botcontent_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdynce_botcontent_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdynce_botcontent_modifiedonbehalfby"></a> lk_msdynce_botcontent_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdynce_botcontent table [lk_msdynce_botcontent_modifiedonbehalfby](msdynce_botcontent.md#BKMK_lk_msdynce_botcontent_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdynce_botcontent_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdynce_botcontent"></a> user_msdynce_botcontent

**Added by**: Active Solution Solution

Same as msdynce_botcontent table [user_msdynce_botcontent](msdynce_botcontent.md#BKMK_user_msdynce_botcontent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdynce_botcontent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_conversationtranscript_createdby"></a> lk_conversationtranscript_createdby

**Added by**: Active Solution Solution

Same as conversationtranscript table [lk_conversationtranscript_createdby](conversationtranscript.md#BKMK_lk_conversationtranscript_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_conversationtranscript_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_conversationtranscript_createdonbehalfby"></a> lk_conversationtranscript_createdonbehalfby

**Added by**: Active Solution Solution

Same as conversationtranscript table [lk_conversationtranscript_createdonbehalfby](conversationtranscript.md#BKMK_lk_conversationtranscript_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_conversationtranscript_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_conversationtranscript_modifiedby"></a> lk_conversationtranscript_modifiedby

**Added by**: Active Solution Solution

Same as conversationtranscript table [lk_conversationtranscript_modifiedby](conversationtranscript.md#BKMK_lk_conversationtranscript_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_conversationtranscript_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_conversationtranscript_modifiedonbehalfby"></a> lk_conversationtranscript_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as conversationtranscript table [lk_conversationtranscript_modifiedonbehalfby](conversationtranscript.md#BKMK_lk_conversationtranscript_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_conversationtranscript_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_conversationtranscript"></a> user_conversationtranscript

**Added by**: Active Solution Solution

Same as conversationtranscript table [user_conversationtranscript](conversationtranscript.md#BKMK_user_conversationtranscript) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_conversationtranscript|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bot_createdby"></a> lk_bot_createdby

**Added by**: Active Solution Solution

Same as bot table [lk_bot_createdby](bot.md#BKMK_lk_bot_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_bot_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bot_createdonbehalfby"></a> lk_bot_createdonbehalfby

**Added by**: Active Solution Solution

Same as bot table [lk_bot_createdonbehalfby](bot.md#BKMK_lk_bot_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_bot_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bot_modifiedby"></a> lk_bot_modifiedby

**Added by**: Active Solution Solution

Same as bot table [lk_bot_modifiedby](bot.md#BKMK_lk_bot_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_bot_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_bot_modifiedonbehalfby"></a> lk_bot_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as bot table [lk_bot_modifiedonbehalfby](bot.md#BKMK_lk_bot_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_bot_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_bot"></a> user_bot

**Added by**: Active Solution Solution

Same as bot table [user_bot](bot.md#BKMK_user_bot) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_bot|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_botcomponent_createdby"></a> lk_botcomponent_createdby

**Added by**: Active Solution Solution

Same as botcomponent table [lk_botcomponent_createdby](botcomponent.md#BKMK_lk_botcomponent_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_botcomponent_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_botcomponent_createdonbehalfby"></a> lk_botcomponent_createdonbehalfby

**Added by**: Active Solution Solution

Same as botcomponent table [lk_botcomponent_createdonbehalfby](botcomponent.md#BKMK_lk_botcomponent_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_botcomponent_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_botcomponent_modifiedby"></a> lk_botcomponent_modifiedby

**Added by**: Active Solution Solution

Same as botcomponent table [lk_botcomponent_modifiedby](botcomponent.md#BKMK_lk_botcomponent_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_botcomponent_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_botcomponent_modifiedonbehalfby"></a> lk_botcomponent_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as botcomponent table [lk_botcomponent_modifiedonbehalfby](botcomponent.md#BKMK_lk_botcomponent_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_botcomponent_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_botcomponent"></a> user_botcomponent

**Added by**: Active Solution Solution

Same as botcomponent table [user_botcomponent](botcomponent.md#BKMK_user_botcomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_botcomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuser_bot_publishedby"></a> systemuser_bot_publishedby

**Added by**: Power Virtual Agents Solution

Same as bot table [systemuser_bot_publishedby](bot.md#BKMK_systemuser_bot_publishedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|publishedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuser_bot_publishedby|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_territorybase_createdby"></a> lk_territorybase_createdby

**Added by**: Application Common Solution

Same as territory table [lk_territorybase_createdby](territory.md#BKMK_lk_territorybase_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|territory|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_territorybase_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_territory_createdonbehalfby"></a> lk_territory_createdonbehalfby

**Added by**: Application Common Solution

Same as territory table [lk_territory_createdonbehalfby](territory.md#BKMK_lk_territory_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|territory|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_territorybase_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_territorybase_modifiedby"></a> lk_territorybase_modifiedby

**Added by**: Application Common Solution

Same as territory table [lk_territorybase_modifiedby](territory.md#BKMK_lk_territorybase_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|territory|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_territorybase_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_territory_modifiedonbehalfby"></a> lk_territory_modifiedonbehalfby

**Added by**: Application Common Solution

Same as territory table [lk_territory_modifiedonbehalfby](territory.md#BKMK_lk_territory_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|territory|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_territorybase_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_system_user_territories"></a> system_user_territories

**Added by**: Application Common Solution

Same as territory table [system_user_territories](territory.md#BKMK_system_user_territories) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|territory|
|ReferencingAttribute|managerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|system_user_territories|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activityfileattachment_createdby"></a> lk_activityfileattachment_createdby

**Added by**: Activities Patch Solution

Same as activityfileattachment table [lk_activityfileattachment_createdby](activityfileattachment.md#BKMK_lk_activityfileattachment_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_activityfileattachment_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activityfileattachment_createdonbehalfby"></a> lk_activityfileattachment_createdonbehalfby

**Added by**: Activities Patch Solution

Same as activityfileattachment table [lk_activityfileattachment_createdonbehalfby](activityfileattachment.md#BKMK_lk_activityfileattachment_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_activityfileattachment_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activityfileattachment_modifiedby"></a> lk_activityfileattachment_modifiedby

**Added by**: Activities Patch Solution

Same as activityfileattachment table [lk_activityfileattachment_modifiedby](activityfileattachment.md#BKMK_lk_activityfileattachment_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_activityfileattachment_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_activityfileattachment_modifiedonbehalfby"></a> lk_activityfileattachment_modifiedonbehalfby

**Added by**: Activities Patch Solution

Same as activityfileattachment table [lk_activityfileattachment_modifiedonbehalfby](activityfileattachment.md#BKMK_lk_activityfileattachment_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_activityfileattachment_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_activityfileattachment"></a> user_activityfileattachment

**Added by**: Activities Patch Solution

Same as activityfileattachment table [user_activityfileattachment](activityfileattachment.md#BKMK_user_activityfileattachment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_activityfileattachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_serviceconfiguration_createdby"></a> lk_msdyn_serviceconfiguration_createdby

**Added by**: Active Solution Solution

Same as msdyn_serviceconfiguration table [lk_msdyn_serviceconfiguration_createdby](msdyn_serviceconfiguration.md#BKMK_lk_msdyn_serviceconfiguration_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_serviceconfiguration_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_serviceconfiguration_createdonbehalfby"></a> lk_msdyn_serviceconfiguration_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_serviceconfiguration table [lk_msdyn_serviceconfiguration_createdonbehalfby](msdyn_serviceconfiguration.md#BKMK_lk_msdyn_serviceconfiguration_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_serviceconfiguration_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_serviceconfiguration_modifiedby"></a> lk_msdyn_serviceconfiguration_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_serviceconfiguration table [lk_msdyn_serviceconfiguration_modifiedby](msdyn_serviceconfiguration.md#BKMK_lk_msdyn_serviceconfiguration_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_serviceconfiguration_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_serviceconfiguration_modifiedonbehalfby"></a> lk_msdyn_serviceconfiguration_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_serviceconfiguration table [lk_msdyn_serviceconfiguration_modifiedonbehalfby](msdyn_serviceconfiguration.md#BKMK_lk_msdyn_serviceconfiguration_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_serviceconfiguration_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_serviceconfiguration"></a> user_msdyn_serviceconfiguration

**Added by**: Active Solution Solution

Same as msdyn_serviceconfiguration table [user_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md#BKMK_user_msdyn_serviceconfiguration) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_serviceconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_slakpi_createdby"></a> lk_msdyn_slakpi_createdby

**Added by**: Active Solution Solution

Same as msdyn_slakpi table [lk_msdyn_slakpi_createdby](msdyn_slakpi.md#BKMK_lk_msdyn_slakpi_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_slakpi_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_slakpi_createdonbehalfby"></a> lk_msdyn_slakpi_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_slakpi table [lk_msdyn_slakpi_createdonbehalfby](msdyn_slakpi.md#BKMK_lk_msdyn_slakpi_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_slakpi_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_slakpi_modifiedby"></a> lk_msdyn_slakpi_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_slakpi table [lk_msdyn_slakpi_modifiedby](msdyn_slakpi.md#BKMK_lk_msdyn_slakpi_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_slakpi_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_slakpi_modifiedonbehalfby"></a> lk_msdyn_slakpi_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_slakpi table [lk_msdyn_slakpi_modifiedonbehalfby](msdyn_slakpi.md#BKMK_lk_msdyn_slakpi_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_slakpi_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_slakpi"></a> user_msdyn_slakpi

**Added by**: Active Solution Solution

Same as msdyn_slakpi table [user_msdyn_slakpi](msdyn_slakpi.md#BKMK_user_msdyn_slakpi) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_slakpi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticle_createdby"></a> lk_msdyn_federatedarticle_createdby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticle table [lk_msdyn_federatedarticle_createdby](msdyn_federatedarticle.md#BKMK_lk_msdyn_federatedarticle_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticle_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticle_createdonbehalfby"></a> lk_msdyn_federatedarticle_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticle table [lk_msdyn_federatedarticle_createdonbehalfby](msdyn_federatedarticle.md#BKMK_lk_msdyn_federatedarticle_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticle_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticle_modifiedby"></a> lk_msdyn_federatedarticle_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticle table [lk_msdyn_federatedarticle_modifiedby](msdyn_federatedarticle.md#BKMK_lk_msdyn_federatedarticle_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticle_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticle_modifiedonbehalfby"></a> lk_msdyn_federatedarticle_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticle table [lk_msdyn_federatedarticle_modifiedonbehalfby](msdyn_federatedarticle.md#BKMK_lk_msdyn_federatedarticle_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticle_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_federatedarticle"></a> user_msdyn_federatedarticle

**Added by**: Active Solution Solution

Same as msdyn_federatedarticle table [user_msdyn_federatedarticle](msdyn_federatedarticle.md#BKMK_user_msdyn_federatedarticle) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_federatedarticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticleincident_createdby"></a> lk_msdyn_federatedarticleincident_createdby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticleincident table [lk_msdyn_federatedarticleincident_createdby](msdyn_federatedarticleincident.md#BKMK_lk_msdyn_federatedarticleincident_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticleincident|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticleincident_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticleincident_createdonbehalfby"></a> lk_msdyn_federatedarticleincident_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticleincident table [lk_msdyn_federatedarticleincident_createdonbehalfby](msdyn_federatedarticleincident.md#BKMK_lk_msdyn_federatedarticleincident_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticleincident|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticleincident_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticleincident_modifiedby"></a> lk_msdyn_federatedarticleincident_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticleincident table [lk_msdyn_federatedarticleincident_modifiedby](msdyn_federatedarticleincident.md#BKMK_lk_msdyn_federatedarticleincident_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticleincident|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticleincident_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_federatedarticleincident_modifiedonbehalfby"></a> lk_msdyn_federatedarticleincident_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_federatedarticleincident table [lk_msdyn_federatedarticleincident_modifiedonbehalfby](msdyn_federatedarticleincident.md#BKMK_lk_msdyn_federatedarticleincident_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticleincident|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_federatedarticleincident_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_createdby"></a> lk_msdyn_kmfederatedsearchconfig_createdby

**Added by**: Active Solution Solution

Same as msdyn_kmfederatedsearchconfig table [lk_msdyn_kmfederatedsearchconfig_createdby](msdyn_kmfederatedsearchconfig.md#BKMK_lk_msdyn_kmfederatedsearchconfig_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmfederatedsearchconfig_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_createdonbehalfby"></a> lk_msdyn_kmfederatedsearchconfig_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kmfederatedsearchconfig table [lk_msdyn_kmfederatedsearchconfig_createdonbehalfby](msdyn_kmfederatedsearchconfig.md#BKMK_lk_msdyn_kmfederatedsearchconfig_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmfederatedsearchconfig_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedby"></a> lk_msdyn_kmfederatedsearchconfig_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_kmfederatedsearchconfig table [lk_msdyn_kmfederatedsearchconfig_modifiedby](msdyn_kmfederatedsearchconfig.md#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmfederatedsearchconfig_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby"></a> lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kmfederatedsearchconfig table [lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby](msdyn_kmfederatedsearchconfig.md#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_kmfederatedsearchconfig"></a> user_msdyn_kmfederatedsearchconfig

**Added by**: Active Solution Solution

Same as msdyn_kmfederatedsearchconfig table [user_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md#BKMK_user_msdyn_kmfederatedsearchconfig) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_kmfederatedsearchconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticleimage_createdby"></a> lk_msdyn_knowledgearticleimage_createdby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage table [lk_msdyn_knowledgearticleimage_createdby](msdyn_knowledgearticleimage.md#BKMK_lk_msdyn_knowledgearticleimage_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticleimage_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticleimage_createdonbehalfby"></a> lk_msdyn_knowledgearticleimage_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage table [lk_msdyn_knowledgearticleimage_createdonbehalfby](msdyn_knowledgearticleimage.md#BKMK_lk_msdyn_knowledgearticleimage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticleimage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticleimage_modifiedby"></a> lk_msdyn_knowledgearticleimage_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage table [lk_msdyn_knowledgearticleimage_modifiedby](msdyn_knowledgearticleimage.md#BKMK_lk_msdyn_knowledgearticleimage_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticleimage_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticleimage_modifiedonbehalfby"></a> lk_msdyn_knowledgearticleimage_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage table [lk_msdyn_knowledgearticleimage_modifiedonbehalfby](msdyn_knowledgearticleimage.md#BKMK_lk_msdyn_knowledgearticleimage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticleimage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_knowledgearticleimage"></a> user_msdyn_knowledgearticleimage

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage table [user_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_user_msdyn_knowledgearticleimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_knowledgearticleimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_createdby"></a> lk_msdyn_knowledgeinteractioninsight_createdby

**Added by**: Active Solution Solution

Same as msdyn_knowledgeinteractioninsight table [lk_msdyn_knowledgeinteractioninsight_createdby](msdyn_knowledgeinteractioninsight.md#BKMK_lk_msdyn_knowledgeinteractioninsight_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgeinteractioninsight_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_createdonbehalfby"></a> lk_msdyn_knowledgeinteractioninsight_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgeinteractioninsight table [lk_msdyn_knowledgeinteractioninsight_createdonbehalfby](msdyn_knowledgeinteractioninsight.md#BKMK_lk_msdyn_knowledgeinteractioninsight_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgeinteractioninsight_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedby"></a> lk_msdyn_knowledgeinteractioninsight_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_knowledgeinteractioninsight table [lk_msdyn_knowledgeinteractioninsight_modifiedby](msdyn_knowledgeinteractioninsight.md#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgeinteractioninsight_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby"></a> lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgeinteractioninsight table [lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby](msdyn_knowledgeinteractioninsight.md#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_knowledgeinteractioninsight"></a> user_msdyn_knowledgeinteractioninsight

**Added by**: Active Solution Solution

Same as msdyn_knowledgeinteractioninsight table [user_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md#BKMK_user_msdyn_knowledgeinteractioninsight) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_knowledgeinteractioninsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchinsight_createdby"></a> lk_msdyn_knowledgesearchinsight_createdby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchinsight table [lk_msdyn_knowledgesearchinsight_createdby](msdyn_knowledgesearchinsight.md#BKMK_lk_msdyn_knowledgesearchinsight_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchinsight_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchinsight_createdonbehalfby"></a> lk_msdyn_knowledgesearchinsight_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchinsight table [lk_msdyn_knowledgesearchinsight_createdonbehalfby](msdyn_knowledgesearchinsight.md#BKMK_lk_msdyn_knowledgesearchinsight_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchinsight_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchinsight_modifiedby"></a> lk_msdyn_knowledgesearchinsight_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchinsight table [lk_msdyn_knowledgesearchinsight_modifiedby](msdyn_knowledgesearchinsight.md#BKMK_lk_msdyn_knowledgesearchinsight_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchinsight_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchinsight_modifiedonbehalfby"></a> lk_msdyn_knowledgesearchinsight_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchinsight table [lk_msdyn_knowledgesearchinsight_modifiedonbehalfby](msdyn_knowledgesearchinsight.md#BKMK_lk_msdyn_knowledgesearchinsight_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchinsight_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_knowledgesearchinsight"></a> user_msdyn_knowledgesearchinsight

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchinsight table [user_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md#BKMK_user_msdyn_knowledgesearchinsight) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_knowledgesearchinsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kalanguagesetting_createdby"></a> lk_msdyn_kalanguagesetting_createdby

**Added by**: Active Solution Solution

Same as msdyn_kalanguagesetting table [lk_msdyn_kalanguagesetting_createdby](msdyn_kalanguagesetting.md#BKMK_lk_msdyn_kalanguagesetting_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kalanguagesetting_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kalanguagesetting_createdonbehalfby"></a> lk_msdyn_kalanguagesetting_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kalanguagesetting table [lk_msdyn_kalanguagesetting_createdonbehalfby](msdyn_kalanguagesetting.md#BKMK_lk_msdyn_kalanguagesetting_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kalanguagesetting_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kalanguagesetting_modifiedby"></a> lk_msdyn_kalanguagesetting_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_kalanguagesetting table [lk_msdyn_kalanguagesetting_modifiedby](msdyn_kalanguagesetting.md#BKMK_lk_msdyn_kalanguagesetting_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kalanguagesetting_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kalanguagesetting_modifiedonbehalfby"></a> lk_msdyn_kalanguagesetting_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kalanguagesetting table [lk_msdyn_kalanguagesetting_modifiedonbehalfby](msdyn_kalanguagesetting.md#BKMK_lk_msdyn_kalanguagesetting_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kalanguagesetting_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_kalanguagesetting"></a> user_msdyn_kalanguagesetting

**Added by**: Active Solution Solution

Same as msdyn_kalanguagesetting table [user_msdyn_kalanguagesetting](msdyn_kalanguagesetting.md#BKMK_user_msdyn_kalanguagesetting) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_kalanguagesetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kbattachment_createdby"></a> lk_msdyn_kbattachment_createdby

**Added by**: Active Solution Solution

Same as msdyn_kbattachment table [lk_msdyn_kbattachment_createdby](msdyn_kbattachment.md#BKMK_lk_msdyn_kbattachment_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kbattachment_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kbattachment_createdonbehalfby"></a> lk_msdyn_kbattachment_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kbattachment table [lk_msdyn_kbattachment_createdonbehalfby](msdyn_kbattachment.md#BKMK_lk_msdyn_kbattachment_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kbattachment_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kbattachment_modifiedby"></a> lk_msdyn_kbattachment_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_kbattachment table [lk_msdyn_kbattachment_modifiedby](msdyn_kbattachment.md#BKMK_lk_msdyn_kbattachment_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kbattachment_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kbattachment_modifiedonbehalfby"></a> lk_msdyn_kbattachment_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kbattachment table [lk_msdyn_kbattachment_modifiedonbehalfby](msdyn_kbattachment.md#BKMK_lk_msdyn_kbattachment_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kbattachment_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_kbattachment"></a> user_msdyn_kbattachment

**Added by**: Active Solution Solution

Same as msdyn_kbattachment table [user_msdyn_kbattachment](msdyn_kbattachment.md#BKMK_user_msdyn_kbattachment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_kbattachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmpersonalizationsetting_createdby"></a> lk_msdyn_kmpersonalizationsetting_createdby

**Added by**: Active Solution Solution

Same as msdyn_kmpersonalizationsetting table [lk_msdyn_kmpersonalizationsetting_createdby](msdyn_kmpersonalizationsetting.md#BKMK_lk_msdyn_kmpersonalizationsetting_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmpersonalizationsetting|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmpersonalizationsetting_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmpersonalizationsetting_createdonbehalfby"></a> lk_msdyn_kmpersonalizationsetting_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kmpersonalizationsetting table [lk_msdyn_kmpersonalizationsetting_createdonbehalfby](msdyn_kmpersonalizationsetting.md#BKMK_lk_msdyn_kmpersonalizationsetting_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmpersonalizationsetting|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmpersonalizationsetting_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmpersonalizationsetting_modifiedby"></a> lk_msdyn_kmpersonalizationsetting_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_kmpersonalizationsetting table [lk_msdyn_kmpersonalizationsetting_modifiedby](msdyn_kmpersonalizationsetting.md#BKMK_lk_msdyn_kmpersonalizationsetting_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmpersonalizationsetting|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmpersonalizationsetting_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby"></a> lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_kmpersonalizationsetting table [lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby](msdyn_kmpersonalizationsetting.md#BKMK_lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmpersonalizationsetting|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_kmpersonalizationsetting_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticletemplate_createdby"></a> lk_msdyn_knowledgearticletemplate_createdby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate table [lk_msdyn_knowledgearticletemplate_createdby](msdyn_knowledgearticletemplate.md#BKMK_lk_msdyn_knowledgearticletemplate_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticletemplate_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby"></a> lk_msdyn_knowledgearticletemplate_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate table [lk_msdyn_knowledgearticletemplate_createdonbehalfby](msdyn_knowledgearticletemplate.md#BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticletemplate_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticletemplate_modifiedby"></a> lk_msdyn_knowledgearticletemplate_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate table [lk_msdyn_knowledgearticletemplate_modifiedby](msdyn_knowledgearticletemplate.md#BKMK_lk_msdyn_knowledgearticletemplate_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticletemplate_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby"></a> lk_msdyn_knowledgearticletemplate_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate table [lk_msdyn_knowledgearticletemplate_modifiedonbehalfby](msdyn_knowledgearticletemplate.md#BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgearticletemplate_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_knowledgearticletemplate"></a> user_msdyn_knowledgearticletemplate

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate table [user_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_user_msdyn_knowledgearticletemplate) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_knowledgearticletemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgepersonalfilter_createdby"></a> lk_msdyn_knowledgepersonalfilter_createdby

**Added by**: Active Solution Solution

Same as msdyn_knowledgepersonalfilter table [lk_msdyn_knowledgepersonalfilter_createdby](msdyn_knowledgepersonalfilter.md#BKMK_lk_msdyn_knowledgepersonalfilter_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgepersonalfilter_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgepersonalfilter_createdonbehalfby"></a> lk_msdyn_knowledgepersonalfilter_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgepersonalfilter table [lk_msdyn_knowledgepersonalfilter_createdonbehalfby](msdyn_knowledgepersonalfilter.md#BKMK_lk_msdyn_knowledgepersonalfilter_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgepersonalfilter_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgepersonalfilter_modifiedby"></a> lk_msdyn_knowledgepersonalfilter_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_knowledgepersonalfilter table [lk_msdyn_knowledgepersonalfilter_modifiedby](msdyn_knowledgepersonalfilter.md#BKMK_lk_msdyn_knowledgepersonalfilter_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgepersonalfilter_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby"></a> lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgepersonalfilter table [lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby](msdyn_knowledgepersonalfilter.md#BKMK_lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgepersonalfilter_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_knowledgepersonalfilter"></a> user_msdyn_knowledgepersonalfilter

**Added by**: Active Solution Solution

Same as msdyn_knowledgepersonalfilter table [user_msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md#BKMK_user_msdyn_knowledgepersonalfilter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_knowledgepersonalfilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchfilter_createdby"></a> lk_msdyn_knowledgesearchfilter_createdby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchfilter table [lk_msdyn_knowledgesearchfilter_createdby](msdyn_knowledgesearchfilter.md#BKMK_lk_msdyn_knowledgesearchfilter_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchfilter_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchfilter_createdonbehalfby"></a> lk_msdyn_knowledgesearchfilter_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchfilter table [lk_msdyn_knowledgesearchfilter_createdonbehalfby](msdyn_knowledgesearchfilter.md#BKMK_lk_msdyn_knowledgesearchfilter_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchfilter_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchfilter_modifiedby"></a> lk_msdyn_knowledgesearchfilter_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchfilter table [lk_msdyn_knowledgesearchfilter_modifiedby](msdyn_knowledgesearchfilter.md#BKMK_lk_msdyn_knowledgesearchfilter_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchfilter_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_knowledgesearchfilter_modifiedonbehalfby"></a> lk_msdyn_knowledgesearchfilter_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchfilter table [lk_msdyn_knowledgesearchfilter_modifiedonbehalfby](msdyn_knowledgesearchfilter.md#BKMK_lk_msdyn_knowledgesearchfilter_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_knowledgesearchfilter_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_knowledgesearchfilter"></a> user_msdyn_knowledgesearchfilter

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchfilter table [user_msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md#BKMK_user_msdyn_knowledgesearchfilter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_knowledgesearchfilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_pluginpackage_createdby"></a> lk_pluginpackage_createdby

**Added by**: Active Solution Solution

Same as pluginpackage table [lk_pluginpackage_createdby](pluginpackage.md#BKMK_lk_pluginpackage_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginpackage|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_pluginpackage_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_pluginpackage_createdonbehalfby"></a> lk_pluginpackage_createdonbehalfby

**Added by**: Active Solution Solution

Same as pluginpackage table [lk_pluginpackage_createdonbehalfby](pluginpackage.md#BKMK_lk_pluginpackage_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginpackage|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_pluginpackage_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_pluginpackage_modifiedby"></a> lk_pluginpackage_modifiedby

**Added by**: Active Solution Solution

Same as pluginpackage table [lk_pluginpackage_modifiedby](pluginpackage.md#BKMK_lk_pluginpackage_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginpackage|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_pluginpackage_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_pluginpackage_modifiedonbehalfby"></a> lk_pluginpackage_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as pluginpackage table [lk_pluginpackage_modifiedonbehalfby](pluginpackage.md#BKMK_lk_pluginpackage_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|pluginpackage|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_pluginpackage_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_keyvaultreference_createdby"></a> lk_keyvaultreference_createdby

**Added by**: Active Solution Solution

Same as keyvaultreference table [lk_keyvaultreference_createdby](keyvaultreference.md#BKMK_lk_keyvaultreference_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_keyvaultreference_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_keyvaultreference_createdonbehalfby"></a> lk_keyvaultreference_createdonbehalfby

**Added by**: Active Solution Solution

Same as keyvaultreference table [lk_keyvaultreference_createdonbehalfby](keyvaultreference.md#BKMK_lk_keyvaultreference_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_keyvaultreference_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_keyvaultreference_modifiedby"></a> lk_keyvaultreference_modifiedby

**Added by**: Active Solution Solution

Same as keyvaultreference table [lk_keyvaultreference_modifiedby](keyvaultreference.md#BKMK_lk_keyvaultreference_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_keyvaultreference_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_keyvaultreference_modifiedonbehalfby"></a> lk_keyvaultreference_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as keyvaultreference table [lk_keyvaultreference_modifiedonbehalfby](keyvaultreference.md#BKMK_lk_keyvaultreference_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_keyvaultreference_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_keyvaultreference"></a> user_keyvaultreference

**Added by**: Active Solution Solution

Same as keyvaultreference table [user_keyvaultreference](keyvaultreference.md#BKMK_user_keyvaultreference) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_keyvaultreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_managedidentity_createdby"></a> lk_managedidentity_createdby

**Added by**: Active Solution Solution

Same as managedidentity table [lk_managedidentity_createdby](managedidentity.md#BKMK_lk_managedidentity_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_managedidentity_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_managedidentity_createdonbehalfby"></a> lk_managedidentity_createdonbehalfby

**Added by**: Active Solution Solution

Same as managedidentity table [lk_managedidentity_createdonbehalfby](managedidentity.md#BKMK_lk_managedidentity_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_managedidentity_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_managedidentity_modifiedby"></a> lk_managedidentity_modifiedby

**Added by**: Active Solution Solution

Same as managedidentity table [lk_managedidentity_modifiedby](managedidentity.md#BKMK_lk_managedidentity_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_managedidentity_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_managedidentity_modifiedonbehalfby"></a> lk_managedidentity_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as managedidentity table [lk_managedidentity_modifiedonbehalfby](managedidentity.md#BKMK_lk_managedidentity_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_managedidentity_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_managedidentity"></a> user_managedidentity

**Added by**: Active Solution Solution

Same as managedidentity table [user_managedidentity](managedidentity.md#BKMK_user_managedidentity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_managedidentity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_acceptingentity_systemuser"></a> email_acceptingentity_systemuser

**Added by**: msft_ActivitiesInfra_Extensions Solution

Same as email table [email_acceptingentity_systemuser](email.md#BKMK_email_acceptingentity_systemuser) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|acceptingentityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_acceptingentity_systemuser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_virtualentitymetadata_createdby"></a> lk_virtualentitymetadata_createdby

**Added by**: Active Solution Solution

Same as virtualentitymetadata table [lk_virtualentitymetadata_createdby](virtualentitymetadata.md#BKMK_lk_virtualentitymetadata_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|virtualentitymetadata|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_virtualentitymetadata_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_virtualentitymetadata_createdonbehalfby"></a> lk_virtualentitymetadata_createdonbehalfby

**Added by**: Active Solution Solution

Same as virtualentitymetadata table [lk_virtualentitymetadata_createdonbehalfby](virtualentitymetadata.md#BKMK_lk_virtualentitymetadata_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|virtualentitymetadata|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_virtualentitymetadata_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_virtualentitymetadata_modifiedby"></a> lk_virtualentitymetadata_modifiedby

**Added by**: Active Solution Solution

Same as virtualentitymetadata table [lk_virtualentitymetadata_modifiedby](virtualentitymetadata.md#BKMK_lk_virtualentitymetadata_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|virtualentitymetadata|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_virtualentitymetadata_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_virtualentitymetadata_modifiedonbehalfby"></a> lk_virtualentitymetadata_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as virtualentitymetadata table [lk_virtualentitymetadata_modifiedonbehalfby](virtualentitymetadata.md#BKMK_lk_virtualentitymetadata_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|virtualentitymetadata|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_virtualentitymetadata_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscription_createdby"></a> lk_organizationdatasyncsubscription_createdby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscription table [lk_organizationdatasyncsubscription_createdby](organizationdatasyncsubscription.md#BKMK_lk_organizationdatasyncsubscription_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscription|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscription_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscription_createdonbehalfby"></a> lk_organizationdatasyncsubscription_createdonbehalfby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscription table [lk_organizationdatasyncsubscription_createdonbehalfby](organizationdatasyncsubscription.md#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscription|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscription_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedby"></a> lk_organizationdatasyncsubscription_modifiedby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscription table [lk_organizationdatasyncsubscription_modifiedby](organizationdatasyncsubscription.md#BKMK_lk_organizationdatasyncsubscription_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscription|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscription_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby"></a> lk_organizationdatasyncsubscription_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscription table [lk_organizationdatasyncsubscription_modifiedonbehalfby](organizationdatasyncsubscription.md#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscription|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscription_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscriptionentity_createdby"></a> lk_organizationdatasyncsubscriptionentity_createdby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscriptionentity table [lk_organizationdatasyncsubscriptionentity_createdby](organizationdatasyncsubscriptionentity.md#BKMK_lk_organizationdatasyncsubscriptionentity_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscriptionentity_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscriptionentity_createdonbehalfby"></a> lk_organizationdatasyncsubscriptionentity_createdonbehalfby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscriptionentity table [lk_organizationdatasyncsubscriptionentity_createdonbehalfby](organizationdatasyncsubscriptionentity.md#BKMK_lk_organizationdatasyncsubscriptionentity_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscriptionentity_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscriptionentity_modifiedby"></a> lk_organizationdatasyncsubscriptionentity_modifiedby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscriptionentity table [lk_organizationdatasyncsubscriptionentity_modifiedby](organizationdatasyncsubscriptionentity.md#BKMK_lk_organizationdatasyncsubscriptionentity_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscriptionentity_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby"></a> lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as organizationdatasyncsubscriptionentity table [lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby](organizationdatasyncsubscriptionentity.md#BKMK_lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_organizationdatasyncsubscriptionentity_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appnotification_createdby"></a> lk_appnotification_createdby

**Added by**: Active Solution Solution

Same as appnotification table [lk_appnotification_createdby](appnotification.md#BKMK_lk_appnotification_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appnotification_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appnotification_createdonbehalfby"></a> lk_appnotification_createdonbehalfby

**Added by**: Active Solution Solution

Same as appnotification table [lk_appnotification_createdonbehalfby](appnotification.md#BKMK_lk_appnotification_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appnotification_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appnotification_modifiedby"></a> lk_appnotification_modifiedby

**Added by**: Active Solution Solution

Same as appnotification table [lk_appnotification_modifiedby](appnotification.md#BKMK_lk_appnotification_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appnotification_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appnotification_modifiedonbehalfby"></a> lk_appnotification_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as appnotification table [lk_appnotification_modifiedonbehalfby](appnotification.md#BKMK_lk_appnotification_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appnotification_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_appnotification"></a> user_appnotification

**Added by**: Active Solution Solution

Same as appnotification table [user_appnotification](appnotification.md#BKMK_user_appnotification) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_appnotification|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appaction_createdby"></a> lk_appaction_createdby

**Added by**: Active Solution Solution

Same as appaction table [lk_appaction_createdby](appaction.md#BKMK_lk_appaction_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appaction_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appaction_createdonbehalfby"></a> lk_appaction_createdonbehalfby

**Added by**: Active Solution Solution

Same as appaction table [lk_appaction_createdonbehalfby](appaction.md#BKMK_lk_appaction_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appaction_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appaction_modifiedby"></a> lk_appaction_modifiedby

**Added by**: Active Solution Solution

Same as appaction table [lk_appaction_modifiedby](appaction.md#BKMK_lk_appaction_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appaction_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_appaction_modifiedonbehalfby"></a> lk_appaction_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as appaction table [lk_appaction_modifiedonbehalfby](appaction.md#BKMK_lk_appaction_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_appaction_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_richtextfile_createdby"></a> lk_msdyn_richtextfile_createdby

**Added by**: Active Solution Solution

Same as msdyn_richtextfile table [lk_msdyn_richtextfile_createdby](msdyn_richtextfile.md#BKMK_lk_msdyn_richtextfile_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_richtextfile_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_richtextfile_createdonbehalfby"></a> lk_msdyn_richtextfile_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_richtextfile table [lk_msdyn_richtextfile_createdonbehalfby](msdyn_richtextfile.md#BKMK_lk_msdyn_richtextfile_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_richtextfile_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_richtextfile_modifiedby"></a> lk_msdyn_richtextfile_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_richtextfile table [lk_msdyn_richtextfile_modifiedby](msdyn_richtextfile.md#BKMK_lk_msdyn_richtextfile_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_richtextfile_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_richtextfile_modifiedonbehalfby"></a> lk_msdyn_richtextfile_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_richtextfile table [lk_msdyn_richtextfile_modifiedonbehalfby](msdyn_richtextfile.md#BKMK_lk_msdyn_richtextfile_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_richtextfile_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_richtextfile"></a> user_msdyn_richtextfile

**Added by**: Active Solution Solution

Same as msdyn_richtextfile table [user_msdyn_richtextfile](msdyn_richtextfile.md#BKMK_user_msdyn_richtextfile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|user_msdyn_richtextfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pminferredtask_createdby"></a> lk_msdyn_pminferredtask_createdby

**Added by**: Active Solution Solution

Same as msdyn_pminferredtask table [lk_msdyn_pminferredtask_createdby](msdyn_pminferredtask.md#BKMK_lk_msdyn_pminferredtask_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pminferredtask_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pminferredtask_createdonbehalfby"></a> lk_msdyn_pminferredtask_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_pminferredtask table [lk_msdyn_pminferredtask_createdonbehalfby](msdyn_pminferredtask.md#BKMK_lk_msdyn_pminferredtask_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pminferredtask_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pminferredtask_modifiedby"></a> lk_msdyn_pminferredtask_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_pminferredtask table [lk_msdyn_pminferredtask_modifiedby](msdyn_pminferredtask.md#BKMK_lk_msdyn_pminferredtask_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pminferredtask_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pminferredtask_modifiedonbehalfby"></a> lk_msdyn_pminferredtask_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_pminferredtask table [lk_msdyn_pminferredtask_modifiedonbehalfby](msdyn_pminferredtask.md#BKMK_lk_msdyn_pminferredtask_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pminferredtask_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_pminferredtask"></a> user_msdyn_pminferredtask

**Added by**: Active Solution Solution

Same as msdyn_pminferredtask table [user_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_user_msdyn_pminferredtask) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_pminferredtask|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pmrecording_createdby"></a> lk_msdyn_pmrecording_createdby

**Added by**: Active Solution Solution

Same as msdyn_pmrecording table [lk_msdyn_pmrecording_createdby](msdyn_pmrecording.md#BKMK_lk_msdyn_pmrecording_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pmrecording_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pmrecording_createdonbehalfby"></a> lk_msdyn_pmrecording_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_pmrecording table [lk_msdyn_pmrecording_createdonbehalfby](msdyn_pmrecording.md#BKMK_lk_msdyn_pmrecording_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pmrecording_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pmrecording_modifiedby"></a> lk_msdyn_pmrecording_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_pmrecording table [lk_msdyn_pmrecording_modifiedby](msdyn_pmrecording.md#BKMK_lk_msdyn_pmrecording_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pmrecording_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_pmrecording_modifiedonbehalfby"></a> lk_msdyn_pmrecording_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_pmrecording table [lk_msdyn_pmrecording_modifiedonbehalfby](msdyn_pmrecording.md#BKMK_lk_msdyn_pmrecording_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_pmrecording_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_pmrecording"></a> user_msdyn_pmrecording

**Added by**: Active Solution Solution

Same as msdyn_pmrecording table [user_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_user_msdyn_pmrecording) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_pmrecording|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysiscomponent_createdby"></a> lk_msdyn_analysiscomponent_createdby

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent table [lk_msdyn_analysiscomponent_createdby](msdyn_analysiscomponent.md#BKMK_lk_msdyn_analysiscomponent_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysiscomponent_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysiscomponent_createdonbehalfby"></a> lk_msdyn_analysiscomponent_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent table [lk_msdyn_analysiscomponent_createdonbehalfby](msdyn_analysiscomponent.md#BKMK_lk_msdyn_analysiscomponent_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysiscomponent_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysiscomponent_modifiedby"></a> lk_msdyn_analysiscomponent_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent table [lk_msdyn_analysiscomponent_modifiedby](msdyn_analysiscomponent.md#BKMK_lk_msdyn_analysiscomponent_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysiscomponent_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby"></a> lk_msdyn_analysiscomponent_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent table [lk_msdyn_analysiscomponent_modifiedonbehalfby](msdyn_analysiscomponent.md#BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysiscomponent_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_analysiscomponent"></a> user_msdyn_analysiscomponent

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent table [user_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_user_msdyn_analysiscomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_analysiscomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisjob_createdby"></a> lk_msdyn_analysisjob_createdby

**Added by**: Active Solution Solution

Same as msdyn_analysisjob table [lk_msdyn_analysisjob_createdby](msdyn_analysisjob.md#BKMK_lk_msdyn_analysisjob_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisjob_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisjob_createdonbehalfby"></a> lk_msdyn_analysisjob_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysisjob table [lk_msdyn_analysisjob_createdonbehalfby](msdyn_analysisjob.md#BKMK_lk_msdyn_analysisjob_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisjob_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisjob_modifiedby"></a> lk_msdyn_analysisjob_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_analysisjob table [lk_msdyn_analysisjob_modifiedby](msdyn_analysisjob.md#BKMK_lk_msdyn_analysisjob_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisjob_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisjob_modifiedonbehalfby"></a> lk_msdyn_analysisjob_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysisjob table [lk_msdyn_analysisjob_modifiedonbehalfby](msdyn_analysisjob.md#BKMK_lk_msdyn_analysisjob_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisjob_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_analysisjob"></a> user_msdyn_analysisjob

**Added by**: Active Solution Solution

Same as msdyn_analysisjob table [user_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_user_msdyn_analysisjob) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_analysisjob|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresult_createdby"></a> lk_msdyn_analysisresult_createdby

**Added by**: Active Solution Solution

Same as msdyn_analysisresult table [lk_msdyn_analysisresult_createdby](msdyn_analysisresult.md#BKMK_lk_msdyn_analysisresult_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresult_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresult_createdonbehalfby"></a> lk_msdyn_analysisresult_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysisresult table [lk_msdyn_analysisresult_createdonbehalfby](msdyn_analysisresult.md#BKMK_lk_msdyn_analysisresult_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresult_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresult_modifiedby"></a> lk_msdyn_analysisresult_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_analysisresult table [lk_msdyn_analysisresult_modifiedby](msdyn_analysisresult.md#BKMK_lk_msdyn_analysisresult_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresult_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresult_modifiedonbehalfby"></a> lk_msdyn_analysisresult_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysisresult table [lk_msdyn_analysisresult_modifiedonbehalfby](msdyn_analysisresult.md#BKMK_lk_msdyn_analysisresult_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresult_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_analysisresult"></a> user_msdyn_analysisresult

**Added by**: Active Solution Solution

Same as msdyn_analysisresult table [user_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_user_msdyn_analysisresult) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_analysisresult|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresultdetail_createdby"></a> lk_msdyn_analysisresultdetail_createdby

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail table [lk_msdyn_analysisresultdetail_createdby](msdyn_analysisresultdetail.md#BKMK_lk_msdyn_analysisresultdetail_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresultdetail_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresultdetail_createdonbehalfby"></a> lk_msdyn_analysisresultdetail_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail table [lk_msdyn_analysisresultdetail_createdonbehalfby](msdyn_analysisresultdetail.md#BKMK_lk_msdyn_analysisresultdetail_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresultdetail_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresultdetail_modifiedby"></a> lk_msdyn_analysisresultdetail_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail table [lk_msdyn_analysisresultdetail_modifiedby](msdyn_analysisresultdetail.md#BKMK_lk_msdyn_analysisresultdetail_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresultdetail_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_analysisresultdetail_modifiedonbehalfby"></a> lk_msdyn_analysisresultdetail_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail table [lk_msdyn_analysisresultdetail_modifiedonbehalfby](msdyn_analysisresultdetail.md#BKMK_lk_msdyn_analysisresultdetail_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_analysisresultdetail_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_analysisresultdetail"></a> user_msdyn_analysisresultdetail

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail table [user_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_user_msdyn_analysisresultdetail) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_analysisresultdetail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthrule_createdby"></a> lk_msdyn_solutionhealthrule_createdby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule table [lk_msdyn_solutionhealthrule_createdby](msdyn_solutionhealthrule.md#BKMK_lk_msdyn_solutionhealthrule_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthrule_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthrule_createdonbehalfby"></a> lk_msdyn_solutionhealthrule_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule table [lk_msdyn_solutionhealthrule_createdonbehalfby](msdyn_solutionhealthrule.md#BKMK_lk_msdyn_solutionhealthrule_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthrule_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthrule_modifiedby"></a> lk_msdyn_solutionhealthrule_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule table [lk_msdyn_solutionhealthrule_modifiedby](msdyn_solutionhealthrule.md#BKMK_lk_msdyn_solutionhealthrule_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthrule_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthrule_modifiedonbehalfby"></a> lk_msdyn_solutionhealthrule_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule table [lk_msdyn_solutionhealthrule_modifiedonbehalfby](msdyn_solutionhealthrule.md#BKMK_lk_msdyn_solutionhealthrule_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthrule_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_solutionhealthrule"></a> user_msdyn_solutionhealthrule

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule table [user_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_user_msdyn_solutionhealthrule) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_solutionhealthrule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleargument_createdby"></a> lk_msdyn_solutionhealthruleargument_createdby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument table [lk_msdyn_solutionhealthruleargument_createdby](msdyn_solutionhealthruleargument.md#BKMK_lk_msdyn_solutionhealthruleargument_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleargument_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleargument_createdonbehalfby"></a> lk_msdyn_solutionhealthruleargument_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument table [lk_msdyn_solutionhealthruleargument_createdonbehalfby](msdyn_solutionhealthruleargument.md#BKMK_lk_msdyn_solutionhealthruleargument_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleargument_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleargument_modifiedby"></a> lk_msdyn_solutionhealthruleargument_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument table [lk_msdyn_solutionhealthruleargument_modifiedby](msdyn_solutionhealthruleargument.md#BKMK_lk_msdyn_solutionhealthruleargument_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleargument_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleargument_modifiedonbehalfby"></a> lk_msdyn_solutionhealthruleargument_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument table [lk_msdyn_solutionhealthruleargument_modifiedonbehalfby](msdyn_solutionhealthruleargument.md#BKMK_lk_msdyn_solutionhealthruleargument_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleargument_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_user_msdyn_solutionhealthruleargument"></a> user_msdyn_solutionhealthruleargument

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument table [user_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_user_msdyn_solutionhealthruleargument) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|owninguser|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|user_msdyn_solutionhealthruleargument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleset_createdby"></a> lk_msdyn_solutionhealthruleset_createdby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleset table [lk_msdyn_solutionhealthruleset_createdby](msdyn_solutionhealthruleset.md#BKMK_lk_msdyn_solutionhealthruleset_createdby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleset|
|ReferencingAttribute|createdby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleset_createdby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleset_createdonbehalfby"></a> lk_msdyn_solutionhealthruleset_createdonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleset table [lk_msdyn_solutionhealthruleset_createdonbehalfby](msdyn_solutionhealthruleset.md#BKMK_lk_msdyn_solutionhealthruleset_createdonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleset|
|ReferencingAttribute|createdonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleset_createdonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleset_modifiedby"></a> lk_msdyn_solutionhealthruleset_modifiedby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleset table [lk_msdyn_solutionhealthruleset_modifiedby](msdyn_solutionhealthruleset.md#BKMK_lk_msdyn_solutionhealthruleset_modifiedby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleset|
|ReferencingAttribute|modifiedby|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleset_modifiedby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_msdyn_solutionhealthruleset_modifiedonbehalfby"></a> lk_msdyn_solutionhealthruleset_modifiedonbehalfby

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleset table [lk_msdyn_solutionhealthruleset_modifiedonbehalfby](msdyn_solutionhealthruleset.md#BKMK_lk_msdyn_solutionhealthruleset_modifiedonbehalfby) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleset|
|ReferencingAttribute|modifiedonbehalfby|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|lk_msdyn_solutionhealthruleset_modifiedonbehalfby|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [systemuser_defaultmailbox_mailbox](#BKMK_systemuser_defaultmailbox_mailbox)
- [position_users](#BKMK_position_users)
- [calendar_system_users](#BKMK_calendar_system_users)
- [business_unit_system_users](#BKMK_business_unit_system_users)
- [MobileOfflineProfile_SystemUser](#BKMK_MobileOfflineProfile_SystemUser)
- [TransactionCurrency_SystemUser](#BKMK_TransactionCurrency_SystemUser)
- [user_parent_user](#BKMK_user_parent_user)
- [organization_system_users](#BKMK_organization_system_users)
- [lk_systemuserbase_modifiedby](#BKMK_lk_systemuserbase_modifiedby)
- [queue_system_user](#BKMK_queue_system_user)
- [lk_systemuser_modifiedonbehalfby](#BKMK_lk_systemuser_modifiedonbehalfby)
- [processstage_systemusers](#BKMK_processstage_systemusers)
- [lk_systemuserbase_createdby](#BKMK_lk_systemuserbase_createdby)
- [lk_systemuser_createdonbehalfby](#BKMK_lk_systemuser_createdonbehalfby)
- [territory_system_users](#BKMK_territory_system_users)


### <a name="BKMK_systemuser_defaultmailbox_mailbox"></a> systemuser_defaultmailbox_mailbox

See mailbox Table [systemuser_defaultmailbox_mailbox](mailbox.md#BKMK_systemuser_defaultmailbox_mailbox) One-To-Many relationship.

### <a name="BKMK_position_users"></a> position_users

See position Table [position_users](position.md#BKMK_position_users) One-To-Many relationship.

### <a name="BKMK_calendar_system_users"></a> calendar_system_users

See calendar Table [calendar_system_users](calendar.md#BKMK_calendar_system_users) One-To-Many relationship.

### <a name="BKMK_business_unit_system_users"></a> business_unit_system_users

See businessunit Table [business_unit_system_users](businessunit.md#BKMK_business_unit_system_users) One-To-Many relationship.

### <a name="BKMK_MobileOfflineProfile_SystemUser"></a> MobileOfflineProfile_SystemUser

See mobileofflineprofile Table [MobileOfflineProfile_SystemUser](mobileofflineprofile.md#BKMK_MobileOfflineProfile_SystemUser) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SystemUser"></a> TransactionCurrency_SystemUser

See transactioncurrency Table [TransactionCurrency_SystemUser](transactioncurrency.md#BKMK_TransactionCurrency_SystemUser) One-To-Many relationship.

### <a name="BKMK_user_parent_user"></a> user_parent_user

See systemuser Table [user_parent_user](systemuser.md#BKMK_user_parent_user) One-To-Many relationship.

### <a name="BKMK_organization_system_users"></a> organization_system_users

See organization Table [organization_system_users](organization.md#BKMK_organization_system_users) One-To-Many relationship.

### <a name="BKMK_lk_systemuserbase_modifiedby"></a> lk_systemuserbase_modifiedby

See systemuser Table [lk_systemuserbase_modifiedby](systemuser.md#BKMK_lk_systemuserbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_queue_system_user"></a> queue_system_user

See queue Table [queue_system_user](queue.md#BKMK_queue_system_user) One-To-Many relationship.

### <a name="BKMK_lk_systemuser_modifiedonbehalfby"></a> lk_systemuser_modifiedonbehalfby

See systemuser Table [lk_systemuser_modifiedonbehalfby](systemuser.md#BKMK_lk_systemuser_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_processstage_systemusers"></a> processstage_systemusers

See processstage Table [processstage_systemusers](processstage.md#BKMK_processstage_systemusers) One-To-Many relationship.

### <a name="BKMK_lk_systemuserbase_createdby"></a> lk_systemuserbase_createdby

See systemuser Table [lk_systemuserbase_createdby](systemuser.md#BKMK_lk_systemuserbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_systemuser_createdonbehalfby"></a> lk_systemuser_createdonbehalfby

See systemuser Table [lk_systemuser_createdonbehalfby](systemuser.md#BKMK_lk_systemuser_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_territory_system_users"></a> territory_system_users

**Added by**: Application Common Solution

See territory Table [territory_system_users](territory.md#BKMK_territory_system_users) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the SystemUser table is the first table in the relationship. Listed by **SchemaName**.

- [systemuserprofiles_association](#BKMK_systemuserprofiles_association)
- [systemuserroles_association](#BKMK_systemuserroles_association)
- [teammembership_association](#BKMK_teammembership_association)
- [queuemembership_association](#BKMK_queuemembership_association)


### <a name="BKMK_systemuserprofiles_association"></a> systemuserprofiles_association

IntersectEntityName: systemuserprofiles<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|systemuserid|
|IsCustomizable|False|
|LogicalName|systemuser|
|NavigationPropertyName|systemuserprofiles_association|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|fieldsecurityprofile|
|IntersectAttribute|fieldsecurityprofileid|
|NavigationPropertyName|systemuserprofiles_association|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_systemuserroles_association"></a> systemuserroles_association

IntersectEntityName: systemuserroles<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|systemuserid|
|IsCustomizable|False|
|LogicalName|systemuser|
|NavigationPropertyName|systemuserroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|role|
|IntersectAttribute|roleid|
|NavigationPropertyName|systemuserroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_teammembership_association"></a> teammembership_association

See team Table [teammembership_association](team.md#BKMK_teammembership_association) Many-To-Many Relationship.

### <a name="BKMK_queuemembership_association"></a> queuemembership_association

See queue Table [queuemembership_association](queue.md#BKMK_queuemembership_association) Many-To-Many Relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.systemuser?text=systemuser EntityType" />