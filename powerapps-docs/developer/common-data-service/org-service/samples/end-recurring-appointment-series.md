---
title: "Sample: End a recurring appointment (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to end an recurring appointment series" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: End a recurring appointment series

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-end-recurring-appointment-series -->

This sample shows how to end a recurring appointment series by using the [DeleteOpenInstancesRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.deleteopeninstancesrequest?view=dynamics-general-ce-9) message.

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

1. Display an option to delete the sample data created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
