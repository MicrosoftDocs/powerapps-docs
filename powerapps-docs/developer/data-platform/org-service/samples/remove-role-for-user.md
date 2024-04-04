---
title: "Sample: Remove a role for a user (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to remove a role for a user " # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
---

# Sample: Remove a role for a user

This sample shows how to disassociate a role from a user by using the [IOrganizationService.Disassociate](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.disassociate) method.

> [!div class="nextstepaction"]
> [SDK for .NET: Remove a role for a user sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RemoveRoleFromUser)

This sample requires an additional user that isn't available in your system. Create the required user manually in **Microsoft 365** in order to run the sample without any errors. For this sample create a user profile **as is** shown below.

**First Name**: Dan<br/>
**Last Name**: Park<br/>
**Security Role**: No security role<br/>
**UserName**: dpark@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IOrganizationService.Disassociate](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.disassociate) message is intended to be used in a scenario where it deletes a link between records.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates the records required by the sample.

### Demonstrate

1. The `query` method retrieves a role from Microsoft Dataverse.
2. The `Disassociate` message removes the role to a team.

### Clean up

This sample creates no records. No cleanup is required.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
