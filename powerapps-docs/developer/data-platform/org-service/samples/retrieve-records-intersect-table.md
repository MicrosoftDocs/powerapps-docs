---
title: "Sample: Retrieve records from an intersect table(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve record from an intersect table." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Retrieve records from an intersect table

This sample shows how to retrieve records from an intersect table.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve records from an intersect table sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveRecordsFromIntersectTable)

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
