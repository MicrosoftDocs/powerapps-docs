---
title: "Use the Common Data Service Web API (Common Data Service)| Microsoft Docs"
description: "The Common Data Service Web API implements OData v4 and provides a development experience that can be used across a wide variety of programming languages, platforms, and devices"
ms.custom: ""
ms.date: 04/22/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 15c4039e-a3ca-4116-ba1d-3ac88cba3ae1
caps.latest.revision: 15
author: "JimDaly" # GitHub ID
ms.author: "susikka"
ms.reviewer: "pehecke"
manager: "shujoshi"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use the Common Data Service Web API

The Web API is one of two web services you can use to work with data and metadata in Common Data Service. The other is the [Organization Service](../org-service/overview.md).

The Common Data Service Web API provides a development experience that can be used across a wide variety of programming languages, platforms, and devices. The Web API implements the OData (Open Data Protocol), version 4.0, an OASIS standard for building and consuming RESTful APIs over rich data sources. You can learn more about this protocol at [https://www.odata.org/](https://www.odata.org/). Details about this standard are available at [https://www.oasis-open.org/standards#odatav4.0](https://www.oasis-open.org/standards#odatav4.0). 


Because the Web API is built on open standards, we don’t provide assemblies for a specific developer experience. You can compose HTTP requests for specific operations or use third-party libraries to generate classes for whatever language or platform you want. You can find a list of libraries that support OData version 4.0 at [https://www.odata.org/libraries/](https://www.odata.org/libraries/).  

## Web API and the Organization service

It is valuable to recognize that the organization service is what defines the platform. The Web API provides a RESTful programming experience but ultimately all data operations go through the underlying organization service. The organization service defines the supported operations as messages. Each message has a name. These names are bound to the events used in the event framework to evaluate what registered extensions should be initiated. More information: [Event Framework](../event-framework.md)

The Web API allows you to do all the same operations as the organization service but presents them in an RESTful style. OData v4 provides for named operations via *functions* or *actions*. Most messages available in the organization service are exposed as a corresponding named function or action. Those messages that correspond to CRUD operations are not available in the Web API because as a RESTful service they have implementations using GET, POST, PATCH, and DELETE HTTP methods, but within the platform the *retrieve*, *create*, *update*, and *delete* messages are invoked just as they are when the corresponding operations are performed using the .NET Framework assemblies.

  
### Related Sections

[Work with data using code](../work-with-data-cds.md)<br />
[OData - the best way to REST](https://www.odata.org/)<br />
[OData Version 4.0 Part 1: Protocol Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html)<br />
[OData Version 4.0 Part 2: URL Conventions Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part2-url-conventions.html)<br />
[OData Version 4.0 Part 3: Common Schema Definition Language (CSDL) Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part3-csdl.html)
