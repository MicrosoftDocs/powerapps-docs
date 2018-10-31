---
title: "Azure aware custom workflow activity(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample obtains the data context from the current Dynamics 365 Customer Engagement operation and posts it to the Azure Service Bus." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Azure aware custom workflow activity

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-azure-aware-custom-workflow-activity -->

This sample obtains the data context from the current operation and posts it to the Azure Service Bus.You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Azurecustomworkflowactivity).

## Requirements

You must configure CDS for Apps to connect with Azure before registering and executing this sample custom workflow activity. More information: [Configure Microsoft Azure Integration with CDS for Apps](../../configure-azure-integration.md).

Notice the `Input id` required argument in the code. When you add this activity to a workflow, you must provide the GUID of a Azure service endpoint.

When registering this custom workflow activity with CDS for Apps, you must register it in the sandbox (partial trust).

## How to run samples

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
2. Register the workflow activity.

## What this sample does

This sample shows how to write a custom workflow activity that can post the data context from the current CDS for Apps operation to the Azure Service Bus. The posting of the data context is done through the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService.Execute(Microsoft.Xrm.Sdk.EntityReference,Microsoft.Xrm.Sdk.IExecutionContext)> method.
