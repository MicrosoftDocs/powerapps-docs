---
title: "Microsoft Dataverse Web API Types and Operations"
description: "Learn how to find information from Dataverse Web API service and metadata documents, including system entity types, functions, and actions for developers."
ms.date: 03/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Web API types and operations

The articles in this section help you understand the Dataverse Web API by introducing important concepts and showing you ways to get the information you need by understanding the service documents.

Like the [Microsoft Graph API](/graph/use-the-api), Dataverse Web API is an OData RESTful service. Unlike the Microsoft Graph API, each environment has a different organization URL and includes custom tables and operations that can be unique to each environment. Each environment is different because of the unique set of customizations or solutions installed.

## First steps

The first thing you should do is look at the service documents for a Dataverse environment you can access. For this step, you need to know the URL for your environment. Then, set up some ways to manage authenticating to the service to view service documents.

### Find the Web API endpoint URL

Use the instructions in [View developer resources](../view-download-developer-resources.md) to identify a Web API endpoint for an environment you can access. It should look something like this: `https://yourorg.api.crm.dynamics.com/api/data/v9.2`.

## Authenticate to the service

Several ways exist to authenticate to interact with the service. Insomnia is a popular choice with wide adoption. You can also use PowerShell with Visual Studio Code.

Use either method to retrieve the service documents and see examples showing how the information in the articles in this section applies to your environment. You can also perform any other operation to try the capabilities of the Web API.

### Set up an Insomnia environment

[Insomnia API client](https://docs.insomnia.rest/insomnia/get-started) provides a great way to connect to your environments and explore the Dataverse Web API. Insomnia can greatly simplify managing getting an access token when using Dataverse Web API.

Use the steps in [Use Insomnia with Dataverse Web API](insomnia.md).


### Use PowerShell with Visual Studio Code

To authenticate to the service, use the steps in [Quick Start Web API with PowerShell and Visual Studio Code](quick-start-ps.md). [Use PowerShell and Visual Studio Code with the Dataverse Web API](use-ps-and-vscode-web-api.md) expands on the quick start to describe more advanced ways to interact with Dataverse Web API. The [Download the Dataverse Web API CSDL $metadata document](use-ps-and-vscode-web-api.md#download-the-dataverse-web-api-csdl-metadata-document) section contains a script to download the CSDL $metadata document.

## OData v4.0 standard

The articles in this section summarize information relevant to Dataverse Web API implementation of the OData v4.0 standard. A service that implements OData must follow the standards set in the specification, but isn't required to implement all parts of the specification.

For more information, see these documents:

- [OData Version 4.0. Part 1: Protocol Plus Errata 03](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html)
- [OData Version 4.0. Part 2: URL Conventions Plus Errata 03](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part2-url-conventions.html)
- [OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part3-csdl.html)
- [OData JSON Format Version 4.0](https://docs.oasis-open.org/odata/odata-json-format/v4.0/os/odata-json-format-v4.0-os.html)

## Next steps

Learn about the Web API service documents.

> [!div class="nextstepaction"]
> [Service Documents](web-api-service-documents.md)


### See also  

[Web API Service Documents](web-api-service-documents.md)   
[Web API EntityTypes](web-api-entitytypes.md)    
[Web API Properties](web-api-properties.md)    
[Web API Navigation Properties](web-api-navigation-properties.md)    
[Web API Actions](web-api-actions.md)    
[Web API Functions](web-api-functions.md)    
[Web API Complex and Enumeration types](web-api-complex-enum-types.md)    
[Use the Dataverse Web API](overview.md)    
[Authenticate to Dataverse with the Web API](authenticate-web-api.md)    
[Perform operations using the Web API](perform-operations-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
