---
title: "aaduser table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the aaduser table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# aaduser table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Virtual entity that represents AAD user

**Added by**: Metadata Extension Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /aadusers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /aadusers(*aaduserid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /aadusers(*aaduserid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /aadusers<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /aadusers(*aaduserid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|aadusers|
|DisplayCollectionName|AAD Users|
|DisplayName|AAD User|
|EntitySetName|aadusers|
|IsBPFEntity|False|
|LogicalCollectionName|aadusers|
|LogicalName|aaduser|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|aaduserid|
|PrimaryNameAttribute|displayname|
|SchemaName|aaduser|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [aaduserId](#BKMK_aaduserId)
- [AccountEnabled](#BKMK_AccountEnabled)
- [BusinessPhones](#BKMK_BusinessPhones)
- [City](#BKMK_City)
- [CompanyName](#BKMK_CompanyName)
- [DisplayName](#BKMK_DisplayName)
- [GivenName](#BKMK_GivenName)
- [id](#BKMK_id)
- [ImAddresses](#BKMK_ImAddresses)
- [JobTitle](#BKMK_JobTitle)
- [Mail](#BKMK_Mail)
- [MobilePhone](#BKMK_MobilePhone)
- [OfficeLocation](#BKMK_OfficeLocation)
- [PostalCode](#BKMK_PostalCode)
- [PreferredLanguage](#BKMK_PreferredLanguage)
- [StreetAddress](#BKMK_StreetAddress)
- [surname](#BKMK_surname)
- [UserPrincipalName](#BKMK_UserPrincipalName)
- [UserType](#BKMK_UserType)


### <a name="BKMK_aaduserId"></a> aaduserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of an aad user.|
|DisplayName|AAD user id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|aaduserid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AccountEnabled"></a> AccountEnabled

|Property|Value|
|--------|-----|
|Description|Indicates if the Account of an AAD User is enabled.|
|DisplayName|AAD User Account Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|accountenabled|
|RequiredLevel|None|
|Type|Boolean|

#### AccountEnabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_BusinessPhones"></a> BusinessPhones

|Property|Value|
|--------|-----|
|Description|Business phone number for the user|
|DisplayName|Business Phones|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|businessphones|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_City"></a> City

|Property|Value|
|--------|-----|
|Description|City.|
|DisplayName|City|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|city|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CompanyName"></a> CompanyName

|Property|Value|
|--------|-----|
|Description|Company Name.|
|DisplayName|Company Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|companyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|--------|-----|
|Description|The name displayed in the address book for the user.|
|DisplayName|Display Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|displayname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_GivenName"></a> GivenName

|Property|Value|
|--------|-----|
|Description|The given name (first name) of the user.|
|DisplayName|Given Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|givenname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_id"></a> id

|Property|Value|
|--------|-----|
|Description|A unique identifer for AAD User|
|DisplayName|A unique identifer for AAD User|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|id|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImAddresses"></a> ImAddresses

|Property|Value|
|--------|-----|
|Description|ImAddresses for the user|
|DisplayName|ImAddresses|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|imaddresses|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_JobTitle"></a> JobTitle

|Property|Value|
|--------|-----|
|Description|The user's job title.|
|DisplayName|Job Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|jobtitle|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Mail"></a> Mail

|Property|Value|
|--------|-----|
|Description|The SMTP address for the user.|
|DisplayName|Mail|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mail|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobilePhone"></a> MobilePhone

|Property|Value|
|--------|-----|
|Description|The primary cellular telephone number for the user.|
|DisplayName|Mobile Phone|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobilephone|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OfficeLocation"></a> OfficeLocation

|Property|Value|
|--------|-----|
|Description|The office location in the user's place of business.|
|DisplayName|Office Location|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|officelocation|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PostalCode"></a> PostalCode

|Property|Value|
|--------|-----|
|Description|Postal Code.|
|DisplayName|Postal Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postalcode|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PreferredLanguage"></a> PreferredLanguage

|Property|Value|
|--------|-----|
|Description|The preferred language for the user. Should follow ISO 639-1 Code; for example 'en-US'.|
|DisplayName|Preferred Language|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|preferredlanguage|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StreetAddress"></a> StreetAddress

|Property|Value|
|--------|-----|
|Description|Street Address.|
|DisplayName|Street Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|streetaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_surname"></a> surname

|Property|Value|
|--------|-----|
|Description|The user's surname (family name or last name).|
|DisplayName|Surname|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|surname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UserPrincipalName"></a> UserPrincipalName

|Property|Value|
|--------|-----|
|Description|The user principal name (UPN) of the user.|
|DisplayName|User Principal Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|userprincipalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UserType"></a> UserType

|Property|Value|
|--------|-----|
|Description|User Type.|
|DisplayName|User Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|usertype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


### <a name="BKMK_CreatedDateTime"></a> CreatedDateTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the AAD user was created.|
|DisplayName|Created Date Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createddatetime|
|RequiredLevel|None|
|Type|DateTime|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.aaduser?text=aaduser EntityType" />