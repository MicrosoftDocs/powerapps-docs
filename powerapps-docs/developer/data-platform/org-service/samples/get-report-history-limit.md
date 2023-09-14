---
title: "Sample: Get report history limits (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to get report history limits." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Get report history limits

This sample shows how to get report history limits using the [GetReportHistoryLimitRequest](/dotnet/api/microsoft.crm.sdk.messages.getreporthistorylimitrequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Get report history limits sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/GetReportHistoryLimit)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `GetReportHistoryLimitRequest` message is intended to be used in a scenario where it contains data that is needed to retrieve the history limit for a report.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `QueryByAttribute` method queries for an existing report.
2. The `GetReportHistoryLimitRequest` method gets the history limit data.

### Clean up

No clean up is required for this sample.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
