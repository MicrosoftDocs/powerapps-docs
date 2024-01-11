---
title: "Sample: Retrieve email attachements for an email template(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve email attachements associated with an email template" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
---

# Sample: Retrieve email attachments for an email template

This sample shows how to retrieve email attachments associated with an email template by using the [IOrganizationService.RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) method.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve email attachments for an email template sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveEmailAttach)

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

The `QueryExpression` retrieves all the attachments.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
