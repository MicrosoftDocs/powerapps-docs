---
title: "Sample: Retrieve email attachements for an email template(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve email attachements associated with an email template" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Retrieve email attachments for an email template

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-retrieve-email-attachments-email-template -->

This sample shows how to retrieve email attachments associated with an email template by using the [IOrganizationService.RetrieveMultiple](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple?view=dynamics-general-ce-9) method. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveEmailAttach).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService.RetrieveMultiple` method is intended to be used in a scenario where it retrieves a collection of records.


## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates a sample email template using the `Template` method.

### Demonstrate

1. The `QueryExpression` retrieves all the attachments.

### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
