---
title: "Web API Conditional Operations Sample (Client-side JavaScript) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform conditional operations using Microsoft Dataverse Web API and client-side JavaScript."
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

# Web API Conditional Operations Sample (Client-side JavaScript)

This sample contains code that demonstrates how to perform conditional operations using client-side JavaScript to complete the set of operations described by the [Web API Conditional Operations Sample](../web-api-conditional-operations-sample.md).

This code uses the [DataverseWebAPI.js sample library](../dataversewebapi-sample-library.md) and is designed to run in the context of a [Single Page Application (SPA)](https://developer.mozilla.org/docs/Glossary/SPA) sample available on GitHub. [Learn more about the sample application](../web-api-samples-client-side-javascript.md)

[!INCLUDE [cc-web-api-spa-javascript-code-sample-note](../../includes/cc-web-api-spa-javascript-code-sample-note.md)]

## Prerequisites

This sample has the same prerequisites as [Quick Start Web API with client-side JavaScript and Visual Studio Code](../quick-start-js-spa.md#prerequisites). To run this sample, you should complete the quick start first. You can use the same application registration information for that quick start to run this sample.

## Context

This sample starts when the user selects a button that triggers the following event handler:

```javascript
// Add event listener to the basic operations button
document.getElementById("conditionalOperationsButton").onclick = async function () {
   runSample(new ConditionalOperationsSample(client, container));
};
```

The `runSample` function takes an instance of the `ConditionalOperationsSample` class where the constructor accepts a [DataverseWebAPI.Client](../dataversewebapi-sample-library.md#client-class) instance and a reference to a container to write messages to.

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/scripts/index.js" id="runSample":::


## ConditionalOperationsSample.js

The following is the `ConditionalOperationsSample` class that contains the code for this sample.

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/samples/ConditionalOperationsSample.js":::


### See also

[Use the Dataverse Web API](../overview.md)<br />
[Perform conditional operations using the Web API](../perform-conditional-operations-using-web-api.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Conditional Operations Sample](../web-api-conditional-operations-sample.md)<br />
[Web API Conditional Operations Sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](basic-operations-client-side-javascript.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)<br />
[Web API Functions and Actions Sample (Client-side JavaScript)](functions-actions-client-side-javascript.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
