---
title: "Sample: Query connections by a record (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query connections for a particular record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Query connections by a record 

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-query-connections-record-early-bound -->

This sample shows how to query connections for a particular record. It creates connections between a contact and two accounts, and then searches for the contact’s connections.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample creates account and contact records and creates connection roles betweem them. The `QueryExpression` retrieves the connections for a particular record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup
1. Checks for the current version of the org.
2. Defines some anonymous types to define the range of possible conection property values.
3. The `ConnectionRole` creates a connection role.
4. The `ConnectionRoleObjectType` creates a connection role object type code record for account entity. 
5. Creates few account and contact records for use in the connection.



### Demonstrate
1. The `QueryExpression` retrieves all the connections associated with the contact created in the sample.

### Clean up

1. Display an option to delete the records in [Setup](#setup).
    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
