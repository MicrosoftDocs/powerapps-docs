---
title: "Sample: Create a reciprocal connection role (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a reciprocal connection role" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Create a reciprocal connection role

This sample shows how to create the reciprocal connection roles. It creates a connection role for an account and a connection role for a contact, and then makes them reciprocal by associating them with each other

> [!div class="nextstepaction"]
> [SDK for .NET: Create a reciprocal connection role sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ReciprocalConnection)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `ConnectionRole` and `ConnectionRoleObjectTypeCode` messages are intended to be used in a scenario where it contains data that is required to create a new connection role and connection role object type.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `ConnectionRole` message creates connection roles required for the sample.
3. The `ConnectionRoleObjectTypeCode` message creates the connection role object type code record for account.
4. The `AssociateRequest` message associates the connection roles with each other.

### Demonstrate

1. Perform initial request and cache the results, including the `DataToken`
1. Update the records created in [Setup](#setup)
1. Perform a second request, this time passing the `DataVersion` with the `DataToken` value retrieved from the initial request.
1. Show the table changes returned by the second request

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
