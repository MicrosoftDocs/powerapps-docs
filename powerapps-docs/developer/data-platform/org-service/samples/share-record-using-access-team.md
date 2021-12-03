---
title: "Sample: Share a record using an access team(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to allow access to a record using an access team." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Share a record using an access team

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-share-record-using-access-team -->

This sample shows how to allow access to a record using an access team. All the members of the team will receive the same access to the record that is granted to the team. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ShareRecordUsingAccessTeam).

This sample requires additional users that are not in your system. Create the required users manually in **Microsoft 365** in order to run the sample without any errors. For this sample create a user profile **as is** shown below. Replace `yourorg` with the organization name.

**First Name**: Nancy<br/>
**Last Name**: Anderson<br/>
**Security Role**: SalesPerson<br/>
**UserName**: nanderson@yourorg.onmicrosoft.com<br/>

**First Name**: David<br/>
**Last Name**: Bristol<br/>
**Security Role**: SalesPerson<br/>
**UserName**: dbristol@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `AddMembersTeamRequest`, `GrantAccessRequest`, `RemoveMembersTeamRequest` messages are intended to be used in a scenario where it contains data that is needed to Add, Grant and Remove Members.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates a test account record for the sample.

### Demonstrate

1. Retrieves the sales persons that are created manually in **Microsoft 365** that will be added to the team.
1. The `WhoAMIRequest` gets the ID's of the current user and business unit.
1. Creates a sample access team. The `AddMembersTeamRequest`adds two sales persons to the access team.
1. The `GrantAccessRequest` grants the team read/write access to the account created in the Setup(#setup).
1. The `RetrieveAndDisplayEntityAccess` retrieves and displays table access information.
1. The `RetrieveAndDisplayPrincipalAccess` retrieves and displays principal access information.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]