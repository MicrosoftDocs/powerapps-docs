---
title: "getGlobalContext.organizationSettings (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getGlobalContext.organizationSettings method.
author: adrianorth
ms.author: aorth
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

The **organizationSettings** object has the following properties.

## attributes

Returns columns and their values as `key:value` pairs that are available for the organization table. More values are available as columns if they're specified as column dependencies in the web resource dependency list. The `key` is the column logical name.

### Syntax

`organizationSettings.attributes`

### Return Value

**Type**: Object

**Description**: An object with columns and their values.

## baseCurrencyId 

Returns the ID of the base currency for the current organization.

Deprecated; use [organizationSettings.baseCurrency](#basecurrency) instead to access the display name along with the ID of the base currency.

### Syntax

`organizationSettings.baseCurrencyId`

### Return Value

**Type**: String

**Description**: ID of the base currency. 

## baseCurrency 

Returns a lookup object containing the ID, name, and table type of the base currency for the current organization. This method is supported only on Unified Interface.

### Syntax

`organizationSettings.baseCurrency`
 
### Return Value

**Type**: Lookup Object

**Description**: Object containing the `id`, `name`, and `entityType` of the base currency. For example:

`{id: "e7dd9bc6-d239-ea11-a813-000d3a35b14a", entityType: "transactioncurrency", name: "US Dollar"}`

## defaultCountryCode 

Returns the default country/region code for phone numbers for the current organization.

### Syntax

`organizationSettings.defaultCountryCode`

### Return Value

**Type**: String

**Description**: Default country/region code for phone numbers.

## isAutoSaveEnabled 

Indicates whether the auto-save option is enabled for the current organization.

### Syntax

`organizationSettings.isAutoSaveEnabled`

### Return Value

**Type**: Boolean

**Description**: **true** if enabled; **false** otherwise.

## languageId 

Returns the preferred language ID for the current organization.

### Syntax

`organizationSettings.languageId`

### Return Value

**Type**: Number

**Description**: Preferred Language ID. For example:

`1033`

## organizationId 

Returns the ID of the current organization.

### Syntax

`organizationSettings.organizationId`

### Return Value

**Type**: String

**Description**: ID of the current organization.

## isTrialOrganization

Returns a boolean indicating whether the organization is a trial organization.

[!INCLUDE [online-only-api-note](../../../includes/online-only-api-note.md)]

### Syntax

`organizationSettings.isTrialOrganization`

### Return Value

**Type**: Boolean

**Description**: **true** if the organization is a trial organization; **false** otherwise.

## organizationExpiryDate

Returns the expiry date of the current organization if it's a trial organization.

[!INCLUDE [online-only-api-note](../../../includes/online-only-api-note.md)]

### Syntax

`organizationSettings.organizationExpiryDate`

### Return Value

**Type**: Date

**Description**: Returns a `Date` object with the organization's expiry date if it's a trial organization. Returns NULL if the organization isn't a trial organization.

## uniqueName 

Returns the unique name of the current organization.

### Syntax

`organizationSettings.uniqueName`

### Return Value

**Type**: String

**Description**: Unique name of the current organization.

## useSkypeProtocol 

Indicates whether the Skype protocol is used for the current organization.

### Syntax

`organizationSettings.useSkypeProtocol`

### Return Value

**Type**: Boolean

**Description**: **true** if Skype protocol is used; **false** otherwise.

## fullNameConventionCode 

Returns the FullNameConventionCode setting of the current organization.

### Syntax

`organizationSettings.fullNameConventionCode`

### Return Value

**Type**: Number

**Description**: Returns a number denoting the full name format selected in the system settings. The following are the possible values and the corresponding format:

0: LastName, FirstName <br/>
1: FirstName LastName <br/>
2: LastName, FirstName MiddleInitial <br/>
3: FirstName MiddleInitial LastName <br/>
4: LastName, FirstName MiddleName <br/>
5: FirstNamet MiddleName LastName <br/>
6: LastName FirstName <br/>
7: LastNameFirstName 

## Related articles

[Client context](client.md)

[User settings](userSettings.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)


[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
