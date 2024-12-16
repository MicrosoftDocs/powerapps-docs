---
title: "getGlobalContext.organizationSettings (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getGlobalContext.organizationSettings method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getGlobalContext.organizationSettings (Client API reference)

Returns information about the current organization settings. 

`var organizationSettings = Xrm.Utility.getGlobalContext().organizationSettings`

## Properties

The `organizationSettings` object has the following properties:


|Name|Type|Description|
|---------|---------|---------|
|`attributes`|object|An object with columns and their values. See [attributes](#attributes)|
|`baseCurrencyId`|string|Deprecated. Use `baseCurrency` property instead.|
|`baseCurrency`|object|Object containing the `id`, `name`, and `entityType` of the base currency for the current organization. See [baseCurrency](#basecurrency)|
|`defaultCountryCode`|string|The default country/region code for phone numbers for the current organization.|
|`isAutoSaveEnabled`|bool|Whether the auto-save option is enabled for the current organization.|
|`languageId`|string|The preferred [LCID language code](/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a) for the current organization.|
|`organizationId`|string|ID of the current organization.|
|`isTrialOrganization`|bool|Whether the organization is a trial environment.|
|`organizationExpiryDate`|Date?|The expiry date of the current organization if it's a trial environment, otherwise null.|
|`uniqueName`|string|the unique name of the current organization.|
|`useSkypeProtocol`|bool|Whether the Skype protocol is used for the current organization.|
|`fullNameConventionCode`|number|The `FullNameConventionCode` setting of the current organization. See [fullNameConventionCode](#fullnameconventioncode)|

### attributes

Returns columns and their values as `key:value` pairs that are available for the organization table. More values are available as columns if they're specified as column dependencies in the web resource dependency list. The `key` is the column logical name.

### baseCurrency

This method is supported only on Unified Interface.

The lookup object will look something like the following:

```json
{
   id: "e7dd9bc6-d239-ea11-a813-000d3a35b14a", 
   entityType: "transactioncurrency", 
   name: "US Dollar"
}
```


### fullNameConventionCode

Returns a number denoting the full name format selected in the system settings. The following are the possible values and the corresponding format:

|Number |Format|
|---------|---------|
|0|LastName, FirstName|
|1|FirstName LastName|
|2|LastName, FirstName MiddleInitial|
|3|FirstName MiddleInitial LastName|
|4|LastName, FirstName MiddleName |
|5|FirstName MiddleName LastName |
|6|LastName FirstName|
|7|LastNameFirstName|

## Related articles

[Client context](client.md)   
[User settings](userSettings.md)   
[Xrm.Utility.getGlobalContext](../getGlobalContext.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
