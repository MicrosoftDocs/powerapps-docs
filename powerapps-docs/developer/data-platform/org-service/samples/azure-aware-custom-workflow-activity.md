---
title: "Azure aware custom workflow activity (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample obtains the data context from the current Microsoft Dataverse operation and posts it to the Azure Service Bus." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: jaredha
ms.author: jaredha
ms.reviewer: jdaly
ms.topic: article
search.audienceType:
  - developer
---

# Sample: Azure aware custom workflow activity

This sample obtains the data context from the current operation and posts it to the Azure Service Bus.

> [!div class="nextstepaction"]
> [SDK for .NET: Azure aware custom workflow activity sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/Azurecustomworkflowactivity)

## Requirements

You must configure Microsoft Dataverse to connect with Azure before registering and executing this sample custom workflow activity. More information: [Configure Microsoft Azure Integration with Dataverse](../../configure-azure-integration.md).

Notice the `Input id` required argument in the code. When you add this activity to a workflow, you must provide the GUID of a Azure service endpoint.

When registering this custom workflow activity with Dataverse, you must register it in the sandbox (partial trust).

## How to run samples

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
2. Register the workflow activity.

## What this sample does

This sample shows how to write a custom workflow activity that can post the data context from the current Dataverse operation to the Azure Service Bus. The posting of the data context is done through the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService.Execute(Microsoft.Xrm.Sdk.EntityReference,Microsoft.Xrm.Sdk.IExecutionContext)> method.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
