---
title: "Sample: Create and update entity metadata  (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create and update entity metadata." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
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

# Create and update entity metadata

This topic shows how to programmatically create a custom user-owned entity called **Bank Account** and add four different types of attributes to it.

You can also create organization-owned custom entities. More information: [Entity ownership](https://docs.microsoft.com/dynamics365/customerengagement/on-premises/developer/introduction-entities#entity-ownership). You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/Nava_samplecode/cds/orgsvc/C%23/CreateUpdateEntityMetadata).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateEntityRequest` message is intended to be used in a scenario where it contains  the data that is needed to create a custom entity, and optionally, to add it to a specified unmanaged solution.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.

### Demonstrate

1. The `createrequest` method creates the custom entity. 
2. The `Entity` method is used to define the entity.
3. The `StringAttributeMetadata` method defines the primary attribute of the entity.
4. The `CreateBankNameAttributeRequest` method creates a string attribute to the entity.
5. The `CreateBalanceAttributeRequest` method creates a money attribute to the entity.
6. The `CreateCheckedDateRequest` method creates a DateTime attribute to the entity.

### Clean up

1. Display an option to delete the records created in the [Setup](#setup).

   The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
