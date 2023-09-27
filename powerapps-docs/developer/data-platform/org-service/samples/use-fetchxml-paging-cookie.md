---
title: "Sample: Use FetchXML with a paging cookie (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use the paging cookie in a FetchXML" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Use FetchXML with a paging cookie

This sample shows how to use the paging cookie in a FetchXML query to retrieve successive pages of query results. It uses the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A>.

> [!div class="nextstepaction"]
> [SDK for .NET: Use FetchXML with a paging cookie sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/UseFetchXMLWithPaging)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService.Retrieve` method is intended to be used in a scenario where it contains data that retrieves all the records.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates an parent account record and also 10 child account records.

### Demonstrate

The `fetchXml` creates the FetchXML string for retrieving all child accounts to a parent account. This fetch query is using 1 placeholder to specify the parent account id for filtering out required accounts.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
