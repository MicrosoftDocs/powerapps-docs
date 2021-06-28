---
title: "Sample: Add a security principal (user or team) to a queue  (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Add a security principal to a queue" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Add a security principal (user or team) to a queue 

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample showcases how to give a user or a team access to a queue. The [AddPrincipalToQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.addprincipaltoqueuerequest?view=dynamics-general-ce-9) adds the specified principal to the list of queue members. If the passed-in security principal is a team each member of the team is added to the queue. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AddSecurityPrincipalToQueue).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `AddPrincipalToQueueRequest` message is intended to be used in a scenario where it contains data that is needed to add the specified principal to the list of queue members. If the principal is a team, add each team member to the queue.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `Queue` method creates a queue instance and set its property values. The returned GUIDs are stored in a variable.
3. The `QueryExpression` retrieves the default business unit for the creation of the team and role.
4. Creates a new example team and role required for the sample.
5. Retrieves the `prvReadQueue` and `prvAppendToQueue` privileges.
6. The `AddPrivilegeRoleRequest` method adds the `prvReadQueue` and `prvAppendToQueue` privileges to the example role.

### Demonstrate

The `AddPrincipalToQueueRequest` method adds the team to the queue.

### Clean up

Display an option to delete the sample data in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]