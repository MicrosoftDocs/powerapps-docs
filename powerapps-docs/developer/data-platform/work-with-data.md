---
title: "Work with data using code in Microsoft Dataverse (PowerApps) | Microsoft Docs" 
description: "Microsoft Dataverse provides web services and APIs that you can use to interact with your data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 03/24/2023
ms.reviewer: pehecke
ms.topic: article
author: divkamath # GitHub ID Temp owner
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Work with data using code in Microsoft Dataverse

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Dataverse has [tables](entities.md) that are used to model and manage business data. You can use the stock provided tables or define your own custom tables to store data.

Dataverse also has APIs known as *messages*. Messages define a set of input parameters and output properties to encapsulate logic that executes on the server. Each message has a name. If you come from a SQL database background, you can think of these like SQL stored procedures. You can use messages that Dataverse provides or you can create your own messages.

## Use web services to work with data

Dataverse provides two web services that you can use to interact with data: Web API, and Organization service, and one that you can use to search for data in Dataverse using it's native endpoint or Web API and the Organization service. Choose the one that best matches the requirement and your skills.

<!--![Flow diagram to choose web service.](media/whentousewebapi.png)-->

### Web API

The Web API is an OData v4 RESTful endpoint. Use the Web API for any programming language that supports HTTP requests and authentication using OAuth 2.0.

More information: [Use the Dataverse Web API](webapi/overview.md)

### Organization service

Use classes provided in the Dataverse SDK for .NET assemblies to access the Organization web service from custom apps, or for extending Dataverse operations using custom plug-ins and workflow activities. The Dataverse SDK for .NET supports build targets for both .NET Framework and .NET 6+. However, plug-in and custom workflow activities must be coded using .NET Framework.

More information: [Use the Dataverse Organization service](org-service/overview.md)

> [!NOTE]
> Use the Xrm.Tooling assemblies if you want to access the Organization service using our PowerShell module or are creating a Windows client application and you want to use our custom login control. More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)

## Limitations

There's a 1-GB size limitation on the size of a response that Dataverse returns.  Few APIs or queries are capable of returning this much data.  If you encounter this limit, you should consider what other options are available to get the data in multiple, smaller requests.

The deprecated SOAP endpoint returns serialized XML data that is much more verbose than the serialized JSON data returned by the Web API. If you're using the deprecated SOAP endpoint, you should use the Web API equivalent operation. More information: [About the legacy SOAP endpoint](org-service/overview.md#about-the-legacy-soap-endpoint)

### Search

Dataverse search delivers fast and comprehensive search results across multiple tables, in a single list, sorted by relevance. It also provides capabilities to support suggestions and autocompletion experiences in apps.

Search has a native endpoint and there are Dataverse messages that you can use from the Web API or Organization service.

More information: [Search for Dataverse records](search/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
