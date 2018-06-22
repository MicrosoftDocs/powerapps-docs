---
title: "getCurrentAppUrl (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getCurrentAppUrl (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns the URL of the current business app in Customer Engagement.

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
|https://[org].crm.dynamics.com/main.aspx?appid=[GUID]|Dynamics 365 Customer Engagement (online)|
|https://[server]/[org]/main.aspx?appid=[GUID]|Dynamics 365 Customer Engagement (on-premises)|

### Related topics

[Create and manage custom business apps using code](../../../../create-manage-custom-business-apps-using-code.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md) 



