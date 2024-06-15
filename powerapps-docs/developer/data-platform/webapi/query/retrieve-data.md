---
title: Use OData to retrieve data
description: Learn how to use OData to send a request to retrieve data using Dataverse Web API.
ms.date: 07/01/2024
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Use OData to retrieve data


## Use OData within a batch request

The length of a URL in a `GET` request [is limited to 32 KB (32,768 characters)](../webapi/compose-http-requests-handle-errors.md#maximum-url-length). Including OData as a parameter in the URL can reach the limit. You can execute a `$batch` operation using a `POST` request as a way to move the OData out of the URL and into the body of the request where the limit doesn't apply. Sending a `GET` request within a `$batch` allows for URLs up to 64 KB (65,536 characters) in length. More than with a normal `GET` request, but it isn't unlimited. More information:  [Execute batch operations using the Web API](../execute-batch-operations-using-web-api.md).

[Quick Start: Web API sample (C#)](../quick-start-console-app-csharp.md)   
[Use the Microsoft Dataverse Web API](../overview.md)

---

## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

Try some sample code

> [!div class="nextstepaction"]
> [OData Sample code](sample.md)
