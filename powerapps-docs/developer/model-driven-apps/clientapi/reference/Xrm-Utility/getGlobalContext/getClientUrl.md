---
title: "getClientUrl (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getClientUrl method.
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
|`https://[org].crm.dynamics.com`|model-driven apps (online)|
|`http(s)://[server]/[org]`|model-driven apps (on-premises)|
|`https://localhost:2525`|model-driven apps for Outlook with Offline Access when offline|

### Related articles

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)   
[Web API RetrieveCurrentOrganization function](xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganization)   
[SDK for .NET RetrieveCurrentOrganizationRequest class](xref:Microsoft.Crm.Sdk.Messages.RetrieveCurrentOrganizationRequest)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
