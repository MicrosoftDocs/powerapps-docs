---
title: " Use Outlook methods (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to use the Outlook methods." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Use Dynamics 365 for Outlook class methods

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to use the methods available in the [Microsoft.Crm.Outlook.Sdk.dll](/dotnet/api/microsoft.crm.outlook.sdk?view=dynamics-outlookclient-ce-9) assembly. You can download the sample from [here]().

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `Microsoft.Crm.Outlook.sdk` assembly is used in a scenario where it contains types that provide programmatic interaction with Microsoft Dynamics 365 for Outlook and Microsoft Dynamics 365 for Microsoft Office Outlook with Offline Access.

## How this sample works

In order to simulate the scenario described above, the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `CrmOutlookService` method sets up the service.
2. The `CrmOutlookService.IsCrmClientOffline` method checks if the client is offline.
3. The `CrmOutlookService.GoOnline()` method takes the client to online. This method will automatically sync up with database, there is no need to call the `Sync()` method.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]