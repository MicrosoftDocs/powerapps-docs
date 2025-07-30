---
title: "getGlobalContext.userSettings (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getGlobalContext.UserSettings method.
author: sriharibs-msft
ms.author: srihas
ms.date: 09/25/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# getGlobalContext.userSettings (Client API reference)

Returns information about the current user settings.

`var userSettings = Xrm.Utility.getGlobalContext().userSettings`

## Properties

The `userSettings` object has the following properties:


|Name|Type|Description|
|---------|---------|---------|
|`dateFormattingInfo`|object|Returns the date formatting information for the current user. See [dateFormattingInfo](#dateformattinginfo)|
|`defaultDashboardId`|string|Returns the ID of the default dashboard for the current user.|
|`isGuidedHelpEnabled`|bool|Whether guided help is enabled for the current user.|
|`isHighContrastEnabled`|bool|Whether high contrast is enabled for the current user.|
|`isRTL`|bool|Whether the language for the current user is a right-to-left (RTL) language.|
|`languageId`|number|The [LCID language code](/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a) for the current user.|
|`roles`|collection|A collection of lookup objects containing the GUID and display name of each of the security role assigned to the user and any security roles assigned to the team that the user is associated with. See [roles](#roles)|
|`securityRolePrivileges`|string[]|an array of strings that represent the GUID values of each of the security role privilege that the user is associated with or any teams that the user is associated with.|
|`securityRoles`|string[]|Deprecated. Use the `roles` property.|
|`transactionCurrency`|object|Object containing the `id`, `name`, and `entityType` of the transaction currency for the current user. See [transactionCurrency](#transactioncurrency)|
|`transactionCurrencyId`|string|Deprecated. Use the `transactionCurrency` property|
|`userId`|string|The [systemuser.systemuserid](../../../../../data-platform/reference/entities/systemuser.md#BKMK_SystemUserId) value of the current user.|
|`userName`|string|The name of the current user.|


### dateFormattingInfo

An object with string properties about date formatting such as `FirstDayOfWeek`, `LongDatePattern`, `MonthDayPattern`, `TimeSeparator`, and so on.

### roles

The collection contains objects with `id` and `name` properties for each of the security roles or teams that the user is associated with.

This property is supported only on Unified Interface.

### transactionCurrency

This method is supported only on Unified Interface.

The data might look something like this:

`{id: "e7dd9bc6-d239-ea11-a813-000d3a35b14a", entityType: "transactioncurrency", name: "US Dollar"}`


## Methods

The `userSettings` object has the following methods:

### getSecurityRolePrivilegesInfo method

Returns a promise which resolves with an object whose keys are the security role privilege GUIDs and values are objects containing the `businessUnitId`, `depth`, and `privilegeName` of the security role privilege.

#### Syntax

`userSettings.getSecurityRolePrivilegesInfo().then(successCallback, errorCallback);`

#### Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`successCallback`|Function|No|A function to call when the security role privileges information is retrieved. A dictionary will be passed to the success callback where the security role privilege GUIDs will be the keys and the values will be objects containing the following properties:<br />`id`: String. The security role privilege GUID.<br />`businessUnitId`: String. The GUID of the business unit of the security role privilege.<br />`privilegeName`: String. The security role privilege name.<br />`depth`: String. The security role privilege depth.|
|`errorCallback`|Function|No|A function to call when the operation fails. An object with the following properties will be passed:<br />`errorCode`: Number. The error code.<br />`message`: String. An error message describing the issue.|

#### Return Value

**Type**: `Promise<{[key: string]: {id: string, businessUnitId: string, privilegeName: string, depth: number}}>`

On success, returns a promise object containing the values specified in the description of the **successCallback** parameter above.

**Description**: GUID and additional details like Business Unit and Privilege Name of each of the security role privileges.

#### getSecurityRolePrivilegesInfo example

```javascript
userSettings
  .getSecurityRolePrivilegesInfo()
  .then(function success(rolePrivileges) {
    var privilegeGuids = Object.keys(rolePrivileges);
    console.log("Privileges Count: " + privilegeGuids.length);

    // Print information about the first role privilege in the dictionary
    var guid = privilegeGuids[0];
    console.log("Privilege Id: " + rolePrivileges[guid].id);
    console.log("Privilege Name: " + rolePrivileges[guid].privilegeName);
    console.log("Privilege Business Unit Id: " + rolePrivileges[guid].businessUnitId);
    console.log("Privilege depth: " + rolePrivileges[guid].depth);
  });
```

### getTimeZoneOffsetMinutes method

Returns the difference in minutes between the local time and Coordinated Universal Time (UTC).

#### Syntax

`userSettings.getTimeZoneOffsetMinutes()`

#### Return Value

**Type**: number

**Description**: Time zone offset in minutes.

### Related articles

[Client context](client.md)   
[Organization settings](organizationSettings.md)   
[Xrm.Utility.getGlobalContext](../getGlobalContext.md)   
[User Settings (UserSettings) table](../../../../../data-platform/reference/entities/usersettings.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
