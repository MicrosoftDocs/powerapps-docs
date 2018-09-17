---
title: "Sample: Work with activity party records (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to work with activity party records" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Work with activity party records

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-work-activity-party-records -->

This sample code shows how to work with activity party records. 

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does
This sample creates some sample data, to work with activity party records. 

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup
1. Checks for the current version of the org.
1. Creates three contact records which are required for this sample.


### Demonstrate
1. Retrieves the contact records that are created in the [Setup](#setup). 
2. Creates the activity party records for each contact.
3. Also creates Letter activity and set **From** and **To** fields to the respective Activity Party entities.

### Clean up

1. Display an option to delete the records created during [Setup](#setup). If you opt **Yes** all the records will be deleted.

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
