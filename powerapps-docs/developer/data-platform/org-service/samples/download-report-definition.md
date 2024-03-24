---
title: "Sample: Download report definition (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to download report definition" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Download report definition

This sample shows how to download a report definition (.rdl) file by using the [DownloadReportDefinitionRequest](/dotnet/api/microsoft.crm.sdk.messages.downloadreportdefinitionrequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Download report definition sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/DownloadReportDefinition)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `DownloadReportDefinitionRequest` message is intended to be used in a scenario where it contains the data that is needed to download a report definition.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `QueryByAttribute` method queries for an existing report.
2. The `DownloadReportDefinitionRequest` method downloads the report definition.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
