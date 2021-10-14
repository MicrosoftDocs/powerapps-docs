---
title: "Sample: Share records using GrantAccess, ModifyAccess and RevokeAccess (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to share a record using grant, modify and revoke access message." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Share records using GrantAccess, ModifyAccess and RevokeAccess messages

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-share-records-using-grantaccess-modifyaccess-revokeaccess-messages 

Change sample to make sure it works with Microsoft Dataverse
-->

This sample shows how to share a record using the following messages:

[GrantAccessRequest](/dotnet/api/microsoft.crm.sdk.messages.grantaccessrequest?view=dynamics-general-ce-9)

[ModifyAccessRequest](/dotnet/api/microsoft.crm.sdk.messages.modifyaccessrequest?view=dynamics-general-ce-9)

[RevokeAccessRequest](/dotnet/api/microsoft.crm.sdk.messages.revokeaccessrequest?view=dynamics-general-ce-9)

You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/GrantModifyRevokeAccess).

This sample requires additional users that are not in your system. Create the required users manually in **Microsoft 365** in order to run the sample without any errors. For this sample create 2 user profiles **as is** shown below. Replace `yourorg` with the organization name.

**First Name**: Dan<br/>
**Last Name**: Wilson<br/>
**Security Role**: Delegate<br/>
**UserName**: dwilson@yourorg.onmicrosoft.com<br/>

**First Name**: Christen<br/>
**Last Name**: Anderson<br/>
**Security Role**: Delegate<br/>
**UserName**: canderson@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `GrantAccessRequest`, `ModifyAccessRequest`, `RevokeAccessRequest` messages are intended to be used in a scenario where it contains data that is needed to grant, modigy and revoke access.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates a unique identifier for preventing name conflicts.
3. Retrieves the user created manually in **Microsoft 365** for this sample.
4. Retrieves the root business unit for creating the team for the sample.
5. The `WhoAMIRequest` gets the current user information.
6. Creates the team and adds the users to the team. 
7. Creates an account record and also creates a task, letter to associate to the account.

### Demonstrate

1. Retrieves and displays the access that the calling user has to the created account.
2. Retrieves and displays the access that the first user has to the created account. 
3. The `GrantAccessRequest` method grants the first user `read` access to the created account.
4. The `ModifyAccessRequest` method grants the first user `delete` access to the created account.
5. The `RevokeAccessRequest` method grants the first user `revoke` access to the created account.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]