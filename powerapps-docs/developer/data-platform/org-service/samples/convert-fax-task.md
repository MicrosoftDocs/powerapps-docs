---
title: "Sample: Convert fax to ask (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Sample that showcases how to convert a fax into a task " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Convert a fax to a task

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-convert-fax-task -->


This sample shows how to convert a **Fax** to a **Task**. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ConvertFaxToTask).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]


## What this sample does

The `CreateRequiredRecords` method creates the sample data that is required for the sample. The `retrievedFax` method retrieves the fax. 
The `DeleteRequiredRecords` method gives an option to delete all the data that sample has created.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `WhoAmIRequest` method gets the current user details.
1. The `ActivityParty` method creates the activity party for sending and receiving fax.
1. The `Fax` method creates the fax required for the sample.


### Demonstrate

1. Retrieves all the fax id's that are created in [Setup](#setup).
2. Creates a task and verifies whether the task has been created. 

### Clean up

1. Displays an option to delete all the data created in the sample.
2. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]