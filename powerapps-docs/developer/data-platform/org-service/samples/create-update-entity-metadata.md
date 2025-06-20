---
title: "Sample: Create and update table definitions  (Microsoft Dataverse) | Microsoft Docs" 
description: "This sample shows how to create and update table definitions." 
ms.date: 04/03/2022
author: mkannapiran
ms.author: kamanick
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Create and update table definitions

This topic shows how to programmatically create a custom user-owned table called **Bank Account** and add four different types of columns to it.

You can also create organization-owned custom tables. More information: [Table ownership](/dynamics365/customerengagement/on-premises/developer/introduction-entities#entity-ownership).

> [!div class="nextstepaction"]
> [SDK for .NET: Create and update table definitions sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CreateUpdateEntityMetadata)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateEntityRequest` message is intended to be used in a scenario where it contains the data that is needed to create a custom table, and optionally, to add it to a specified unmanaged solution.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `createrequest` method creates the custom table.
2. The `Entity` method is used to define the table.
3. The `StringAttributeMetadata` method defines the primary column of the table.
4. The `CreateBankNameAttributeRequest` method creates a string column to the table.
5. The `CreateBalanceAttributeRequest` method creates a money column to the table.
6. The `CreateCheckedDateRequest` method creates a DateTime column to the table.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
