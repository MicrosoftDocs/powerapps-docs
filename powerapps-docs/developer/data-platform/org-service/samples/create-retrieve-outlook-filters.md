---
title: "Sample: Create and retrieve Outlook filters (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to create and retrieve outlook filters." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: sriharibs-msft
ms.author: srihas
manager: evchaki
ms.reviewer: pehecke
ms.topic: sample
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Sample: Create and retrieve Outlook filters

This sample shows how to retrieve filters for Outlook.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CreartRetrieveOutlookFilters).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## How this sample works

In order to simulate the scenario described above, the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `fetchXml` method creates a retrieves offline filter. In your Outlook client, this will appear in **System Filters** tab under **File -> CRM -> Synchronize -> Outlook Filters**.
2. The `InstantiateFiltersRequest` method activates the selected offline templates for the current user.
3. The `ResetUserFilterRequest` method resets the current user's offline templates to the defaults.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
