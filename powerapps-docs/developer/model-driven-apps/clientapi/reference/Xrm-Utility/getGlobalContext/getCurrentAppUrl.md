---
title: "getCurrentAppUrl (Client API reference)"
description: Includes description and supported parameters for the getCurrentAppUrl method.
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
# getCurrentAppUrl (Client API reference)

Returns the URL of the current business app in model-driven apps.

> [!NOTE]
> In mobile client, this method returns null value.
 
## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getCurrentAppUrl();
``` 

## Return Value

**Type**: String

**Description**: URL of the current business app. Possible return values:

|Value |Client |
|---|---|
|`https://[org].crm.dynamics.com/main.aspx?appid=[GUID]`|model-driven apps (online)|
|`https://[server]/[org]/main.aspx?appid=[GUID]`|model-driven apps (on-premises)|

### Related articles

[Create, manage, and publish model-driven apps using code](../../../../create-manage-model-driven-apps-using-code.md)   
[Xrm.Utility.getGlobalContext](../getGlobalContext.md) 

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
