---
title: "getGlobalContext.userSettings (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 44296667-f1cd-49be-a300-7259bc3b41e0
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getGlobalContext.userSettings (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns information about the current user settings.

`var userSettings = Xrm.Utility.getGlobalContext().userSettings`

The **userSettings** object provides following properties and a method.

## dateFormattingInfo 

Returns the date formatting information for the current user.

### Syntax

`userSettings.dateFormattingInfo`

### Return Value

**Type**: Object

**Description**: An object with informatiuon about date formatting such as **FirstDayOfWeek**, **LongDatePattern**, **MonthDayPattern**, **TimeSeparator**, and so on.

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

## securityRolePrivileges 

Returns an array of strings that represent the GUID values of each of the security role privilege that the user is associated with or any teams that the user is associated with.

### Syntax

`userSettings.securityRolePrivileges`

### Return Value

**Type**: Array

**Description**: GUID values of each of the security role privilege.

## securityRoles 

Returns an array of strings that represent the GUID values of each of the security role that the user is associated with or any teams that the user is associated with.

### Syntax

`userSettings.securityRoles`

### Return Value

**Type**: Array

**Description**: GUID values of each of the security role. For example:

`["0d3dd20a-17a6-e711-a94e-000d3a1a7a9b", "ff42d20a-17a6-e711-a94e-000d3a1a7a9b"]`

## transactionCurrencyId 

Returns the transaction currency ID for the current user.

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

