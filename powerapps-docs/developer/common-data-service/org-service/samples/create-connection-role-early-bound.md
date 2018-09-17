---
title: "Sample: Create a connection role (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a connection role" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Create a connection role

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-create-connection-role-early-bound -->

This sample shows how to create a connection role that can be used for accounts and contacts.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to create a connection role that can be used for accounts and contacts.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup
1. Checks for the current version of the org.

### Demonstrate
1. Defines some anonymous types to define the range of possible connection property values.
2. Creates a connection role for account and contact entity.
3. Creates a connection role object type code record for account and contact entity.

### Clean up

1. Display an option to delete the records in [Setup](#setup).
    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
