---
title: "Discovery Service (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about access to the Discovery Service for discovering business organization instance details."
ms.custom: ""
ms.date: 11/11/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Discovery Service

[!INCLUDE [cc-discovery-service-description](includes/cc-discovery-service-description.md)]


The Discovery Service is accessed through two different APIs:

- For the Web API: [Discover the URL for your organization using the Web API](webapi/discover-url-organization-web-api.md)
- For the Organization Service: [Use the Discovery Service with the Microsoft.Xrm.Sdk.Discovery NameSpace](org-service/discovery-service.md)

> [!NOTE]
> The legacy Discovery Service that was accessible via the 2011 SOAP endpoint has been deprecated along with the regional Discovery Service Web API endpoints. See [Important changes (deprecations)](/power-platform/important-changes-coming.md) for more details.

### See Also

[Use the Common Data Service Web API](webapi/overview.md)<br />
[Modify existing code to use Discovery Service Web API endpoint](discovery-orgsdk-to-webapi.md)
