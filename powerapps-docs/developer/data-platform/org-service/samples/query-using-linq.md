---
title: "Query data using LINQ (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample provides many examples of Language-Integrated Query (LINQ) with data from Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 02/05/2020
ms.reviewer: "pehecke"

ms.topic: sample
author: "phecke" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
search.audienceType:
  - developer
---

# Sample: Query data using LINQ

These samples show how to query business data using [Language-Integrated Query (LINQ)](/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq-queries).

> [!div class="nextstepaction"]
> [SDK for .NET: Query data using LINQ sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/QueriesUsingLINQ)

## How to run this sample

See [How to run samples](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/README.md) for information about how to run this sample. There are multiple projects in the solution. Each project demonstrates some aspect of LINQ queries.

## What this sample does

Read each sample's comments to find out what each sample does. There are samples that:

- Create a simple LINQ query
- Create a LINQ query using late binding
- Retrieve multiple records using condition operators
- Complex queries - a wide assortment of LINQ examples

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Creates any records required by the `Demonstrate` region of each `Main`() method.

### Demonstrate

Code in the `Demonstrate` region of the `Main`() method performs one or more LINQ queries.

### Clean up

Displays an option to delete the records created in [Setup](#setup).

The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
