---
title: "Sample: Associate security role to a team (Microsoft Dataverse) | Microsoft Docs"
description: "This sample showcases how to assign a security role to a team " 
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

# Sample: Associate security role to a team

This sample shows how to assign a security role to a team by using the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) class.

> [!NOTE]
> This example doesn't take into consideration that a team or user can only be assigned a role from its business unit. The role to assign is the first one from the collection that the `RetrieveMultiple` method returns. If that record is from a business unit that differs from the requesting team, the assignment fails.


> [!div class="nextstepaction"]
> [SDK for .NET: Associate security role to a team sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/AssociateSecurityRoleToTeam)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

Use the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) class when you want to assign a specified record to a new owner (user or team) by changing the `OwnerId` column of the record.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample performs the following steps:

### Setup

1. Checks for the current version of the org.
1. The `CreateRequiredRecords` method creates the records required by the sample.

### Demonstrate

1. The `query` method retrieves a role from Microsoft Dataverse.
1. The `Associate` method assigns the role to a team.

### Clean up

[Setup](#setup) displays an option to delete the sample data. You can choose not to delete the sample data if you want to examine the tables and data that the sample creates. You can also manually delete the records.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
