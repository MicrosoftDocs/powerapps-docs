---
title: "Sample: Query connections by reciprocal roles (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query connections bt reciprocal roles" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Query connections by reciprocal roles

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-query-connections-reciprocal-roles-early-bound -->

This sample shows how to create matching roles and then find a matching role for a particular role. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/QueryByReciprocalRole).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to create matching roles and then find a matching role for a particular role.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup
1. Checks for the current version of the org.
2. Defines some anonymous types to define the range of possible connection property values.
3. The `ConnectionRole`creates the primary connection role instance.
4. The `ConnectionRoleObjectTypeCode` creates a connection role object type code record for account and contact entity.
5. The `AssociateRequest` associates the connection roles.

### Demonstrate

1. The `QueryExpression` retrieves all connection roles that have this role listed as reciprocal role.

### Clean up

1. Display an option to delete the records in [Setup](#setup).
    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
