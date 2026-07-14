---
title: "Use the Microsoft Dataverse Web API (Dataverse)| Microsoft Docs"
description: "The Microsoft Dataverse Web API implements the OData v4 protocol and provides a development experience that can be used across a wide variety of programming languages, platforms, and devices"
ms.date: 01/09/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: concept-article
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Use the Microsoft Dataverse Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

To work with data, as well as table and column definitions in Dataverse, you can use the Web API or [SDK for .NET](../org-service/overview.md).

The Dataverse Web API provides a development experience that you can use across a wide variety of programming languages, platforms, and devices. The Web API implements the OData (Open Data Protocol), version 4.0, an OASIS standard for building and consuming RESTful APIs over rich data sources. You can learn more about this protocol at [https://www.odata.org/](https://www.odata.org/). Details about this OASIS standard are available at [https://www.oasis-open.org/standards#odatav4.0](https://www.oasis-open.org/standards#odatav4.0). 


Because the Web API is built on open standards, other than the [Python SDK](../sdk-python/index.yml), Microsoft doesn't provide assemblies or libraries for a specific developer experience. You can compose HTTP requests for specific operations or use third-party libraries to generate classes for whatever language or platform you want. You can find a list of libraries that support OData version 4.0 at [https://www.odata.org/libraries/](https://www.odata.org/libraries/).

Model-driven applications and Power Pages provide objects with methods to perform data operations by using the Web API. See:

- [Xrm.WebApi (Client API reference)](../../model-driven-apps/clientapi/reference/xrm-webapi.md)
- [Portals Web API overview](/power-pages/configure/web-api-overview)

## Web API and the Organization service

It's valuable to recognize that the *organization service* is what defines the platform. The Web API provides a RESTful programming experience but ultimately all data operations go through the underlying organization service. The organization service defines the supported operations as messages. Each message has a name. These names are bound to the events used in the event framework to evaluate what registered extensions should be initiated. For more information, see [Event Framework](../event-framework.md).

The Web API allows you to do the same operations as the SDK for .NET but presents them in a RESTful style. OData v4 provides for named operations via *functions* or *actions*. Most messages available in the organization service are exposed as a corresponding named function or action. Messages that correspond to CRUD operations aren't available in the Web API. As a RESTful service, these operations have implementations that use `GET`, `POST`, `PATCH`, and `DELETE` HTTP methods. But within the platform, the *retrieve*, *create*, *update*, and *delete* messages are invoked in the same way the corresponding operations are performed by using the SDK for .NET assemblies.

## Getting started

You can use the Web API with any language that allows you to send authenticated HTTP requests. We prepared a few getting started experiences for four common scenarios:

### HTTP request tools

An application that you can use to compose and send authenticated HTTP requests is an essential tool. Many options are available, such as [Postman](https://www.postman.com/), [Bruno](https://www.usebruno.com/), or [curl](https://curl.se/). Choose and use whichever tool you like best. The following steps describe how to use [Insomnia](https://insomnia.rest/) because it has a graphical user interface, a relatively easy installation, and provides an option to opt out of creating an account. [Learn how to use Insomnia with Dataverse Web API](insomnia.md).

> [!TIP]
> Unless you already have a favorite HTTP request tool, you might find that using PowerShell with Visual Studio Code is as easy to get started and allows for powerful scripting capabilities as well.


### PowerShell developers

Using Web API with PowerShell is one of the easiest ways to get started. You can use the [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) to send requests and process the responses by using the [ConvertTo-Json cmdlet](/powershell/module/microsoft.powershell.utility/convertto-json).

You can find the following content about using PowerShell with Web API:

- [Quick Start Web API with PowerShell and Visual Studio Code](quick-start-ps.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](use-ps-and-vscode-web-api.md)
- [Web API Data operations Samples (PowerShell)](web-api-samples-powershell.md)


### JavaScript developers

JavaScript developers frequently use the Dataverse Web API with model-driven apps. Model-driven apps provide the [Xrm.WebApi](../../model-driven-apps/clientapi/reference/xrm-webapi.md) object that exposes methods to interact with the Web API. [Learn more about client-side JavaScript using Web API in model-driven apps](get-started-web-api-client-side-javascript.md).

Single Page Applications (SPAs) also use JavaScript and can connect to the Dataverse Web API. [Quickstart: Web API with client-side JavaScript and Visual Studio Code](quick-start-js-spa.md) describes how to connect to the Web API by using a SPA application pattern. You can find more samples in [Web API Data operations Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md).

Within Power Apps Component Framework (PCF) components, JavaScript developers use methods that are part of the [WebAPI](../../component-framework/reference/webapi.md) object to work with Dataverse data in PCF components.

Finally, Power Pages exposes a [Portals Web API](/power-pages/configure/web-api-overview) that offers a subset of Dataverse operations available using the Web API.

### .NET developers

.NET developers can use either the [Dataverse SDK for .NET](../org-service/overview.md) or the Web API. You might want to use the Web API when you don't want to take a dependency on a specific NuGet package or the requirements of your project don't require the strongly typed classes provided by the SDK for .NET.

To use Web API with C#, see these quick start articles:

- [Quick Start: Web API sample (C#)](quick-start-console-app-csharp.md)
- [Quickstart: Blazor Server Web API sample (C#)](quick-start-blazor-server-app.md)

For more C# Web API samples, see [Web API Data operations Samples (C#)](web-api-samples-csharp.md).


### Related Sections

[Work with data using code](../work-with-data.md)  
[OData - the best way to REST](https://www.odata.org/)  
[OData Version 4.0 Part 1: Protocol Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html)  
[OData Version 4.0 Part 2: URL Conventions Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part2-url-conventions.html)  
[OData Version 4.0 Part 3: Common Schema Definition Language (CSDL) Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part3-csdl.html)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
