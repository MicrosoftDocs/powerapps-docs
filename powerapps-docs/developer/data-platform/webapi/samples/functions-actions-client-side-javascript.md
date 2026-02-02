---
title: "Web API Functions and Actions Sample (Client-side JavaScript) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API and client-side JavaScript."
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

# Web API Functions and Actions Sample (Client-side JavaScript)

This sample contains code that demonstrates how to use Web API functions and actions using client-side JavaScript to complete the set of operations described by the [Web API Functions and Actions Sample](../web-api-functions-actions-sample.md).

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/JS/SPASample/src/samples/FunctionsAndActions.js)

This code uses the [DataverseWebAPI.js sample library](../dataversewebapi-sample-library.md) and is designed to run in the context of a [Single Page Application (SPA)](https://developer.mozilla.org/docs/Glossary/SPA) sample available on GitHub. [Learn more about the sample application](../web-api-samples-client-side-javascript.md)

[!INCLUDE [cc-web-api-spa-javascript-code-sample-note](../../includes/cc-web-api-spa-javascript-code-sample-note.md)]

## Prerequisites

This sample has the same prerequisites as [Quick Start Web API with client-side JavaScript and Visual Studio Code](../quick-start-js-spa.md#prerequisites). To run this sample, you should complete the quick start first. You can use the same application registration information for that quick start to run this sample.

## Context

This sample starts when the user selects a button that triggers the following event handler:

```javascript
// Add event listener to the basic operations button
document.getElementById("functionsAndActionsButton").onclick = async function () {
   runSample(new FunctionsAndActions(client, container));
};
```

The `runSample` function takes an instance of the `FunctionsAndActions` class where the constructor accepts a [DataverseWebAPI.Client](../dataversewebapi-sample-library.md#client-class) instance and a reference to a container to write messages to.

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/scripts/index.js" id="runSample":::

## FunctionsAndActions.js

This sample is different from others because it installs a managed solution that contains a bound function defined by a Custom API named `sample_IsSystemAdmin` included in a managed solution named `IsSystemAdminFunction`. The `IsSystemAdminFunction_1_0_0_0_managed.js` library provides the base64 encoded string value that represents the `IsSystemAdminFunction_1_0_0_0_managed.zip` solution file. The private `#installIsSystemAdminFunctionSolution` method uses this data with the [ImportSolution Action](/power-apps/developer/data-platform/webapi/reference/importsolution) to create this `sample_IsSystemAdmin` function.

[Learn more about the IsSystemAdmin custom API sample](../../org-service/samples/issystemadmin-customapi-sample-plugin.md)

The following is the `FunctionsAndActions` class that contains the code for this sample.

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/samples/FunctionsAndActions.js":::

### See also

[Use the Dataverse Web API](../overview.md)<br />
[Use Web API functions](../use-web-api-functions.md)<br />
[Use Web API actions](../use-web-api-actions.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Functions and Actions Sample](../web-api-functions-actions-sample.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](basic-operations-client-side-javascript.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
