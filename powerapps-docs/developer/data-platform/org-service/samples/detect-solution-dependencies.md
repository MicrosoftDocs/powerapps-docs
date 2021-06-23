---
title: "Sample: Detect solution dependencies(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to detect dependencies on solutions." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Detect solution dependencies

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to detect dependencies before you delete a solution component.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveDependentComponentsRequest`, `RetrieveDependenciesForDeleteRequest` messages are intended to be used in a scenario where it contains data to detect solution dependencies. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/SolutionDependencies).

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Publisher` method creates the sample publisher that will `own` the two solutions.
1. The `Solution` method creates the primary solution.
1. The `OptionSetMetadata` creates the global option set and associates it to the solution.
1. The `ExportSolutionRequest` exports the solution as managed so that we can later import it.
1. The `DeleteOptionSetRequest` deletes the option set previously created, so it can be imported under the managed solution.
1. The `ImportSolutionRequest` re-imports the solution as managed.

### Demonstrate

1. The `QueryByAttribute` queries all solution components for a solution.
1. The `RetrieveDependentComponentsRequest` retrieves all the dependencies for the component. If there are no dependencies we can ignore this component. If there are dependencies upon this solution component, and the solution itself is managed, then you will be unable to delete the solution.

### Clean up

Display an option to delete the solutions created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]