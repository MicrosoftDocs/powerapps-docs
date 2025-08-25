---
title: "Sample: Query connections by a record (early bound)"
description: "This sample shows how to query connections for a particular record."
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

# Sample: Query connections by a record (early bound)

This sample shows how to query connections for a particular record. It creates connections between a contact and two accounts, and then searches for the contact's connections.

> [!div class="nextstepaction"]
> [SDK for .NET: Query connections by a record (early bound) sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/QueryByRecord)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample creates account and contact records and creates connection roles between them. The `QueryExpression` retrieves the connections for a particular record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Defines some anonymous types to define the range of possible connection property values.
3. The `ConnectionRole` creates a connection role.
4. The `ConnectionRoleObjectType` creates a connection role object type code record for account table.
5. Creates few account and contact records for use in the connection.

### Demonstrate

The `QueryExpression` retrieves all the connections associated with the contact created in the sample.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[Use connections to link records to each other](../../connection-entities.md)   
[Describe a relationship between tables with connection roles](../../describe-relationship-entities-connection-roles.md)  
[Sample: Create a connection](create-connection-early-bound.md)  
[Sample: Create a connection role](create-connection-role-early-bound.md)  
[Sample: Create a reciprocal connection role](create-reciprocal-connection-role-early-bound.md)  
[Sample: Query connection roles by entity type code (early bound)](query-connection-roles-entity-type-code-early-bound.md)  
[Sample: Query connections by reciprocal roles (early bound)](query-connections-reciprocal-roles-early-bound.md)  
[Sample: Update a connection role (early bound)](update-connection-role.md)  

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
