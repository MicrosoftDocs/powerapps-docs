---
title: "Sample: Workflow operations (Microsoft Dataverse) | MicrosoftDocs"
description: "This sample demonstrates how to perform a number of workflow operations such as create, delete, activate, set state , and more."
ms.date: 04/06/2022
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
---

# Sample: Workflow operations

This sample demonstrates how to perform a number of workflow operations such as create, delete, activate, set state , and more.

Download the sample: [Workflow](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/Workflow)

## How to run this sample

See [How to run samples](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/README.md) for general information about how to run this sample.

Notice that there are five separate samples, each in it's own C# file, in the solution's [project](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/Workflow/Workflow). To run each sample, set it as the startup object in the project's properties prior to executing the sample.

> [!IMPORTANT]
> Some operations described in these samples are not supported by Dataverse. In Dataverse, workflows must be created and updated using the Workflow designer. With Dynamics 365 Customer Engagement on-premises you can create Workflows using the XAML definitions with code. This is not supported with Dataverse.

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

Each sample creates any required records that the demonstration code requires. This is done in the `CreateRequiredRecords()` method.

### Demonstrate

The main demonstration code for each sample is found in the `Demonstrate` region of the `Main()` method in each class file.

### Clean up

The `DeleteRequiredRecords()` method displays an option in the console window to delete any records created by the sample(s).

The deletion is optional in case you want to examine the records created by the sample(s). Typically, you would not respond to the delete prompt in the console window until after you view the new organization records in your browser. You can manually delete the created records any time after the program terminates to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
