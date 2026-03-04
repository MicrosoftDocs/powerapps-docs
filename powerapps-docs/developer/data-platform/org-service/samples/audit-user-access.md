---
title: "Sample: Audit user access (Microsoft Dataverse) | Microsoft Docs"
description: "This sample shows how to audit user access" 
ms.date: 03/04/2026
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

# Sample: Audit user access

This sample code shows how to audit user access.

> [!div class="nextstepaction"]
> [SDK for .NET: Audit user access sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/AuditUserAccess)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample first enables user access auditing with the signed-in user's organization. Next, it creates and modifies an account table so that audit records are generated.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample performs the following steps:

### Setup

1. Checks for the current version of the org.
1. Creates a new account table and enables auditing on the new account table.

### Demonstrate

1. Get the organization's ID from the system user record and retrieve the organization record.
1. Enable auditing on the organization, including auditing for user access.
1. Make an update request to the account table to be tracked by auditing.
1. Set the organization and account auditing flags back to old values and retrieve them if you changed them.

### Clean up

Display an option to delete the records you created during [Setup](#setup). You can choose not to delete these records if you want to examine the tables and data that the sample created. You can also manually delete the records.

[!INCLUDE[footer-banner](../../../../includes/footer-banner.md)]
