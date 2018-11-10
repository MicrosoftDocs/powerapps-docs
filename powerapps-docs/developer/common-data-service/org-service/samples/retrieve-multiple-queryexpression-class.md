---
title: "Sample: Retrieve multiple with QueryExpression (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve multiple using QueryExpression" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Retrieve multiple with the QueryExpression class

<!-- Re-title? This is really about retrieving  related records 
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/sample-retrieve-multiple-queryexpression-class
-->
This sample shows how to retrieve multiple entities using the [IOrganizationService.RetrieveMultiple(QueryBase)](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple?view=dynamics-general-ce-9#Microsoft_Xrm_Sdk_IOrganizationService_RetrieveMultiple_Microsoft_Xrm_Sdk_Query_QueryBase_) method with [QueryExpression](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.query.queryexpression?view=dynamics-general-ce-9) along with their related entity columns. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveMultipleByQueryExpression).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]


## What this sample does

The `QueryExpression` class is intended to be used in a scenario where it contains a complex query expressed in a hierarchy of expressions.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.

### Demonstrate
1. Creates multiple accounts with primary contacts.
1. The `QueryExpression` class creates a query expression specifying the link entity alias and the columns of the link entity that you want to return.
### Clean up

1. No clean up is required.
