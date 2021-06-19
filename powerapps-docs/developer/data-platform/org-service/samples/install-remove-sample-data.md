---
title: "Sample: Install and remove sample data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to install and remove sample data." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Install or remove sample data

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to install or uninstall the sample data for an organization by using the [InstallSampleDataRequest](/dotnet/api/microsoft.crm.sdk.messages.installsampledatarequest?view=dynamics-general-ce-9) message.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `InstallSampleDataRequest` message is intended to be used in a scenario where it contains data that is needed to install the sample data.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.

### Demonstrate

1. Prompts users to install or remove sample data.
2. If the user opts to install sample data, the `InstallSampleDataRequest` message installs the sample data.
3. If the user opts to uninstall the sample data, the `UninstallSampleDataRequest` message removes the sample data.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]