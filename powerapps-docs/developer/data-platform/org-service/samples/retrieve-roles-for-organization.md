---
title: " Retrieve roles for an organization (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to retrieve roles for an organization " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/20/2019
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

# Retrieve the roles for an organization

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to retrieve the roles for an organization by using the [IOrganizationService.RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple?view=dynamics-general-ce-9) method.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveRolesForOrganization).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IOrganizationService.RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple?view=dynamics-general-ce-9) message is intended to be used in a scenario where it contains data  that is needed to retrieve a collection of records.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

The `query` method retrieves all the roles that are present in an organization.

### Clean up

This sample creates no records. No cleanup is required.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]