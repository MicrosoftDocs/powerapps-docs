---
title: "Azure aware custom plug-in (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample plug-in can post the pipeline execution context to the Azure Service Bus." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: jaredha
ms.author: jaredha
manager: sunilg
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---
# Sample: Azure aware custom plug-in

The plug-in demonstrates how to obtain the execution context and the tracing service from the service provider parameter of the `Execute` method. The plug-in then posts the context to the Azure Service Bus endpoint and writes information to the trace log to facilitate debugging. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Azureplugin).

## How to run this sample

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
2. Open the sample solution in Visual Studio and sign the assembly with a key.
3. Register the plug-in using the **Plugin Registration Tool**.

>[!NOTE]
> This sample requires a service endpoint to be created first, and its ID passed to the plug-in constructor through the unsecure configuration parameter when the plug-in step is registered.




[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]