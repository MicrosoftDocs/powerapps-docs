---
title: "Sample: Retrieve multiple with QueryExpression (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve multiple using QueryExpression" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Retrieve multiple with the QueryExpression class

This sample shows how to retrieve multiple tables using the [IOrganizationService.RetrieveMultiple(QueryBase)](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple#Microsoft_Xrm_Sdk_IOrganizationService_RetrieveMultiple_Microsoft_Xrm_Sdk_Query_QueryBase_) method with [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression) along with their related table columns. 

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve multiple with the QueryExpression class sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveMultipleByQueryExpression)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `QueryExpression` class is intended to be used in a scenario where it contains a complex query expressed in a hierarchy of expressions.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. Creates multiple accounts with primary contacts.
1. The `QueryExpression` class creates a query expression specifying the link table alias and the columns of the link table that you want to return.

### Clean up

No clean up is required.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
