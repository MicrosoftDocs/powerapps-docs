---
title: "Sample: Export ribbon definitions(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to export ribbon definitions" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Export ribbon definitions (Microsoft Dataverse)

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to export ribbon definitions. It uses the [RetrieveApplicationRibbonRequest](/dotnet/api/microsoft.crm.sdk.messages.retrieveapplicationribbonrequest?view=dynamics-general-ce-9) and [RetrieveEntityRibbonRequest](/dotnet/api/microsoft.crm.sdk.messages.retrieveentityribbonrequest?view=dynamics-general-ce-9) messages. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ExportRibbonDefinitions).


## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveApplicationRibbonRequest` message is intended to be used in a scenario where it contains data that is needed to retrieve the data that defines the content and behavior of the application ribbon. The `RetrieveEntityRibbonRequest` message is intended to be used in a scenario where it contains data that is needed to retrieve ribbon definitions for a table.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `RetrieveApplicationRibbonRequest` method retrieves the application ribbon.
2. The `RetrieveEntityRibbonRequest` method retrieves the system ribbons

### Clean up

No clean up is required for this sample


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]