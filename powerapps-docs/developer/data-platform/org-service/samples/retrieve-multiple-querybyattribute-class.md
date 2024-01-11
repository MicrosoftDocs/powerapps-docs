---
title: "Sample: Retrieve multiple with the QueryByAttribute class(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use QueryByAttribute class" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Retrieve multiple with the QueryByAttribute class

This sample shows how to use [QueryByAttribute](/dotnet/api/microsoft.xrm.sdk.query.querybyattribute) in the [RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) method.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve multiple with the QueryByAttribute class sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveMultipleQueryByAttribute)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `QueryByAttribute` class is intended to be used in a scenario where it contains a query that is expressed as a set of column and value pairs.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates 2 account records.

### Demonstrate

The `QueryByAttribute` method creates query using QueryByAttribute.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
