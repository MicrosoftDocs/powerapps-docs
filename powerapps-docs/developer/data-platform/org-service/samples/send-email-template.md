---
title: "Sample: Send an email using a template (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to send an email message by using a template." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Send an email using a template

<!-- https://learn.microsoft.com/dynamics365/customer-engagement/developer/sample-send-email-template -->

This sample shows how to send an email message by using a template using the [SendEmailFromTemplateRequest](/dotnet/api/microsoft.crm.sdk.messages.sendemailfromtemplaterequest) message.

> [!div class="nextstepaction"]
> [SDK for .NET: Send an email using a template sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/SendEmailUsingTemp)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `SendEmailFromTemplateRequest` message is intended to be used in a scenario where it contains data that is needed to send an email message using a template.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates a contact record to send an email to (To: column).

### Demonstrate

1. The `ActivityParty` creates the `From:` and `To:` activity party for the email.
2. Creates an email message.
3. The `QueryExpression` queries to get one of the email template of type `Contact`.
4. The `SendEmailFromTemplateRequest` sends an email message by using a template.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
