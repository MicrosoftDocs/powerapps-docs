---
title: "getGlobalContext.organizationSettings (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 02/06/2020
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: badf4f82-cb47-4864-aa43-bb777d04de4d
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getGlobalContext.organizationSettings (Client API reference)



Returns information about the current organization settings. 

`var organizationSettings = Xrm.Utility.getGlobalContext().organizationSettings`

The **organizationSettings** object provides following properties.

## attributes

Returns attributes and their values as `key:value` pairs that are available for the organization entity. Additional values will be available as attributes if they are specified as attribute dependencies in the web resource dependency list. The `key` will be the attribute logical name.

### Syntax

`organizationSettings.attributes`

### Return Value

**Type**: Object

**Description**: An object with attributes and their values.

## baseCurrencyId 

Returns the ID of the base currency for the current organization.

Deprecated; use [organizationSettings.baseCurrency](#basecurrency) instead to access the display name along with the ID of the base currency.

### Syntax

`organizationSettings.baseCurrencyId`

### Return Value

**Type**: String

**Description**: ID of the base currency. 

## baseCurrency 

Returns a lookup object containing the ID, name, and entity type of the base currency for the current organization. This method is supported only on the Unified Interface.

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

**Description**: Id of the current organization.

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


## Related topics

[Client context](client.md)

[User settings](userSettings.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)