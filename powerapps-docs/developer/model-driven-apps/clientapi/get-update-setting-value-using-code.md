---
title: "Get or update setting value using client API "
description: "Get or update setting value using client API."
Keywords: settings, settings environment value, settings app value, model-driven app
ms.subservice: dataverse-developer
author: sriharibs-msft
ms.author: srihas
ms.date: 02/04/2024
ms.reviewer: jdaly
ms.topic: how-to
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Get or update a setting value using client API

Settings are solution components that enable developers to quickly configure apps to provide a customized experience. Settings can be used to enable or disable features or configure feature behavior for a single app or all apps within an environment. More information: [Use settings to provide customized app experiences](../../../maker/data-platform/create-edit-configure-settings.md)

The following functions can be used to get or update a setting value using client API.

## getCurrentAppSetting

Gets the value of a setting for the current app.

### Syntax

```JavaScript
var settingValue = Xrm.Utility.getGlobalContext().getCurrentAppSetting(settingName);
```

### Parameters

| Name | Type | Required | Description |
|:--------------|:--------------|:--------------|:-------------------------|
|`settingName` | String | Yes | The name of the setting to get the value for. |

### Return value

**Type:** Same as the type of the setting: *Number*, *String*, or *Yes/No*<br><br>
**Description:**

- If the setting is **Overridable**:

  - When **Value can be overridden** is set to **Environment and app**, the setting app value is returned.
  
    - If a setting app value does not exist, then the setting environment value is returned.
    - If a setting environment value does not exist, the default value as specified in the setting definition is returned.
   
  - When **Value can be overridden** is set to **Environment only**, the setting environment value is returned.
   
    - If a setting environment value does not exist, the default value as specified in the setting definition is returned.
   
  - When **Value can be overridden** is set to **App only**, the setting app value is returned.
  
    - If a setting app value does not exist, the default value as specified in the setting definition is returned.

- If the setting is not **Overridable**, the default value as specified in the setting definition is returned.
- If the setting name is incorrect or the setting could not be found, the return value is null.

## saveSettingValue

Adds or updates the setting app value for the current app or the setting environment value for the current environment.

### Syntax

```JavaScript
var appOverrideScope = 2; // Add or update a setting app value
var saveSettingOptions = {overrideScope: appOverrideScope, solutionUniqueName: mySolutionName};
Xrm.Utility.getGlobalContext().saveSettingValue(settingName, value, saveSettingOptions).then(successCallback, errorCallback);
```

### Parameters

| Name | Type | Required | Description |
|:--------------|:--------------|:--------------|:-------------------------|
|`settingName` | String | Yes | The name of the setting to update the value of. |
|`value` | *Number*, *String*, or *Yes/No* | Yes | The value to update the setting to. |
|`saveSettingOptions` | String | No | Options when updating the value. It contains two parameters <ul><li><b>overrideScope</b><ul><li>Use **1** to add or update a setting environment value</li><li>Use **2** to add or update a setting app value.</li><li>If not specified it is set to environment.</li></ul></li><li><b>solutionUniqueName</b><ul><li>The solution to which the setting environment value or setting app value should be added.</li><li>If not specified the default solution is used.</li></ul></li></ul>|
|`successCallback` | String | Yes | A function to call if the update is successful. |
|`errorCallback`| String | Yes | A function to call if the update fails. |

### Return value

On success, returns a promise object.

## Web APIs

You can also use the following Web APIs to get or update a setting value

- [RetrieveSetting function](xref:Microsoft.Dynamics.CRM.RetrieveSetting)
- [SaveSettingValue action](xref:Microsoft.Dynamics.CRM.SaveSettingValue)

### Related articles

[Solutions overview](../../../maker/data-platform/solutions-overview.md)   
[Use settings to provide customized app experiences](../../../maker/data-platform/create-edit-configure-settings.md)
