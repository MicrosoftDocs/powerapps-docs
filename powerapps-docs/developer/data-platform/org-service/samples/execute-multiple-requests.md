---
title: "Sample: Execute multiple requests (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to execute multiple organization messages requests by using a single web service method call." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Execute multiple requests

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to execute multiple organization message requests by using a single web service method call, passing [ExecuteMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.executemultiplerequest?view=dynamics-general-ce-9) as a parameter. Reducing the number of message requests that must be transmitted over the network results in increased message processing performance.

You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ExecutemultipleRequests).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `ExecuteMultipleRequest` message is intended to be used in a scenario where it contains data that is needed to execute one or more messages requests as a single batch operation, and optionally return a collection of results.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `ExecuteMultipleRequest` method creates the `ExecuteMultipleRequest` object.
1. The `ExecutingMultipleSettings` method assigns settings that define execution behavior: continue on error, return responses.
1. The `OrganizationRequestCollection` method creates an empty organization request collection.
1. The `CreateRequest` method is added for each table to the request collection.
1. The `GetCollectionOdEntitiesToUpdate` class updates the tables that are previously created.


### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]