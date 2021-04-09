---
title: " Update a connection role (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to update a connection role" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/20/2019
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

# Update a connection role (early bound)

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to modify the properties of the connection role, such as a role name, description, and category. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/UpdateConnectionRole).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IOrganizationService.Update](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update?view=dynamics-general-ce-9) message is intended to be used in a scenario where it contains the data that is needed to update existing record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org. 
1. Creates required data that this sample requires.

### Demonstrate

The `Update` message updates the connection role.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]