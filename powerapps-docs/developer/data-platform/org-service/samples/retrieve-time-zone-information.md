---
title: "Sample: Retreive time zone information (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve time zone information" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Retrieve time zone information

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-retrieve-time-zone-information -->

This sample shows how to retrieve time zone information. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveTimeZone).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveAllTimeZonesForLocale` method is intended to be used in a scenario where it uses the current locale id to retrieve all the time zones.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `RetrieveCurrentUSerSettings` method retrieves the current users timezone code and locale id.
2. The `RetrieveAllTimeZonesForLocale` method uses the current locale id and retrieves all the time zones.
3. The `GetTimeZoneCodeByLocaleAndName` method retrieves the timezone by name and locale id.
4. The `RetrieveTimeZoneById` method retrieves the timezone by id.
5. The `RetrieveTimeZonesLessThan50` method retrieves time zones less than 50.
6. The `RetrieveLocalTimeFromUTCTime` method retrieves the local time from UTC time.
7. The `RetrieveUTCTimeFromLocalTime` method retrieves the UTC time from the locale time.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]