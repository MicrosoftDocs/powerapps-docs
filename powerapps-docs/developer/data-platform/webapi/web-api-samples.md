---
title: "Web API data operation samples (Microsoft Dataverse) | Microsoft Docs"
description: "See C# and JavaScript sample code that demonstrates how to use the Microsoft Dataverse Web API for basic table row operations, data query, conditional operations, and functions and actions."
ms.custom: ""
ms.date: 06/14/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: cdcb02f5-3baa-4fb7-8fb3-6fe53c2d4271
caps.latest.revision: 11
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Web API data operations samples

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can use the Microsoft Dataverse Web API with a wide variety of programming languages or libraries. This guide provides a number of code samples demonstrating how to use the Web API in different ways. This topic introduces the samples available for each group of operations and how to perform these operations using different languages or libraries.

<!-- TODO:
> [!NOTE]
> With the availability of the new [Xrm.WebApi](../clientapi/reference/xrm-webapi.md) client API methods, we are working on updating the client-side JavaScript samples to use the new client API methods. Check back soon.   -->
  
## Web API samples list

The following table describes the Dataverse Web API samples and their language-specific implementations.  
  
|Language-neutral description|C# implementation|Client-side JavaScript implementation|  
|-----------------------------------|------------------------|--------------------------------------------|  
|[Web API Samples](web-api-samples.md) (this topic)|[Web API Samples (C#)](web-api-samples-csharp.md)|[Web API Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)|  
<!-- TODO:
|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)|Under construction. See [Xrm.WebApi](../clientapi/reference/xrm-webapi.md)|  
|[Web API Query Data Sample](web-api-query-data-sample.md)|[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)|Under construction. See [Xrm.WebApi](../clientapi/reference/xrm-webapi.md)|   
|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|[Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)|Under construction. See [Xrm.WebApi](../clientapi/reference/xrm-webapi.md)|  
|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)|Under construction. See [Xrm.WebApi](../clientapi/reference/xrm-webapi.md)|  -->  
  
### Groups of operations

The following table classifies the samples by demonstrated operation groups.  
  
|Group|Description|  
|-----------|-----------------|  
|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|How to perform basic CRUD (Create, Retrieve, Update, and Delete) and associative operations.<p/> More information: <br/>-   [Create a table row using the Web API](create-entity-web-api.md)<br />-   [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />-   [Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />-   [Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)|  
|[Web API Query Data Sample](web-api-query-data-sample.md)|How to perform basic query requests.<p/> More information: <br /> -   [Query Data using the Web API](query-data-web-api.md)<br />-   [Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)|  
|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|How to perform certain categories of operations that are conditionally based upon the version of the table row contained on the  server and/or currently maintained by the client. <p/>More information:<br/>-   [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)|  
|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|How to use bound/unbound functions and actions, including custom actions.<p/>More information: <br/>-   [Use Web API functions](use-web-api-functions.md)<br />-   [Use Web API actions](use-web-api-actions.md)|  
  
### Language or library

The following table lists the topics that cover the common language- or library-specific implementation issues.  
  
|Language or library|Description|  
|-------------------------|-----------------|  
|[Web API Samples (C#)](web-api-samples-csharp.md)|Describes the common elements used in this group of C# samples which demonstrate operations using basic .NET classes and a minimum of helper libraries.|  
|[Web API Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)|Under construction.|  
  
### See also

[Use the Dataverse Web API](overview.md)<br />
[Web API Basic Operations Sample](web-api-basic-operations-sample.md)<br />
[Web API Query Data Sample](web-api-query-data-sample.md)<br />
[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)<br />
[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)<br />
[Web API Samples (C#)](web-api-samples-csharp.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]