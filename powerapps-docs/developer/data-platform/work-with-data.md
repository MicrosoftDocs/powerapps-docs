---
title: "Work with data using code in Microsoft Dataverse (PowerApps) | Microsoft Docs" 
description: "Microsoft Dataverse provides web services and APIs that you can use to interact with your data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/14/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "divka78" # GitHub ID Temp owner
ms.subservice: dataverse-developer
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
# Work with data using code in Microsoft Dataverse

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Dataverse has [tables](entities.md) that are used to model and manage business data. You can use the stock provided tables or define your own custom tables to store data.

## Use web services to work with data

Dataverse provides two web services that you can use to interact with data: Web API, and Organization service, and one that you can use to search for data in Dataverse. Choose the one that best matches the requirement and your skills. [Search for Dataverse records](search/overview.md)

![Flow diagram to choose web service.](media/whentousewebapi.png)

### Web API

The Web API is an OData v4 RESTful endpoint. Use this for any programming language that supports HTTP requests and authentication using OAuth 2.0.

More information: [Use the Dataverse Web API](webapi/overview.md) 

### Organization service

Use the .NET Framework SDK assemblies for projects that involve writing plug-ins or workflow extensions.

More information: [Use the Dataverse Organization service](org-service/overview.md)

> [!NOTE]
> Use the Xrm.Tooling assemblies if you are creating a Windows client application. More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)

### Search

Dataverse search delivers fast and comprehensive search results across multiple tables, in a single list, sorted by relevance. It also provides capabilities to support suggestions and autocompletion experiences in apps.

More information: [Search for Dataverse records](search/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]