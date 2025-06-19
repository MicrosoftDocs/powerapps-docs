---
title: "getAdvancedConfigSetting (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getAdvancedConfigSettings method.
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
# getAdvancedConfigSetting (Client API reference)



Returns information about the advanced configuration settings for the organization. 

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getAdvancedConfigSetting(setting);
```

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|`setting` |String |Yes |Name of the configuration setting. <br/>Only the following two configuration settings are supported: **"MaxChildIncidentNumber"** and **"MaxIncidentMergeNumber"** |

## Return Value

Returns the advanced configuration setting value.

### Related articles

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
