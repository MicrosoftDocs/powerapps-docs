---
title: " Create and update emailable table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to create and update emailable table." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/17/2021
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

# Create an Email table

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to create and update a table using the [CreateEntityRequest](/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest?view=dynamics-general-ce-9) message.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CreateUpdateEmailableEntity).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateEntityRequest` message is intended to be used in a scenario where it contains  the data that is needed to create a custom table, and optionally, to add it to a specified unmanaged solution.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `Entity` method creates the custom table. Define the table to enable for emailing. In order to do so, `IsActivityParty` must be set to true.
2. The `StringAttributeMetadata` method is used to define the primary column of the table which is used in the ActivityParty screens. Be sure to select descriptive columns.
3. The `PublishRequest` method publishes all the customizations.
4. The `CreateFirstEmailAttributeRequest` method creates an email column in order to create emails from the table.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]