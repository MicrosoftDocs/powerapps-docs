---
title: "Sample: Retrieve valid status transitions (Microsoft Dataverse) | Microsoft Docs"
description: "This sample shows how to retrieve valid state transitions." 
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

# Sample: Retrieve valid status transitions

This sample shows how to retrieve valid state transitions regardless of whether custom state transitions have been defined for the table.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve valid status transitions sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/RetrieveValidTransitions)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `GetValidStatusOptions` method is intended to be used in a scenario where it contains data that returns valid status option transitions regardless of whether state transitions are enabled for the table.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `MetadataFilterExpression` method checks for table definitions.

### Demonstrate

1. The `MetadataFilterExpression` method retrieves the status options for the `Incident` table.
1. The `RetrieveMetadataChangeRequest` method retrieves the metadata.
1. The `GetValidStatusOptions` method gets the valid status transitions for each status option.

### Clean up

This sample creates no records. No clean up is required.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
