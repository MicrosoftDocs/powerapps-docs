---
title: "Sample: Dump choices/picklist information to a file (Microsoft Dataverse) | Microsoft Docs" 
description: "This sample showcases how to dump choices information to a file." 
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

# Sample: Dump choices/picklist information to a file

This sample shows how to write out all the choices column definitions to an `XML` file. It uses the [RetrieveAllEntitiesRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieveallentitiesrequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Dump choices/picklist information to a file sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/DumpPickListInfo)

The following sample creates a new file at `\DumpPickListInfo\bin\Debug\AttributePicklistValues.xml`. You can open this file in **Office Excel** to see a tabular report.

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
