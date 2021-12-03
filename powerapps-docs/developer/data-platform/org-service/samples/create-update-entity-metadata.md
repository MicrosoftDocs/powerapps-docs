---
title: "Sample: Create and update table definitions  (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create and update table definitions." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/17/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Create and update table definitions

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This topic shows how to programmatically create a custom user-owned table called **Bank Account** and add four different types of columns to it.

You can also create organization-owned custom tables. More information: [Table ownership](/dynamics365/customerengagement/on-premises/developer/introduction-entities#entity-ownership). You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CreateUpdateEntityMetadata).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateEntityRequest` message is intended to be used in a scenario where it contains  the data that is needed to create a custom table, and optionally, to add it to a specified unmanaged solution.

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