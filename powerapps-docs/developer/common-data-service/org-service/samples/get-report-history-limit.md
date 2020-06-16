---
title: "Sample: Get report history limits (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to get report history limits." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# Get report history limits

This sample shows how to get report history limits using the [GetReportHistoryLimitRequest](https://docs.microsoft.com/dotnet/api/microsoft.crm.sdk.messages.getreporthistorylimitrequest?view=dynamics-general-ce-9) message. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/GetReportHistoryLimit).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `GetReportHistoryLimitRequest` message is intended to be used in a scenario where it contains data that is needed to retrieve the history limit for a report.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `QueryByAttribute` method  queries for an existing report.
2. The `GetReportHistoryLimitRequest` method gets the history limit data.

### Clean up

No clean up is required for this sample.
