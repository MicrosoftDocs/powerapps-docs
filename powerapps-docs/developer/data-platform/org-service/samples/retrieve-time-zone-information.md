---
title: "Sample: Retrieve time zone information (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve time zone information" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Retrieve time zone information

This sample shows how to retrieve time zone information.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve time zone information sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveTimeZone)

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
