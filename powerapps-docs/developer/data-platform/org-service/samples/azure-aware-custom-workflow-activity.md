---
title: "Azure aware custom workflow activity (Microsoft Dataverse) | Microsoft Docs"
description: "This sample obtains the data context from the current Microsoft Dataverse operation and posts it to the Azure Service Bus." 
ms.date: 03/04/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
---

# Sample: Azure aware custom workflow activity

This sample gets the data context from the current operation and sends it to the Azure Service Bus.

> [!div class="nextstepaction"]
> [SDK for .NET: Azure aware custom workflow activity sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/Azurecustomworkflowactivity)

## Requirements

Before registering and running this sample custom workflow activity, configure Microsoft Dataverse to connect with Azure. For more information, see [Configure Microsoft Azure Integration with Dataverse](../../configure-azure-integration.md).

Notice the `Input id` required argument in the code. When you add this activity to a workflow, you must provide the GUID of an Azure service endpoint.

When registering this custom workflow activity with Dataverse, register it in the sandbox.

## How to run the sample

1. Download or clone the [Power Apps samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
2. Register the workflow activity.

## What this sample does

This sample shows how to write a custom workflow activity that can send the data context from the current Dataverse operation to the Azure Service Bus. The posting of the data context is done through the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService.Execute(Microsoft.Xrm.Sdk.EntityReference,Microsoft.Xrm.Sdk.IExecutionContext)> method.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
