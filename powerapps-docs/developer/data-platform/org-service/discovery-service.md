---
title: "Use the Discovery Service with the SDK Assemblies (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to use the Discovery Service with the APIs available in the Microsoft Dataverse SDK assemblies." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 03/22/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "ImadYanni" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
---

# Use the Discovery Service with the SDK Assemblies

> [!IMPORTANT]
> Effective March 2, 2020, the *regional* Discovery Service will be [deprecated](/power-platform/important-changes-coming#regional-discovery-service-is-deprecated).
>
> For information on how to transition to use the *global* Discovery Service, see [Modify your code to use global Discovery Service](../webapi/discovery-orgsdk-to-webapi.md).

You can create a client for a specific Microsoft Dataverse environment and not provide the user any options about which environment they can connect with. Only valid users for that specific environment can use your client.

If you want people using your client to be able to connect to any Dataverse environment they have access to you could prompt them to enter the URL for their environment, but this is not recommended. Each user may have access to multiple Dataverse environments. Users may not know or remember the URL for their environment. Expecting people to enter this URL is bound to frustrate users. 

Instead, your client should provide a list of each of the available environments based on the user's credentials. If there is more than one environment available, your application should prompt the user to choose which environment they want to connect with.

With Dataverse, server and organization allocation may change as part of datacenter management and load balancing. Therefore, a discovery service provides a way to discover which server is serving an instance at a given time.

 - Regional Discovery Services are no longer available.
 - To access Global Discovery functionality with the SDK going foward, see [Sample: Access the Discovery service](/powerapps/developer/data-platform/org-service/samples/access-discovery-service)

## Global Discovery Service Endpoints:
[!INCLUDE [global-discovery-services](../../../includes/global-discovery-services.md)]

### See also

[Global Discovery Service Sample](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/DiscoveryService)<br />
[Discover the URL for your organization](../webapi/discover-url-organization-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
