---
title: "getClientUrl (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
|https://[org].crm.dynamics.com|model-driven apps (online)|
|http(s)://[server]/[org]|model-driven apps (on-premises)|
|https://localhost:2525|model-driven apps for Outlook with Offline Access when offline|

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)





