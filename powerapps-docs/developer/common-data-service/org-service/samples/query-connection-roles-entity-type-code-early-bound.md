---
title: "Sample: Query connection role by entity type code(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query a xonncetion ro" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Query connection roles by entity type code

This sample shows how to use a query to find a connection role for an account entity by specifying an entity type code.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to use a query to find a connection role for an account entity by specifying an entity type code.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.

### Demonstrate

1. Defines some anonymous types to define the range of possible conection property values.
2. The `ConnectionRole` creates a connection role.
3. The `QueryExpression` queries all the connection roles.
4. The `ConnectionRoleObjectTypeCode` creates a connection role object type code record for account entity. 

### Clean up

1. Display an option to delete the records in [Setup](#setup).
    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
