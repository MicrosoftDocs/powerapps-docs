---
title: "Sample: Retrieve records from an intersect table(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve record from an intersect table." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Retrieve records from an intersect table

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/org-service/sample-retrieve-records-intersect-table -->
This sample shows how to retrieve records from an intersect table. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveRecordsFromIntersectTable).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `QueryExpression` message is intended to be used in a scenario that contains queries in a hierarchy of expressions.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org. 
1. The `CreateRequireRecords` method creates table records that are used by the sample.
1. The `QueryExpression` message is used to retrieve the default business unit needed to create the team.
1. The `WhoAmIRequest` gets the GUID of the current user.
1. The `Role` message instantiate a role table record and set its property values.
1. The `AssociateRequest` assigns the user to the Managers role. 

### Demonstrate

1. The `QueryExpression` retrieves the records from an intersect table.
1. The `RetrieveMultipleRequest` builds the fetch request and obtains the results.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]