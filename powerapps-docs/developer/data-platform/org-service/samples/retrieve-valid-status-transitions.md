---
title: "Sample: Retrieve valid status transitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve valid state transitions." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Retrieve valid status transitions

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to retrieve valid state transitions regardless of whether custom state transitions have been defined for the table. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveValidTransitions).
 
## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]


## What this sample does

The `GetValidStatusOptions` method is intended to be used in a scenario where it contains data that returns valid status option transitions regardless of whether state transitions are enabled for the table.
## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `MetadataFilterExpression` method checks for table definitions.

### Demonstrate

1. The `MetadataFilterExpression` method retrieves the status options for the `Incident` table.
1. The `RetrieveMetadataChangeRequest` method retrieves the metadata.
1. The `GetValidStatusOptions` method gets the valid status transitions for each status option.

### Clean up

This sample creates no records. No clean up is required.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]