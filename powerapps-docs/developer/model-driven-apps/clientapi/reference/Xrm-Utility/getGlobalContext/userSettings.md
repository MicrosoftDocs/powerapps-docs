---
title: "getGlobalContext.userSettings (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 02/06/2020
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 44296667-f1cd-49be-a300-7259bc3b41e0
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getGlobalContext.userSettings (Client API reference)

Returns information about the current user settings.

`var userSettings = Xrm.Utility.getGlobalContext().userSettings`

The **userSettings** object provides following properties and a method.

## dateFormattingInfo 

Returns the date formatting information for the current user.

### Syntax

`userSettings.dateFormattingInfo`

### Return Value

**Type**: Object

**Description**: An object with information about date formatting such as **FirstDayOfWeek**, **LongDatePattern**, **MonthDayPattern**, **TimeSeparator**, and so on.

## defaultDashboardId 

Returns the ID of the default dashboard for the current user.

### Syntax

`userSettings.defaultDashboardId`

### Return Value

**Type**: String

**Description**: ID of the default dashboard. 

## isGuidedHelpEnabled 

Indicates whether guided help is enabled for the current user.

### Syntax

`userSettings.isGuidedHelpEnabled`

### Return Value

**Type**: Boolean

**Description**: true if enabled; false otherwise. 

## isHighContrastEnabled 

Indicates whether high contrast is enabled for the current user.

### Syntax

`userSettings.isHighContrastEnabled`

### Return Value

**Type**: Boolean

**Description**: true if enabled; false otherwise.

## isRTL 

Indicates whether the language for the current user is a right-to-left (RTL) language.

### Syntax

`userSettings.isRTL`

### Return Value

**Type**: Boolean

**Description**: true if it is RTL; false otherwise.

## languageId 

Returns the language ID for the current user.

### Syntax

`userSettings.languageId`

### Return Value

**Type**: Number

**Description**: Language ID.

## roles 

Returns a collection of lookup objects containing the GUID and display name of each of the security role or teams that the user is associated with. This method is supported only on the Unified Interface.

### Syntax

`userSettings.roles`
 
### Return Value

**Type**: Collection

**Description**: Object containing `id` and `name` of each of the security role or teams that the user is associated with.

## securityRolePrivileges 

Returns an array of strings that represent the GUID values of each of the security role privilege that the user is associated with or any teams that the user is associated with.

### Syntax

`userSettings.securityRolePrivileges`

### Return Value

**Type**: Array

**Description**: GUID values of each of the security role privilege.

## securityRoles 

Returns an array of strings that represent the GUID values of each of the security role or teams that the user is associated with. 

Deprecated; use [userSettings.roles](#roles) instead to view the display names of security roles or teams along with the ID.

### Syntax

`userSettings.securityRoles`

### Return Value

**Type**: Array

**Description**: GUID values of each of the security role. For example:

`["0d3dd20a-17a6-e711-a94e-000d3a1a7a9b", "ff42d20a-17a6-e711-a94e-000d3a1a7a9b"]`

## transactionCurrency 

Returns a lookup object containing the ID, display name, and entity type of the transaction currency for the current user. This method is supported only on the Unified Interface.

### Syntax

`userSettings.transactionCurrency`

### Return Value

**Type**: Lookup object

**Description**: Object containing the `id`, `name`, and `entityType` of the transaction currency. For example:

`{id: "e7dd9bc6-d239-ea11-a813-000d3a35b14a", entityType: "transactioncurrency", name: "US Dollar"}`

## transactionCurrencyId 

Returns the transaction currency ID for the current user.

Deprecated; use [userSettings.transactionCurrency](#transactioncurrency) instead to access the display name along with the ID.

### Syntax

`userSettings.transactionCurrencyId`

### Return Value

**Type**: String

**Description**: Transaction currency ID.

## userId 

Returns the GUID of the **SystemUser.Id** value for the current user.

### Syntax

`userSettings.userId`

### Return Value

**Type**: String

**Description**: The ID of the user. For example:

`"{75B5BA27-FD41-4D45-8E3A-C8446C95F0CC}"`

## userName 

Returns the name of the current user.

### Syntax

`userSettings.userName`

### Return Value

**Type**: String

**Description**: Name of the current user.

## getTimeZoneOffsetMinutes method

Returns the difference in minutes between the local time and Coordinated Universal Time (UTC).

### Syntax

`userSettings.getTimeZoneOffsetMinutes()`

### Return Value

**Type**: number

**Description**: Time zone offset in minutes.

## Related topics

[Client context](client.md)

[Organization settings](organizationSettings.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)

