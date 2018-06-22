---
title: "getClientUrl (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getClientUrl (Client API reference)



Returns the base URL that was used to access the application.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getClientUrl();
``` 

## Return Value

**Type**: String

**Description**: The values returned will resemble those listed in the following table.

|Value |Client |
|---|---|
|https://[org].crm.dynamics.com|Dynamics 365 Customer Engagement (online)|
|http(s)://[server]/[org]|Dynamics 365 Customer Engagement (on-premises)|
|http://localhost:2525|Dynamics 365 Customer Engagement for Outlook with Offline Access when offline|

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)





