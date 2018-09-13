---
title: "Sample: Create am email using a template (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to instantiate an email record" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Create an email using a template

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-create-email-template -->

This sample shows how to instantiate an email record by using [InstantiateTemplateRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.instantiatetemplaterequest?view=dynamics-general-ce-9) message.  

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `InstantiateTemplateRequest` message is intended to be used in a scenario where it instantiates an email record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates an account record. 
2. Defines the body and subject of the email template in **XML** format.
3. Creates an email template.

### Demonstrate

1. The `InstantiateTemplateRequest` message is used to create an email message using a template. 
2. Serialize the email message to **XML** and save to a file.


### Clean up

1. Display an option to delete the record created in [Setup](#setup).
    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
