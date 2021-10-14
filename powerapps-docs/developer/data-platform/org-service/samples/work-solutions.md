---
title: "Sample: Work with solutions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to work with solutions" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Work with solutions

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-work-solutions -->

This sample shows how to how to perform the following actions with solutions:

- Create a publisher.
- Retrieve the default publisher.
- Create a solution.
- Retrieve a solution.
- Add an existing solution component.
- Remove a solution component.
- Export or package a solution.
- Install or upgrade a solution.
- Delete a solution.

You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/WorkwithSolutions).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to work with solutions. This sample covers how to create a publisher, create a solution, export and import solution and also how to delete the solution.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Publisher` method defines a new publisher. 
1. The `Solution` method creates a new solution.
1. The `OptionSetMetadata` method adds a solution component.
1. The `ExportSolutionRequest` method exports the created solution in the [Setup](#setup).
1. The `DeleteSolutionRequest` method deletes the solution and the components.

### Demonstrate

1. The `querySDKSamplePublisher` method checks whether the publisher is already in the system.
1. The `querySampleSolutionResults` method checks whether the solution is already in the system.
1. The `ExportSolutionRequest` method exports the solution.
1. The `ImportSolutionRequest` method imports the solution.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]