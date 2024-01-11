---
title: "Sample: Solution staging with asynchronous import (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Demonstrates how to stage and asynchronously import a solution." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/05/2022
ms.reviewer:
ms.topic: sample
author: "phecke" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
search.audienceType:
  - developer
---

# Sample: Solution staging with asynchronous import

<!-- https://learn.microsoft.com/dynamics365/customer-engagement/developer/sample-work-solutions -->

This sample shows how to perform the following actions with solutions:

- Stage a solution and check the validation results
- Import the staged solution using an asynchronous job and check for job completion

> [!div class="nextstepaction"]
> [SDK for .NET: Solution staging with asynchronous import sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/SolutionStagingAndImport)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

Be sure to edit the App.config file and set the Username, Password, and Url values for your test environment.

## What this sample does

This sample shows how to stage (load) a solution in a Microsoft Dataverse environment and check the solution validation results. This enables you to check for a valid solution staging prior to solution import. Next, the sample performs an asynchronous import of the staged solution. An asynchronous job allows for importing large solutions and avoiding a timeout error.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Invokes the SampleHelpers.Connect method to authenticate the user and return a web service reference.

### Demonstrate

1. The `StageSolution` method reads the compressed solution file and stages the solution.
1. The `ImportSolution` method imports the solution using an asynchronous job.
1. The `CheckImportStatus` method waits for the asynchronous job to complete and checks the job for a successful status.

### Clean up

The program does not automatically delete the imported solution. You should manually delete the solution named "Contoso sample" from your test environment.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
