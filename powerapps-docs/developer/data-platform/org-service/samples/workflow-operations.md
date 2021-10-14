---
title: "Sample: Workflow operations (Microsoft Dataverse) | MicrosoftDocs"
description: "This sample demonstrates how to perform a number of workflow operations such as create, delete, activate, set state , and more."
ms.custom: ""
ms.date: 1/14/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Workflow operations

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample demonstrates how to perform a number of workflow operations such as create, delete, activate, set state , and more.

Download the sample: [Workflow](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Workflow)

## How to run this sample

See [How to run samples](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/README.md) for general information about how to run this sample.

Notice that there are five separate samples, each in it's own C# file, in the solution's [project](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Workflow/Workflow). To run each sample, set it as the startup object in the project's properties prior to executing the sample.

## What this sample does

The operations demonstrated by these samples are as follows:

- Create a synchronous (real-time) or asynchronous workflow
- Delete a workflow
- Execute a workflow
- Activate or deactivate a workflow
- Set or get a workflow's status and state
- Create a workflow from a template

You can view created workflows in **Settings > Processes** (under Process Center) when viewing your organization using a web browser.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Each sample creates any required table instances that the demonstration code requires. This is done in the `CreateRequiredRecords()` method.

### Demonstrate

The main demonstration code for each sample is found in the `Demonstrate` region of the `Main()` method in each class file.

### Clean up

The `DeleteRequiredRecords()` method displays an option in the console window to delete any records created by the sample(s).

The deletion is optional in case you want to examine the table instances (records) created by the sample(s). Typically, you would not respond to the delete prompt in the console window until after you view the new organization records in your browser. You can manually delete the created records any time after the program terminates to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]