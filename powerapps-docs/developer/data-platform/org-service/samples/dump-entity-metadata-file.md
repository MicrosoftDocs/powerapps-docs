---
title: "Sample: Dump table definitions to a file (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write out all the table definitions to an XML file." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: NHelgren
ms.author: nhelgren
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Dump table definitions to a file

This sample shows how to write out all table definitions to an `XML` file. It uses the [RetrieveAllEntitiesRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieveallentitiesrequest) message.

The following sample creates a new file at `\Entities\bin\Debug\EntityInfo.xml`. You can open this file in Office Excel to see a tabular report. You may need this information to discover the entity type code for a custom table for use in reports.

> [!div class="nextstepaction"]
> [SDK for .NET: Dump table definitions to a file sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/DumpEntityMetadata)

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
