---
title: "Sample: Publish reports (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to publish reports." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Publish reports

This sample shows how to publish a report by creating a **Report** record and the related records that make it visible.

> [!div class="nextstepaction"]
> [SDK for .NET: Publish reports sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/PublishReport)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## How this sample works

In order to simulate the scenario described above, the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `Report` method instantiates the report object.
2. The `ReportCategory` method sets the report category te report should belong to.
3. The `ReportEntity` method defines which table this report uses.
4. The `ReportVisibility` method sets the report visibility.

### Clean up

No clean up is required for this sample.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
