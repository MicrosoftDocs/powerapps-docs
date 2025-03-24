---
title: "Web API Basic Operations Sample (Client-side JavaScript) (Microsoft Dataverse)"
description: "This sample demonstrates how to perform basic CRUD (create, retrieve, update, and delete) and association and dissociation operations on table rows (entity records) using client-side JavaScript and the Microsoft Dataverse Web API."
ms.date: 03/22/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
  - Mattp123
---

# Web API Basic Operations Sample (client-side JavaScript)

This sample contains code that demonstrates how to perform basic CRUD (create, retrieve, update, and delete) and association and dissociation operations on tables rows (entity records) using client-side JavaScript. This sample completes the set of operations described by the [Web API Basic Operations Sample](../web-api-basic-operations-sample.md).

This code uses the [DataverseWebAPI.js sample library](../dataversewebapi-sample-library.md) and is designed to run in the context of a [Single Page Application (SPA)](https://developer.mozilla.org/docs/Glossary/SPA) sample available on GitHub. [Learn more about the sample application](../web-api-samples-client-side-javascript.md)

[!INCLUDE [cc-web-api-spa-javascript-code-sample-note](../../includes/cc-web-api-spa-javascript-code-sample-note.md)]

## Prerequisites

This sample has the same prerequisites as [Quick Start Web API with client-side JavaScript and Visual Studio Code](../quick-start-js-spa.md#prerequisites). To run this sample, you should complete the quick start first. You can use the same application registration information for that quick start to run this sample.

## Context

This sample starts when the user selects a button that triggers the following event handler:

```javascript
// Add event listener to the basic operations button
document.getElementById("basicOperationsButton").onclick = async function () {
   runSample(new BasicOperationsSample(client, container));
};
```

The `runSample` function takes an instance of the `BasicOperationsSample` class where the constructor accepts a [DataverseWebAPI.Client](../dataversewebapi-sample-library.md#client-class) instance and a reference to a container to write messages to.

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/scripts/index.js" id="runSample":::


## BasicOperationsSample.js

The following is the `BasicOperationsSample` class that contains the code for this sample.

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/samples/BasicOperationsSample.js":::

### See also

[Use the Dataverse Web API](../overview.md)   
[Create a table row using the Web API](../create-entity-web-api.md)   
[Retrieve a table row using the Web API](../retrieve-entity-using-web-api.md)   
[Update and delete table rows using the Web API](../update-delete-entities-using-web-api.md)   
[Web API Samples](../web-api-samples.md)   
[Web API Basic Operations Sample](../web-api-basic-operations-sample.md)   
[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)   
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)   
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)   
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)   
[Web API Functions and Actions Sample (Client-side JavaScript)](functions-actions-client-side-javascript.md)   

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
