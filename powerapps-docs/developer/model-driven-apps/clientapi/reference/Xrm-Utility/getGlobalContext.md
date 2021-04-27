---
title: "getGlobalContext (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getGlobalContext method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getGlobalContext (Client API reference)



[!INCLUDE[./includes/getGlobalContext-description.md](./includes/getGlobalContext-description.md)]
The method provides access to the global context without going through the form context. It contains an equivalent of all the methods available for the **Xrm.Page.context** object (now deprecated) to retrieve information specific to the client, organization or user.

> [!IMPORTANT]
> To access the global context information in a standalone HTML Web resource, you should include a reference to **ClientGlobalContext.js.aspx** in the web resource, and then use the **GetGlobalContext** function. More information: [GetGlobalContext function and ClientGlobalContext.js.aspx](../GetGlobalContext-ClientGlobalContext.js.aspx.md) 

## Properties of Global Context (getGlobalContext)

Use the following properties of global context to return information about the client, organization settings, or user settings:

|Property |Description | 
|---|---|
|[client](getGlobalContext/client.md) | Returns information about the client.|
|[organizationSettings](getGlobalContext/organizationSettings.md) | Returns information about the current organization settings.|
|[userSettings](getGlobalContext/userSettings.md) | Returns information about the current user settings.|


## Methods of Global Context (getGlobalContext)

|Method |Description |
|---|---|
|[getAdvancedConfigSetting](getGlobalContext/getAdvancedConfigSetting.md) |Returns information about the advanced configuration settings for the organization.|
|[getClientUrl](getGlobalContext/getClientUrl.md) |Returns the base URL that was used to access the application.|
|[getCurrentAppName](getGlobalContext/getCurrentAppName.md) |Returns the name of the current business app in model-driven apps.|
|[getCurrentAppProperties](getGlobalContext/getCurrentAppProperties.md) |Returns the properties of the current business app in model-driven apps.|
|[getCurrentAppUrl](getGlobalContext/getCurrentAppUrl.md) |Returns the URL of the current business app in model-driven apps.|
|[getVersion](getGlobalContext/getVersion.md) |Returns the version number of the model-driven apps instance.|
|[getWebResourceUrl](getGlobalContext/getWebResourceUrl.md) |Returns the relative URL with the caching token for the specified web resource.|
|[isOnPremises](getGlobalContext/isOnPremises.md) |Returns a boolean value indicating if the model-driven apps instance is hosted on-premises or online.|
|[prependOrgName](getGlobalContext/prependOrgName.md) |Prefixes the current organization's unique name to a string, typically a URL path.|




 





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]