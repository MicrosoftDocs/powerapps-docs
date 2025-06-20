---
title: "Web API data operation samples"
description: "See C#, PowerShell, and JavaScript sample code that demonstrates how to use the Microsoft Dataverse Web API for basic table row operations, data query, conditional operations, and functions and actions."
ms.topic: sample
ms.date: 01/20/2024
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API data operations samples

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can use the Microsoft Dataverse Web API with a wide variety of programming languages or libraries. This guide provides a number of code samples demonstrating how to use the Web API in different ways. This topic introduces the samples available for each group of operations and how to perform these operations using different languages or libraries.
  
## Web API samples list

This topic introduces language neutral (HTTP request/response) examples for Dataverse web API.

The following table describes the Dataverse Web API samples and their language-specific implementations.

|Language|Sample article|
|---------|---------|
|C#|[C# Web API samples](web-api-samples-csharp.md)|
|PowerShell|[PowerShell Web API samples](web-api-samples-powershell.md)|
|Client-side JavaScript|[Client-side JavaScript Web API samples](web-api-samples-client-side-javascript.md)|


  
### Groups of operations

The following table classifies the samples by demonstrated operation groups.  
  
|Group|Description|  
|-----------|-----------------|  
|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|How to perform basic CRUD (Create, Retrieve, Update, and Delete) and associative operations.<p/> More information: <br/>-   [Create a table row using the Web API](create-entity-web-api.md)<br />-   [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />-   [Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />-   [Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)|  
|[Web API Query Data Sample](web-api-query-data-sample.md)|How to perform basic query requests.<p/> More information: <br /> -   [Query Data using the Web API](query/overview.md)<br />-   [Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)|  
|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|How to perform certain categories of operations that are conditionally based upon the version of the table row contained on the  server and/or currently maintained by the client. <p/>More information:<br/>-   [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)|  
|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|How to use bound/unbound functions and actions, including custom actions.<p/>More information: <br/>-   [Use Web API functions](use-web-api-functions.md)<br />-   [Use Web API actions](use-web-api-actions.md)|
|[Web API table schema operations sample](web-api-metadata-operations-sample.md)|How to create, update, and delete table, column, and relationship definitions. More information: [Use the Web API with table definitions](use-web-api-metadata.md)|

  
### See also

[Use the Dataverse Web API](overview.md)   
[Web API Basic Operations Sample](web-api-basic-operations-sample.md)   
[Web API Query Data Sample](web-api-query-data-sample.md)   
[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)   
[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)   
[Web API table schema operations sample](web-api-metadata-operations-sample.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
