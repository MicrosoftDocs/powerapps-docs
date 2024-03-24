---
title: "Sample: Send bulk email and monitor results (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This samples hows how to send bulk emails and monitor results" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Send bulk email and monitor results

This sample shows how to send bulk email using the <xref:Microsoft.Crm.Sdk.Messages.SendBulkMailRequest> and monitor the results by retrieving records from the `AsyncOperation` table.

> [!div class="nextstepaction"]
> [SDK for .NET: Send bulk email and monitor results sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/BulkEmail)

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
