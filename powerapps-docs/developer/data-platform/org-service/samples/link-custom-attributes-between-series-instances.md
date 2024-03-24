---
title: "Sample: Link custom columns between series and instances (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to link a custom column between series and instances" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Link custom columns between series and instances

This sample shows how to link a custom column that is created for a recurring appointment series (`RecurringAppointmentMaster`) with a custom column that is created for the appointment instances (`Appointment`).

> [!div class="nextstepaction"]
> [SDK for .NET: Link custom columns between series and instances sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/LinkAttributes)

## What this sample does

The `CreateAttributeRequest` message is intended to be used in a scenario where it contains data that is needed to create custom columns.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `StringAttributeMetadata` message creates custom string columns for recurring appointment instance and appointment instance.
2. The `LinkedAttributeId` links the custom column to the appointment's custom column.

### Clean up

Display an option to delete the records that are created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
