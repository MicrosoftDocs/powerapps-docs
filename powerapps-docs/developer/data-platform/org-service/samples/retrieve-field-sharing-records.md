---
title: "Sample: Retrieve field sharing records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve the field sharing records for a table." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Retrieve field sharing records

This sample shows how to retrieve the `PrincipalObjectAttributeAccess` (field sharing) records for a table.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve field sharing records sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveFieldSharing)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `PrincipleObjectAttributeAccess` message is intended to be used in a scenario where it retrieves the field sharing records for a table.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateAttributeRequest` method creates the custom columns required for the sample.

### Demonstrate

1. The `WhoAMIRequest` retrieves the current user's information.
2. The `RetrieveUserPrivilegesRequest` message checks if the current user has `prvReadPOAA`.
3. The `PrincipalObjectAttributeAccess` creates POAA table for the custom columns created in the Setup(#setup).
4. Using the `QueryExpression` retrieve user shared column permissions.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
