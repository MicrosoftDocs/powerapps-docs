---
title: "Sample: Query the working hours of multiple users (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to query the working hours of multiple hours" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Query the working hours of multiple users

<!-- https://learn.microsoft.com/dynamics365/customer-engagement/developer/sample-query-working-hours-multiple-users -->

This sample shows how to retrieve the working hours of multiple users by using the [QueryMultipleSchedulesRequest](/dotnet/api/microsoft.crm.sdk.messages.querymultipleschedulesrequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Query the working hours of multiple users sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23)

This sample requires additional users that are not present in your system. Create the required user manually **as is** shown below in **Microsoft 365** before you run the sample. Replace `yourorg` with the `OrgName` of your organization.

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
2. Retrieves the current user's information and also the user, that you have created manually in **Microsoft 365**.

### Demonstrate

The `QueryMultipleScheduleRequest` message retrieves the working hours of the current user and the user that you have created manually.

### Clean up

Display an option to delete the records created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
