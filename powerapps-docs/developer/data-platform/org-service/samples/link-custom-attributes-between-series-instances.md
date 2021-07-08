---
title: "Sample: Link custom attributes between series and instances(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to link a custom attribute between series and instances" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Link custom attributes between series and instances

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to link a custom attribute that is created for a recurring appointment series (`RecurringAppointmentMaster`) with a custom attribute that is created for the appointment instances (`Appointment`). You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/LinkAttributes).

## What this sample does

The `CreateAttributeRequest` message is intended to be used in a scenario where it contains data that is needed to create custom attributes.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `StringAttributeMetadata` message creates custom string attributes for recurring appointment instance and appointment instance.
2. The `LinkedAttributeId` links the custom attribute to the appointment's custom attribute.

### Clean up

Display an option to delete the records that are created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]