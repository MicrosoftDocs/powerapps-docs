---
title: "Sample: Audit user access (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to audit user access" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Audit user access

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-audit-user-access -->

This sample code shows how to audit user access. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AuditUserAccess).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample first enables user access auditing with the logged on user's organization. Next, it creates and modifies an account table so that audit rows are generated.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates a new account table and enables auditing on the new account table.

### Demonstrate

1. Gets the organization's ID from the system user row and retrieves organization row.
2. Enables auditing on the organization, including auditing for user access.
3. Makes an update request to the account table to be tracked by auditing.
4. set the organization and account auditing flags back to old values and retrieve them if they were actually changed.

### Clean up

Display an option to delete the rows created during [Setup](#setup). The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the rows to achieve the same result.
