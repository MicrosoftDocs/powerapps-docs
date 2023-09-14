---
title: "Azure aware custom plug-in (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample plug-in can post the pipeline execution context to the Azure Service Bus." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/19/2023
author: jaredha
ms.author: jaredha
ms.reviewer: jdaly
ms.topic: article
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Azure aware custom plug-in

The plug-in demonstrates how to obtain the execution context and the tracing service from the service provider parameter of the `Execute` method. The plug-in then posts the context to the Azure Service Bus endpoint and writes information to the trace log to facilitate debugging.

> [!div class="nextstepaction"]
> [SDK for .NET: Azure aware custom plug-in sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/Azureplugin)

## How to run this sample

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
1. Open the `Azureplugin.sln` solution file located at `PowerApps-Samples\dataverse\orgsvc\C#\Azureplugin` with Visual Studio.
1. Sign the assembly with a key.
1. Register the plug-in using the **Plugin Registration Tool**.

> [!NOTE]
> This sample requires a service endpoint to be created first, and its ID passed to the plug-in constructor through the unsecure configuration parameter when the plug-in step is registered.

More information:

[Write a custom Azure-aware plug-in](../../write-custom-azure-aware-plugin.md)  
[Register a plug-in](../../register-plug-in.md)



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
