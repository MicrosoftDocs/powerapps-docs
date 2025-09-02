---
title: "Sample: Create a connection role (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a connection role" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Create a connection role

This sample shows how to create a connection role that can be used for accounts and contacts.

> [!div class="nextstepaction"]
> [SDK for .NET: Create a connection role sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/ConnectionRole)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to create a connection role that can be used for accounts and contacts.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. Defines some anonymous types to define the range of possible connection property values.
2. Creates a connection role for account and contact table.
3. Creates a connection role object type code record for account and contact table.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[Use connections to link records to each other](../../connection-entities.md)   
[Describe a relationship between tables with connection roles](../../describe-relationship-entities-connection-roles.md)  
[Sample: Create a connection](create-connection-early-bound.md)  
[Sample: Create a reciprocal connection role](create-reciprocal-connection-role-early-bound.md)  
[Sample: Query connections by a record (early bound)](query-connections-record-early-bound.md)  
[Sample: Query connection roles by entity type code (early bound)](query-connection-roles-entity-type-code-early-bound.md)  
[Sample: Query connections by reciprocal roles (early bound)](query-connections-reciprocal-roles-early-bound.md)  
[Sample: Update a connection role (early bound)](update-connection-role.md)  

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
