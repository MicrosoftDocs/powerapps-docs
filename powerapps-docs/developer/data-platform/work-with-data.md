---
title: "Work with data using code in Microsoft Dataverse (PowerApps) | Microsoft Docs" 
description: "Microsoft Dataverse provides web services and APIs that you can use to interact with your data."
ms.date: 11/18/2025
ms.reviewer: pehecke
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Work with data using code in Microsoft Dataverse

There are several different ways to access Dataverse data using code.

- Use the Dataverse [SDK for .NET](#sdk-for-net), [SDK for Python](./sdk-python/), or [Web API](#web-api) to retrieve, add, and modify data.
- Use [Dataverse search](#search-dataverse-data) search Dataverse data.
- Use the Dataverse Tabular Data Stream (TDS) endpoint to [query data with SQL](#query-data-with-sql).

This article introduces the options you have to work with Dataverse data using code.

<!-- 
Use Dataverse tables to model and manage business data. You can use [existing tables](reference/about-entity-reference.md) and customize them, or [create your own custom tables](../../maker/data-platform/create-edit-entities-portal.md) to store data.

Dataverse also has APIs known as *messages*. Each message has a name like `Create`, `Delete`, or `WhoAmI`. Messages define a set of input parameters and output properties to encapsulate logic that executes on the server.  If you come from a SQL database background, you can think of these like SQL stored procedures. You can use messages that Dataverse provides or you can [create your own messages](custom-actions.md). 
-->

## Retrieve, add, and modify data

Dataverse provides two ways to retrieve, add, and modify data: SDK for .NET & Web API. Choose the one that best matches the requirements, your skills, and preferences.

:::image type="content" source="media/whentousewebapi.svg" alt-text="Flow diagram to choose programming style":::

### SDK for .NET

If you are working with .NET, we recommend using our [SDK for .NET](org-service/overview.md).

- Use the [ServiceClient class](/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient) in the [DataverseServiceClient NuGet package](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) if you have a client application.
- Use the [Microsoft.CrmSdk.CoreAssemblies NuGet package](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) when you're writing a plug-in or custom workflow activity.

The Dataverse SDK for .NET supports build targets for both .NET Framework and .NET 6+. However, plug-in and custom workflow activities must use .NET Framework.

If you're using our [PowerShell module](https://www.powershellgallery.com/packages/Microsoft.Xrm.Tooling.CrmConnector.PowerShell/) or using our [custom log-in control](xrm-tooling/use-xrm-tooling-common-login-control-client-applications.md) with a Windows client application, use the [the Xrm.Tooling](xrm-tooling/build-windows-client-applications-xrm-tools.md)

- [Use the SDK for .NET](org-service/overview.md)
- [Quickstart: Execute an SDK for .NET request (C#)](org-service/quick-start-org-service-console-app.md)

### SDK for Python

If you are working with Python, we recommend using our [SDK for Python](./sdk-python/). The SDK enables data scientists and developers to create, access, and manager Dataverse business data using Python programming. The Dataverse SDK for Python implements common Python programming paradigms and best practices, provides a more natural Python interface to Dataverse, and supports community contributions.

### Web API

The Dataverse Web API is an OData v4 RESTful endpoint. Use the Web API for any programming language that supports HTTP requests and authentication using OAuth 2.0, including .NET.

- [Learn to use the Dataverse Web API](webapi/overview.md)
- [Quick Start: Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [Quick Start: Web API sample (C#)](webapi/quick-start-console-app-csharp.md)

## Search Dataverse data

Dataverse search delivers fast and comprehensive search results across multiple tables, in a single list, sorted by relevance. It also provides capabilities to support suggestions and autocompletion experiences in apps.

Search has a native endpoint and there are Dataverse messages that you can use from the Web API or SDK for .NET.

[Learn to search for Dataverse records](search/overview.md)

## Query data with SQL

The [Power Query Dataverse connector](/power-query/connectors/dataverse) uses the Dataverse Tabular Data Stream (TDS) endpoint to retrieve data using [Dataverse SQL](how-dataverse-sql-differs-from-transact-sql.md), a subset of Transact-SQL.

[Retrieving data using SQL Management Studio (SSMS)](dataverse-sql-query.md#sql-server-management-studio-preview) is a preview feature.

[Learn to use SQL to query data](dataverse-sql-query.md)

## Request and Response payload size limitations

The maximum payload size for any request sent to Dataverse is 128 MB. Requests with payloads over this limit receive a [413 Payload Too Large](https://devdoc.net/web/developer.mozilla.org/docs/Web/HTTP/Status/413.html) HTTP status code in the response.

There's a 1-GB size limitation on the size of a response that Dataverse returns. Few APIs or queries are capable of returning this much data.  If you encounter this limit, you should consider what other options are available to get the data in multiple, smaller requests.

The deprecated SOAP endpoint payloads use serialized XML data that is much more verbose than the serialized JSON data payloads the Web API uses. You're less likely to encounter errors where the request or response payload is too large when you use the Web API. [Learn about the legacy SOAP endpoint](org-service/overview.md#about-the-legacy-soap-endpoint)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
