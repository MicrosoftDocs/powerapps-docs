---
title: "Sample: Query connections by reciprocal roles (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query connections bt reciprocal roles" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Query connections by reciprocal roles (early bound)

This sample shows how to create matching roles and then find a matching role for a particular role.

> [!div class="nextstepaction"]
> [SDK for .NET: Query connections by reciprocal roles (early bound) sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/QueryByReciprocalRole)

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
4. The `ConnectionRoleObjectTypeCode` creates a connection role object type code record for account and contact table.
5. The `AssociateRequest` associates the connection roles.

### Demonstrate

The `QueryExpression` retrieves all connection roles that have this role listed as reciprocal role.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[Use connections to link records to each other](../../connection-entities.md)   
[Describe a relationship between tables with connection roles](../../describe-relationship-entities-connection-roles.md)  
[Sample: Create a connection](create-connection-early-bound.md)  
[Sample: Create a connection role](create-connection-role-early-bound.md)  
[Sample: Create a reciprocal connection role](create-reciprocal-connection-role-early-bound.md)  
[Sample: Query connections by a record (early bound)](query-connections-record-early-bound.md)  
[Sample: Query connection roles by entity type code (early bound)](query-connection-roles-entity-type-code-early-bound.md)  
[Sample: Update a connection role (early bound)](update-connection-role.md)  

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
