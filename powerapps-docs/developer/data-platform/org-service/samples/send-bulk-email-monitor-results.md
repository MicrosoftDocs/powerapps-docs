---
title: "Sample: Send bulk email and monitor results(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This samples hows how to send bulk emails and monitor results" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Send bulk email and monitor results

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-send-bulk-email-monitor-results -->

This sample shows how to send bulk email using the <xref:Microsoft.Crm.Sdk.Messages.SendBulkMailRequest> and monitor the results by retrieving records from the `AsyncOperation` table. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/BulkEmail).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `SendBulkMailRequest` message is intended to be used in a scenario to send bulk emails.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org
1. The `Contact` method creates 2 contact records for this sample.

### Demonstrate

1. Gets the system user to use as the sender.
2. Set tacking id for the bulk email request.
3. Creates a query expression for the bulk operation to retrieve the contacts in the email list.
4. Set the regarding id and execute the bulk email request.
5. Retrieve the bulk email async operation and monitor it via polling.

### Clean up

Display an option to delete the records created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]