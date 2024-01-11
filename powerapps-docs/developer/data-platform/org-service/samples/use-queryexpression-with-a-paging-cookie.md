---
title: "Sample: Use QueryExpresion with a paging cookie (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use the paging cookie in a QueryExpresion" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Use QueryExpression with a paging cookie

This sample shows how to use the paging cookie in a QueryExpression query to retrieve successive pages of query results. It uses the [IOrganizationService.RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) method.

> [!div class="nextstepaction"]
> [SDK for .NET: Use QueryExpression with a paging cookie sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/UseQueryExpressionwithPaging)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService.RetreiveMultiple` method is intended to be used in a scenario where it retrieves a collection of records.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates a parent account record and 10 child account records.

### Demonstrate

1. The `ConditionExpress` defines the condition expression for retrieving records.
1. The `OrderExpression` method defines the order expression to retrieve the records.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
