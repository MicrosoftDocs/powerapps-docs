---
title: "Sample: Audit entity data changes (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to audit entity data changes" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Audit entity data changes

This sample shows how to enable and disable auditing on an entity and its attributes, retrieve the data change history of the audited entity, and delete the audit records. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AuditEntityData).

## How to run this sample
[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveRecordChangeHistoryRequest` message is intended to be used in a scenario where it contains data that is needed to retrieve the audit history for an entity.


## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates an sample account entity.

### Demonstrate

1. Gets the organization's ID from the system user record.
2. Enabling auditing on organization and also on the sample account entity.
3. The `RetrieveRecordChangeHistoryRequest` retrieves the audit history for the account entity and displays the result.

### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
