---
title: "Sample: Query connections by a record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query connections for a particular record." # 115-145 characters including spaces. This abstract displays in the search result.
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

<!-- https://learn.microsoft.com/dynamics365/customer-engagement/developer/sample-query-connections-record-early-bound -->

This sample shows how to query connections for a particular record. It creates connections between a contact and two accounts, and then searches for the contact’s connections.

> [!div class="nextstepaction"]
> [SDK for .NET: Query connections by a record (early bound) sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/QueryByRecord)

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

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
