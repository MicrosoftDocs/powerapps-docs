---
title: "Sample: Use QueryExpresion with a paging cookie (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use the paging cookie in a QueryExpresion" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Use QueryExpression with a paging cookie

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/sample-use-queryexpression-with-a-paging-cookie -->

This sample shows how to use the paging cookie in a QueryExpression query to retrieve successive pages of query results. It uses the [IOrganizationService.RetrieveMultiple](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple?view=dynamics-general-ce-9) method.

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
1. The `OrderExpresion` method defines the order expresion to retrieve the records.

### Clean up

1. Displays an option to delete all the data created in the sample.

The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.
