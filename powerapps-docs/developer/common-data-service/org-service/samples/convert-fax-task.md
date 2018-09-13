---
title: "Sample: Convert fax to ask (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Sample that showcases how to convert a faxt into a task " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Convert a fax to a task

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-convert-fax-task -->


This sample shows how to convert a **Fax** to **Task**. To download the complete sample, clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo and go to **cds > orgsvc > C#** and search for the sample. 

## How to run this sample

See [How to run this sample](/powerapps-samples/cds/How-to-run-samples) for information about how to run this sample.

What this sample does

The `CreateRequiredRecords` method creates the sample data that is required for the sample. The `retrievedFax` method retrieves the fax. 
The `DeleteRequiredRecords` nmethod gives an option to delete all the data that sample has created.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates required data that this sample requires.


### Demonstrate
1. Retreives all the fax id's that are created in [Setup](#setup).
2. Creates a task and verifies whether the task has been created. 

### Clean up

1. Displays an option to delete all the data created in the sample.
2. The deletion is optional in case you want to exxamine the data created by the sample. You can manually delete the data to achieve same results.
