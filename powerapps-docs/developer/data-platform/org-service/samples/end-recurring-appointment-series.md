---
title: "Sample: End a recurring appointment (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to end an recurring appointment series" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: End a recurring appointment series

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-end-recurring-appointment-series -->

This sample shows how to end a recurring appointment series by using the [DeleteOpenInstancesRequest](/dotnet/api/microsoft.crm.sdk.messages.deleteopeninstancesrequest?view=dynamics-general-ce-9) message. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/EndRecurringAppointment).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `DeleteOpenInstanceRequest` message is intended to be used in a scenario where it contains the data that is needed to delete instances of a recurring appointment master that has an `Open` state.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Defines the anonymous types that define possible recurrence pattern values, possible values for days, and recurrence rule pattern end type values.
3. Creates a new recurring appointment that is required for the sample.

### Demonstrate

1. The `RecurringAppointmentMaster` message retrieves a recurring appointment series that is created in the [Setup](#setup).
2. The `DeleteOpenInstanceRequest` message ends the recurring appointment series to the last occurring past instance date w.r.t. the series end date.

### Clean up

Display an option to delete the sample data created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]