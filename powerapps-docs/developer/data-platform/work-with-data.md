---
title: "Work with data using code in Microsoft Dataverse (PowerApps) | Microsoft Docs" 
description: "Microsoft Dataverse provides web services and APIs that you can use to interact with your data."
ms.date: 05/14/2024
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

Use Dataverse tables to model and manage business data. You can use [existing tables](reference/about-entity-reference.md) and customize them, or [create your own custom tables](../../maker/data-platform/create-edit-entities-portal.md) to store data.

Dataverse also has APIs known as *messages*. Each message has a name like `Create`, `Delete`, or `WhoAmI`. Messages define a set of input parameters and output properties to encapsulate logic that executes on the server.  If you come from a SQL database background, you can think of these like SQL stored procedures. You can use messages that Dataverse provides or you can [create your own messages](custom-actions.md).

Dataverse provides two ways to work with data: Web API & SDK for .NET. Choose the one that best matches the requirements, your skills, and your preferences.

<!--![Flow diagram to choose web service.](media/whentousewebapi.png)-->
:::image type="content" source="media/whentousewebapi.svg" alt-text="Flow diagram to choose programming style":::

## Web API

The Dataverse Web API is an OData v4 RESTful endpoint. Use the Web API for any programming language that supports HTTP requests and authentication using OAuth 2.0.

More information: [Use the Dataverse Web API](webapi/overview.md)

## SDK for .NET

Use classes provided in the Dataverse SDK for .NET assemblies for custom apps, or for extending Dataverse operations using custom plug-ins and workflow activities. The Dataverse SDK for .NET supports build targets for both .NET Framework and .NET 6+. However, plug-in and custom workflow activities must be coded using .NET Framework.

More information: [Use the Dataverse SDK for .NET](org-service/overview.md)

> [!NOTE]
> Use the Xrm.Tooling assemblies if you want to use the SDK for .NET using our PowerShell module or are creating a Windows client application and you want to use our custom login control. More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)

## Search

Dataverse search delivers fast and comprehensive search results across multiple tables, in a single list, sorted by relevance. It also provides capabilities to support suggestions and autocompletion experiences in apps.

Search has a native endpoint and there are Dataverse messages that you can use from the Web API or Organization service.

More information: [Search for Dataverse records](search/overview.md)

## Limitations

There's a 1-GB size limitation on the size of a response that Dataverse returns.  Few APIs or queries are capable of returning this much data.  If you encounter this limit, you should consider what other options are available to get the data in multiple, smaller requests.

The deprecated SOAP endpoint returns serialized XML data that is much more verbose than the serialized JSON data returned by the Web API. If you're using the deprecated SOAP endpoint, you should use the Web API equivalent operation. More information: [About the legacy SOAP endpoint](org-service/overview.md#about-the-legacy-soap-endpoint)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
