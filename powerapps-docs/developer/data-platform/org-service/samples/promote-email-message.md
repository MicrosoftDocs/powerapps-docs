---
title: "Sample: Promote an email message (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Promote an email message

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-promote-email-message -->

This sample shows how to create an email activity instance from the specified email message in Microsoft Dataverse by using the [DeliverPromoteEmailRequest](/dotnet/api/microsoft.crm.sdk.messages.deliverpromoteemailrequest?view=dynamics-general-ce-9) message. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/PromoteEmail).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `DeliverPromoteEmailRequest` message is intended to be used in a scenario where it contains data that is needed to create an email activity record from the specified email message.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. Creates a contact to send an email to (To: column).
2. The `WhoAmIRequest` retrieves the system user to send the email (From: column).
3. The `DeliverPromoteEmailRequest` message creates the request and also executes it.
4. Verify the success by defining anonymous types that define possible values for email status. 
5. Queries the delivered email, and verify the status code is `sent`.

### Clean up

Display an option to delete the records created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]