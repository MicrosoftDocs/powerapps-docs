---
title: "Sample: Send an email (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to send an email" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Send an email

This sample shows how to send an email using [SendEmailRequest](/dotnet/api/microsoft.crm.sdk.messages.sendemailrequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Send an email sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/SendEmail)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `SendEmailRequest` message is intended to be used in a scenario where it contains data that is needed to send an email message.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Contact` method creates a contact to send an email to `(To: column)`.
1. The `WhoAmIRequest` method gets the current user information to send the email `(From: column)`.
1. The `ActivityParty`method creates `To` and `From` activity party for the email.
1. The `Email` method creates an email message.

### Demonstrate

The `SendEmailRequest` method sends an email message created in the [Setup](#setup).

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
