---
title: "Sample: Send an email using a template(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to send an email message by using a template." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Send an email using a template

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-send-email-template -->

This sample shows how to send an email message by using a template using the [SendEmailFromTemplateRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.sendemailfromtemplaterequest?view=dynamics-general-ce-9) message.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `SendEmailFromTemplateRequest` message is intended to be used in a scenario where it contains data that is needed to send an email message using a template.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates a contact record to send an email to (To: field).

### Demonstrate

1. The `ActivityParty` creates the `From:`  and `To:` activity party for the email.
2. Creates an email message.
3. The `QueryExpression` queries to get one of the email template of type `Contact`.
4. The `SendEmailFromTemplateRequest` sends an email message by using a template.


### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
