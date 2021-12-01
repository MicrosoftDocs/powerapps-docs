---
title: "Sample: Use duplicate detection when creating and updating records(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to invoke duplicate detection for creating and updating table records" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Use duplicate detection when creating and updating records

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/org-service/sample-use-duplicate-detection-when-creating-and-updating-records -->
This sample shows how to invoke duplicate detection for creating and updating table records. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/UseDuplicatedetectionforCRUD).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]


## What this sample does

The `DuplicateRule` method is intended to be used in a scenario where it contains data that is needed to create duplicate detection rule.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates an account record. 
1. The `DuplicateRule` method creates a duplicate detection rule.
1. The `DuplicateRuleCondition` method creates a duplicate detection rule conditions.
1. The `PublishDuplicateRuleRequest` method publishes the duplicate detection rule created earlier. You need to wait for publishing operation to complete, so we keep polling the state of the rule until it becomes `Published`.

### Demonstrate
1. The `Account` method creates an account record. 
1. The `CreateRequest` method creates operation by suppressing duplicate detection.
1. The `UpdateRequest` method updates the retrieved account record with new account number.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]