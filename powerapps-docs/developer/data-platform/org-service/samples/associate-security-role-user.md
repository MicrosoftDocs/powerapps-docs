---
title: " Associate security role to a user (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to assign a security role to a user " # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Associate security role to a user

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to assign a security role to a user by using the [IOrganizationService.Associate](/dotnet/api/microsoft.xrm.sdk.iorganizationservice?view=dynamics-general-ce-9) message. 

This sample requires an additional user that isn't available in your system. Create the required user manually in **Microsoft 365** in order to run the sample without any errors. For this sample create a user profile **as is** shown below. 

**First Name**: Dan<br/>
**Last Name**: Park<br/>
**Security Role**: User without any roles assigned<br/>
**UserName**: dpark@yourorg.onmicrosoft.com<br/>

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AssociateSecurityRoleToUser)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IOrganizationService.Associate](/dotnet/api/microsoft.xrm.sdk.iorganizationservice?view=dynamics-general-ce-9) message is intended to be used in a scenario where it provides programmatic access to the metadata and data for an organization.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates the records required by the sample.

### Demonstrate

1. The `QueryExpression` method retrieves a role from Microsoft Dataverse.
2. The `Associate` message assigns the role to a user.

### Clean up

Display an option to delete the sample data in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]