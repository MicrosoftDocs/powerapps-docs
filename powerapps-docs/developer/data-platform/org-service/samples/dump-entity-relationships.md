---
title: " Dump table relationships to a file (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to dump table relationships to a file." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Dump table relationships information to a file

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to write out all the column definitions to an `XML` file. It uses the [RetrieveAllEntitiesRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieveallentitiesrequest?view=dynamics-general-ce-9) message. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/DumpEntityRelationShips).

The following sample creates a new file at `\DumpEntityRelationShips\bin\Debug\RelationshipInfo.xml`. You can open this file in **Office Excel** to see a tabular report. 

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveAllEntitiesRequest` message is intended to be used in a scenario that contains data that is needed to retrieve metadata information about all the tables.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `RetrieveAllEntitiesRequest` method retrieves the metadata. 
1. The `StreamWriter` creates an instance of StreamWriter to write text to a file.

### Clean up

This sample creates no records. No cleanup is required.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]