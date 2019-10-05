---
title: "Azure aware custom workflow activity (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample obtains the data context from the current Common Data Service operation and posts it to the Azure Service Bus." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Azure aware custom workflow activity

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-azure-aware-custom-workflow-activity -->

This sample obtains the data context from the current operation and posts it to the Azure Service Bus.You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Azurecustomworkflowactivity).

## Requirements

You must configure Common Data Service to connect with Azure before registering and executing this sample custom workflow activity. More information: [Configure Microsoft Azure Integration with Common Data Service](../../configure-azure-integration.md).

Notice the `Input id` required argument in the code. When you add this activity to a workflow, you must provide the GUID of a Azure service endpoint.

When registering this custom workflow activity with Common Data Service, you must register it in the sandbox (partial trust).

## How to run samples

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
2. Register the workflow activity.

## What this sample does

This sample shows how to write a custom workflow activity that can post the data context from the current Common Data Service operation to the Azure Service Bus. The posting of the data context is done through the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService.Execute(Microsoft.Xrm.Sdk.EntityReference,Microsoft.Xrm.Sdk.IExecutionContext)> method.
