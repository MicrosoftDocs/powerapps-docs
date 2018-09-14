---
title: "Sample: Query the working hours of multiple users (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query the working hours of multiple hours" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Query the working hours of multiple users

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-query-working-hours-multiple-users -->

This sample shows how to retrieve the working hours of multiple users by using the [QueryMultipleSchedulesRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.querymultipleschedulesrequest?view=dynamics-general-ce-9) message.

This sample requires additional users that are not present in your system. Create the required user manually **as is** shown below in **Office 365** befor you run the sample.

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: Sales Manager<br/>
**UserName**: kcook@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `QueryMultipleScheduleRequest` message is intended to be used in a scenario where it contains data that is needed to search multiple resources for available time block that match the specified parameters.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Retrieves the current user's information and also the user, that you have created manually in **Office 365**.


### Demonstrate

1. The `QueryMultipleScheduleRequest` message retrieves the working hours of the current user and the user that you have created manually.

### Clean up
