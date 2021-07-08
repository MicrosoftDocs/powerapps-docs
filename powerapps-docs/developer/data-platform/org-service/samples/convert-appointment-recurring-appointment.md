---
title: "Sample: Convert an appointment to a recurring appointment (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to convert an appointment to a recurring appointment series" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Convert an appointment to a recurring appointment

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to convert an appointment to a recurring appointment series using the [AddRecurrenceRequest](/dotnet/api/microsoft.crm.sdk.messages.addrecurrencerequest?view=dynamics-general-ce-9) message. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ConvertToRecurring).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `AddRecurrenceRequest` message is intended to be used in a scenario where it contains the data that is needed to add recurrence information to an existing appointment.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates an sample appointment that is later converted into an recurring appointment.

### Demonstrate

1. Specifies the recurrence information that needs to be added to the appointment created in the [Setup](#setup).
2. Defines the anonymous types that define the possible recurrence pattern values and also possible values for days.
3. Defines the anonymous types that define the possible values for the recurrence rule pattern and type.
4. The `RecurringAppointmentMaster` specifies the recurrence information. 
5. The `AddRecurrence` message converts the created appointment into recurring appointment.

### Clean up

Display an option to delete the sample data created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the sample data to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]