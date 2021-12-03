---
title: "Sample: Synchronize data with external systems using the change tracking system (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve changes from a table and synchronize data with external systems." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Synchronize data with external systems using change tracking

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-synchronize-data-external-systems-using-change-tracking -->

This sample code shows how to retrieve changes from a table and synchronize data with external systems by using the `RetrieveEntityChanges` message with the [RetrieveEntityChangesRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieveentitychangesrequest) and [RetrieveEntityChangesResponse](/dotnet/api/microsoft.xrm.sdk.messages.retrieveentitychangesresponse) classes. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Changetracking).

For more information about the feature that this sample demonstrates, see [Use change tracking to synchronize data with external systems](../../use-change-tracking-synchronize-data-external-systems.md).
<!-- The link above won't work until the topic is published -->

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveEntityChanges` message is intended to be used in a scenario where data from an external system is synchronized and the capability to use change tracking can be used to detect and reconcile data changes.

Without a separate system required to fully replicate this scenario, this sample simulates the scenario by performing two requests. In between the requests some data is changed so that the second request will return data about what was changed over time.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Import a managed solution (ChangeTrackingSample_1_0_0_0_managed.zip) that creates a `sample_book` table that has an alternate key named `sample_bookcode`. Verify that the indexes to support the alternate key are active
1. 10 initial sample_book table records are created so that changes to those tables can be tracked.

### Demonstrate

1. Perform initial request and cache the results, including the `DataToken`
1. Update the records created in [Setup](#setup)
1. Perform a second request, this time passing the `DataVersion` with the `DataToken` value retrieved from the initial request.
1. Show the table changes returned by the second request

### Clean up

Display an option to delete the managed solution imported in [Setup](#setup), which removes the `sample_book` table and all the data created in the sample. The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the `ChangeTrackingSample` to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]