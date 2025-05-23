---
title: "Sample: Query the working hours of a user (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve the working hours of a user" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Query the working hours of a user

This sample shows how to retrieve the working hours of a user by using the [QueryScheduleRequest](/dotnet/api/microsoft.crm.sdk.messages.queryschedulerequest) message

> [!div class="nextstepaction"]
> [SDK for .NET: Query the working hours of a user sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/QueryWorkingHours)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `QueryScheduleRequest` message is intended to be used in a scenario where it contains data that is needed to search the specified resource for an available time block that matches specified parameters.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `WhoAMIRequest` message gets the current user's information.
2. The `QueryScheduleRequest` message retrieves the working hours of the current user.

### Clean up

Display an option to delete the sample data created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
