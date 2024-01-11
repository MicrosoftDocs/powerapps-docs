---
title: "Sample: Book an appointment (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to book or schedule an appointment " # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Book an appointment

This sample shows how to book or schedule an appointment by using the [BookRequest](/dotnet/api/microsoft.crm.sdk.messages.bookrequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Book an appointment sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/BookAppointment)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `BookRequest` message is intended to be used in a scenario to book or schedule an appointment.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks the current version of the org.
1. Gets the current user information and creates the ActivityParty instance.

### Demonstrate

Creates the appointment instance using the [BookRequest](/dotnet/api/microsoft.crm.sdk.messages.bookrequest) message and verifies that the appointment has been scheduled or not.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
