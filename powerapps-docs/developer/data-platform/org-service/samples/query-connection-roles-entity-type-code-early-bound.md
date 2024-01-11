---
title: "Sample: Query connection role by entity type code (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query a connection ro" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Query connection roles by entity type code (early bound)

This sample shows how to use a query to find a connection role for an account table by specifying an entity type code.

> [!div class="nextstepaction"]
> [SDK for .NET: Query connection roles by entity type code (early bound) sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/QueryRoleByEntityType)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to use a query to find a connection role for an account table by specifying an entity type code.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. Defines some anonymous types to define the range of possible connection property values.
2. The `ConnectionRole` creates a connection role.
3. The `QueryExpression` queries all the connection roles.
4. The `ConnectionRoleObjectTypeCode` creates a connection role object type code record for account table.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
