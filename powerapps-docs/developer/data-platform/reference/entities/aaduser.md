---
title: "Microsoft Entra ID (aaduser) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Microsoft Entra ID (aaduser) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Microsoft Entra ID (aaduser) table/entity reference (Microsoft Dataverse)

Virtual entity that represents Microsoft Entra ID

## Messages

The following table lists the messages for the Microsoft Entra ID (aaduser) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /aadusers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /aadusers(*aaduserid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /aadusers(*aaduserid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /aadusers<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /aadusers(*aaduserid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /aadusers(*aaduserid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Microsoft Entra ID (aaduser) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Microsoft Entra ID** |
| **DisplayCollectionName** | **Microsoft Entra IDs** |
| **SchemaName** | `aaduser` |
| **CollectionSchemaName** | `aadusers` |
| **EntitySetName** | `aadusers`|
| **LogicalName** | `aaduser` |
| **LogicalCollectionName** | `aadusers` |
| **PrimaryIdAttribute** | `aaduserid` |
| **PrimaryNameAttribute** |`displayname` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Unique identifier of a Microsoft Entra ID.**|
|DisplayName|**Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`aaduserid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AccountEnabled"></a> AccountEnabled

|Property|Value|
|---|---|
|Description|**Indicates if the Account of an Microsoft Entra ID is enabled.**|
|DisplayName|**Microsoft Entra ID Account Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accountenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`adduser_account_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BusinessPhones"></a> BusinessPhones

|Property|Value|
|---|---|
|Description|**Business phone number for the user**|
|DisplayName|**Business Phones**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`businessphones`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_City"></a> City

|Property|Value|
|---|---|
|Description|**City.**|
|DisplayName|**City**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`city`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CompanyName"></a> CompanyName

|Property|Value|
|---|---|
|Description|**Company Name.**|
|DisplayName|**Company Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`companyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**The name displayed in the address book for the user.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_GivenName"></a> GivenName

|Property|Value|
|---|---|
|Description|**The given name (first name) of the user.**|
|DisplayName|**Given Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`givenname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_id"></a> id

|Property|Value|
|---|---|
|Description|**A unique identifer for Microsoft Entra ID**|
|DisplayName|**A unique identifer for Microsoft Entra ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`id`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ImAddresses"></a> ImAddresses

|Property|Value|
|---|---|
|Description|**ImAddresses for the user**|
|DisplayName|**ImAddresses**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`imaddresses`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_JobTitle"></a> JobTitle

|Property|Value|
|---|---|
|Description|**The user's job title.**|
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

### <a name="BKMK_Mail"></a> Mail

|Property|Value|
|---|---|
|Description|**The SMTP address for the user.**|
|DisplayName|**Mail**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mail`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_MobilePhone"></a> MobilePhone

|Property|Value|
|---|---|
|Description|**The primary cellular telephone number for the user.**|
|DisplayName|**Mobile Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mobilephone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OfficeLocation"></a> OfficeLocation

|Property|Value|
|---|---|
|Description|**The office location in the user's place of business.**|
|DisplayName|**Office Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`officelocation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_PostalCode"></a> PostalCode

|Property|Value|
|---|---|
|Description|**Postal Code.**|
|DisplayName|**Postal Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postalcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_PreferredLanguage"></a> PreferredLanguage

|Property|Value|
|---|---|
|Description|**The preferred language for the user. Should follow ISO 639-1 Code; for example 'en-US'.**|
|DisplayName|**Preferred Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredlanguage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_StreetAddress"></a> StreetAddress

|Property|Value|
|---|---|
|Description|**Street Address.**|
|DisplayName|**Street Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`streetaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_surname"></a> surname

|Property|Value|
|---|---|
|Description|**The user's surname (family name or last name).**|
|DisplayName|**Surname**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`surname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_UserPrincipalName"></a> UserPrincipalName

|Property|Value|
|---|---|
|Description|**The user principal name (UPN) of the user.**|
|DisplayName|**User Principal Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userprincipalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_UserType"></a> UserType

|Property|Value|
|---|---|
|Description|**User Type.**|
|DisplayName|**User Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usertype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

### <a name="BKMK_CreatedDateTime"></a> CreatedDateTime

|Property|Value|
|---|---|
|Description|**Date and time when the Microsoft Entra ID was created.**|
|DisplayName|**Created Date Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createddatetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.aaduser?displayProperty=fullName>
