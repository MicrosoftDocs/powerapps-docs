---
title: "Discovery Service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about accessing the Discovery service for discovering environment details."
ms.custom: ""
ms.date: 03/23/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Discovery service

[!INCLUDE [cc-discovery-service-description](includes/cc-discovery-service-description.md)]

The Discovery service is accessed through two different APIs:

- For the OData V4 RESTful API: [Discover the URL for your organization](webapi/discover-url-organization-web-api.md)
- For the discovery API available through the 2011 (SOAP) endpoint: [Use the Discovery service with the Microsoft.Xrm.Sdk.Discovery NameSpace](org-service/discovery-service.md)

> [!NOTE]
> The *regional* Discovery service is deprecated. More information: [Important changes (deprecations)](/power-platform/important-changes-coming.md).

### See Also

[Use the Microsoft Dataverse Web API](webapi/overview.md)<br />
[Modify your code to use global Discovery service](webapi/discovery-orgsdk-to-webapi.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]