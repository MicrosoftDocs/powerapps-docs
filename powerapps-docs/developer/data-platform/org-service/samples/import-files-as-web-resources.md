---
title: "Sample: Import files as web resources (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to import files as web resources" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: adrianorth
ms.author: aorth
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Import files as web resources

This sample shows how to import files as web resources.

> [!div class="nextstepaction"]
> [SDK for .NET: Import files as web resources sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/ImportWebResources)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample will show how to use the `SolutionUniqueName` optional parameter to associate a web resource with a specific solution when it is created.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` class creates a publisher and a solution required for the sample when adding the web resources.

### Demonstrate

1. The `XDocument` method reads the descriptive data from the XML files.
1. The `WebResource` is used to set the web resource properties.
1. The `CreateRequest` method is used to add optional parameters.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
