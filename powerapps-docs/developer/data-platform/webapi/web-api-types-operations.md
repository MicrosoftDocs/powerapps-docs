---
title: "Web API types and operations (Microsoft Dataverse)| Microsoft Docs"
description: "Describes how you can find information you need from the Web API service and metadata documents, including documentation of the Web API system entity types, functions, and actions"
ms.custom: ""
ms.date: 11/24/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)" 
ms.assetid: d80cfb87-d4f1-4c75-bcc8-4f54d1351e26
caps.latest.revision: 27
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API types and operations

The topics in this area will help you understand the Dataverse Web API by introducing important concepts and showing you ways to get the information you will need by understanding the service documents.

Like the [Microsoft Graph API](/graph/use-the-api), Dataverse Web API is an OData RESTful service. Unlike the Microsoft Graph API, each environment has a different organization URL and includes custom tables and operations that can be unique to each environment. Each environment is different because of the unique set of customizations or solutions installed.

## First steps

The first thing you should do is look at the service documents for a Dataverse environment you can access. For this you will need to know the URL for your environment. Then, we recommend that you set up a Postman environment to manage authenticating to the service to view service documents.

### Find the Web API endpoint URL

Use the instructions in [View developer resources](../view-download-developer-resources.md) to identify a Web API endpoint for an environment you can access. It should look something like this: `https://yourorg.api.crm.dynamics.com/api/data/v9.2`.

### Set up a Postman environment

Because you must authenticate to view data about service documents, [Postman API client](https://learning.postman.com/docs/getting-started/introduction/) provides a great way to connect to your environments and explore the Dataverse Web API. Postman can greatly simplify managing getting an access token when using Dataverse Web API.

Use the steps in [Set up a Postman environment](setup-postman-environment.md) and watch this video [Get started using Postman with Microsoft Dataverse Web API](https://youtu.be/HpUj11yU0fY).

With Postman API Client, you can easily retrieve the service documents and see examples showing how the information in the topics in this section applies to your environment. Postman API Client also helps you perform any other kind of operation to try the capabilities of the Web API.

## OData v4.0 standard

The topics in this section summarize information relevant to Dataverse Web API implementation of the OData v4.0 standard. A service that implements OData must follow the standards set in the specification, but is not required to implement all parts of the specification.

For more information, see these documents:

- [OData Version 4.0. Part 1: Protocol Plus Errata 03](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html)
- [OData Version 4.0. Part 2: URL Conventions Plus Errata 03](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part2-url-conventions.html)
- [OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part3-csdl.html)
- [OData JSON Format Version 4.0](https://docs.oasis-open.org/odata/odata-json-format/v4.0/os/odata-json-format-v4.0-os.html)


### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API EntityTypes](web-api-entitytypes.md)<br />
[Web API Properties](web-api-properties.md)<br />
[Web API Navigation Properties](web-api-navigation-properties.md)<br />
[Authenticate to Dataverse with the Web API](authenticate-web-api.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br/>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]